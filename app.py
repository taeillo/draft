from flask import Flask, request, redirect, jsonify, render_template 
from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'keys.json'

username = None
password = None

app = Flask(__name__) 

@app.route('/order', methods=['POST','GET'])
def order():
    return render_template('order.html')

@app.route('/', methods=['POST','GET'])
@app.route('/index', methods=['POST','GET'])
def index():
    return render_template('index.html')

@app.route('/index.css')
def main1():
    return app.send_static_file('styles/index.css')

@app.route('/index.js')
def main2():
    return app.send_static_file('javascript/index.js')

@app.route('/offline')
def offline():
    return app.send_static_file('offline.html')

@app.route('/asset-manifest.json')
def manifest():
    return app.send_static_file('manifest.json')



creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('sheets', 'v4', credentials=creds)

# If modifying these scopes, delete the file token.json.


# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1HQevvoML_FZVEHkwgD66Gyw836lgjR93v_zI632P070'

# Read from sheet

sheet = service.spreadsheets()

result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Form Responses 1!A1:N20").execute()
values = result.get('values', [])

print(values)

# Update to sheet

data = [[]]

updated_result = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Form Responses 1!A1", valueInputOption="USER_ENTERED", body={"values":data}).execute()

print('{0} cells updated.'.format(updated_result.get('updatedCells')))





if __name__ == "__main__":
    app.run(debug=True)
