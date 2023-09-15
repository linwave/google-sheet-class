import httplib2
import apiclient
import time
from oauth2client.service_account import ServiceAccountCredentials


class GoogleSheets():
    # Файл, полученный в Google Developer Console
    CREDENTIALS_FILE = 'luxun-bot-a404ce32119e.json'
    # ID Google Sheets документа (можно взять из его URL)
    spreadsheet_id = '1eRoIfuCVodQET5UaoUFyhhEPuhCioQ6kVoO1T5m1-mk'

    # Авторизуемся и получаем service — экземпляр доступа к API
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE,
        ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)

    def getRangeValues(self, range):
        values1 = self.service.spreadsheets().values().get(
            spreadsheetId=self.spreadsheet_id,
            range=range,
            majorDimension='ROWS'  # 'COLUMNS'
        ).execute()
        aaa = values1.get('values', [])
        return aaa

    def updateRangeValues(self, range, values):
        data = [{
            'range': range,
            'values': values
        }]
        body = {
            'valueInputOption': 'USER_ENTERED',
            'data': data
        }
        self.service.spreadsheets().values().batchUpdate(spreadsheetId=self.spreadsheet_id,
                                                         body=body).execute()

# gs = GoogleSheets()
# range = "Example!A2:B"
# data = gs.getRangeValues(range)

# gs = GoogleSheets()
# range = "Example!A2:B"
# data = gs.getRangeValues(range)

# range = "Example!A5:B6"
# data = [
#     [0, 1],
#     [0, 0]
# ]
# gs.updateRangeValues(range, data)
# def google_data():
#     # # Пример чтения файла
#     values1 = service.spreadsheets().values().get(
#         spreadsheetId=spreadsheet_id,
#         range='Example!A2:B',
#         majorDimension='ROWS'  # 'COLUMNS'
#     ).execute()
#     aaa = values1.get('values', [])
#     return aaa
#
# Пример записи в файл
# values = service.spreadsheets().values().batchUpdate(
#     spreadsheetId=spreadsheet_id,
#     body={
#         "valueInputOption": "USER_ENTERED",
#         "data": [
#             {"range": "Example!A5:B7",
#              "majorDimension": "ROWS",
#              "values": aaa}
#         ]
#     }
# ).execute()
