import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import gspread
import json


class q2googledrive:
    def __init__(self, token="token.json", secrets="credentials.json"):
        self.SCOPES = [
            "https://www.googleapis.com/auth/drive.metadata.readonly",
            "https://www.googleapis.com/auth/drive.readonly",
        ]
        self.token = None
        self.token_data = token
        self.secrets = secrets
        self.google_sheets = None
        if self.token_data and self.secrets:
            self.login()

    def login(self):
        if isinstance(self.token_data, str) and os.path.exists(self.token_data):
            self.token = Credentials.from_authorized_user_file(self.token_data, self.SCOPES)
        elif isinstance(self.token_data, str):
            try:
                token_data = json.loads(self.token_data)
                self.token = Credentials.from_authorized_user_info(token_data)
            except Exception as error:
                print(f"An error occurred while jsonify token data: {error}")
        else:
            self.token = Credentials.from_authorized_user_info(self.token_data)

        if not self.token or not self.token.valid:
            if self.token and self.token.expired and self.token.refresh_token:
                self.token.refresh(Request())
            else:
                if isinstance(self.secrets, str) and os.path.exists(self.secrets):
                    flow = InstalledAppFlow.from_client_secrets_file("credentials.json", self.SCOPES)
                elif isinstance(self.token_data, str):
                    flow = InstalledAppFlow.from_client_config(json.loads(self.secrets), self.SCOPES)
                else:
                    flow = InstalledAppFlow.from_client_config(self.secrets, self.SCOPES)
                self.token = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open("token.json", "w") as token:
                token.write(self.token.to_json())
        try:
            self.drive = build("drive", "v3", credentials=self.token)
        except HttpError as error:
            self.drive = None
            print(f"An error occurred: {error}")

    def dir(self, q=""):
        return self.drive.files().list(q=q, fields="files(id, name)").execute().get("files", [])

    def load_docs(self, id):
        return self.load(id, "application/vnd.openxmlformats-officedocument.wordprocessingml.document")

    def load_odt(self, id):
        return self.load(id, "application/vnd.oasis.opendocument.text")

    def load_xlsx(self, id):
        return self.load(id, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

    def load_ods(self, id):
        return self.load(id, "application/x-vnd.oasis.opendocument.spreadsheet")

    def load(self, id, mimeType):
        return self.drive.files().export(fileId=id, mimeType=mimeType).execute()

    def n2c(self, n):
        return chr(n + 64) if n <= 26 else self.n2c((n - n % 26) // 26) + self.n2c(n % 26)

    def load_spreadsheet_dict(self, id):
        if self.google_sheets is None:
            self.google_sheets = gspread.oauth(credentials_filename=self.secrets)

        if self.google_sheets is None:
            return ""

        sheet = self.google_sheets.open_by_key(id)
        rez = {}
        for worksheet in sheet.worksheets():
            rez[worksheet.title] = {}
            for row_number, row in enumerate(sheet.worksheet(worksheet.title).get_all_values()):
                rez[worksheet.title][row_number + 1] = {}
                for column_number, cell in enumerate(row):
                    rez[worksheet.title][row_number + 1][self.n2c(column_number + 1)] = cell
        return rez


if __name__ == "__main__":
    q2gd = q2googledrive()
    print(len(q2gd.load_docs("13uo49QJ3ouEZL1prgp9h7T1EZz_QX1DJh6hL3Bb7NiM")))
    # files = q2gd.dir("mimeType='application/vnd.google-apps.document' and name contains '/data2doc/'")
    # for x in files:
    #     print(x)
    # print(q2gd.load_spreadsheet_dict("19xpPvbIqVZ2ITveS-DUI3vwSBnSWPXc3qWc1NYtRREs"))
