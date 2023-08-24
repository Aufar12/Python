import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

# Credentials.json bisa diambil dari google developer console
# https://docs.gspread.org/en/v5.10.0/oauth2.html#enable-api-access-for-a-project
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)

client = gspread.authorize(creds)
wb = client.open("Nama Spreadsheet Yang ingin Dituju")

for i in range(1,4):
    sheet = wb.worksheet('Sheet'+str(i))
    sheet.clear()

sheet.update('C1:D2', [[1, 2], [3, 4]])

