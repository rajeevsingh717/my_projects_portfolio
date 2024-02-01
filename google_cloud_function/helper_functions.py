from bs4 import BeautifulSoup
import requests
import datetime
import csv
import os
from google.cloud import storage
from google.oauth2 import service_account


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}


# function to upload the file to GCS bucket
def file_upload_google_storage(project_id, bucket_name, gcs_file_name, csv_filename):
    credentials = service_account.Credentials.from_service_account_file('service_account.json')
    client = storage.Client(credentials=credentials, project=project_id)
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(gcs_file_name)
    blob.upload_from_filename(csv_filename)


# writing the data to csv file
def write_csv_file(data,csv_filename):
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


# Below function captures data from yahoo finance. It captures the most active stocks.
# The below function does not capture the 52-week range info


def getmostactive25_stocks() -> list:
    base_url = 'https://finance.yahoo.com/most-active'
    page = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find('table') # Find the table in the HTML
    prices = [] # Initialize empty lists to store the table data
    # Iterate through the rows of the table
    data_capture_time = datetime.datetime.now()
    for row in table.find_all('tr'):
        columns = row.find_all('td')  # Assuming data is in <td> elements
        row_data = [column.get_text() for column in columns]
        row_data.append(data_capture_time.strftime('%Y-%m-%d %H:%M:%S'))
        prices.append(row_data)
    header = ['Symbol', 'Name', 'Price (Intraday)', 'Change', '% Change', 'Volume', 'Avg Vol (3 month)', 'Market Cap',
              'PE Ratio (TTM)', '52 Week Range','data_capture_datetime']
    prices[0] = header
    return prices