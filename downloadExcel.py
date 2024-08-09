import os
import requests
import sys

def getGoogleSeet(spreadsheet_id, outDir, outFile):
  
  url = f'https://docs.google.com/spreadsheets/d/{spreadsheet_id}/export?format=csv'
  response = requests.get(url)
  if response.status_code == 200:
    filepath = os.path.join(outDir, outFile)
    with open(filepath, 'wb') as f:
      f.write(response.content)
      print('CSV file saved to: {}'.format(filepath))    
  else:
    print(f'Error downloading Google Sheet: {response.status_code}')
    sys.exit(1)


##############################################

outDir = 'public/'

os.makedirs(outDir, exist_ok = True)
filepath = getGoogleSeet('14MAEAGOOf56EBViRK6Ee9M0Eb4bGpqRq08SH-kj6D70', outDir, "stats.csv")

sys.exit(0); ## success