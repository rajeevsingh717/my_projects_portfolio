from flask import Flask, request, jsonify
import os
import requests
import json
from google.cloud import bigquery
from google.oauth2 import service_account

app = Flask(__name__)


def load_data(data):
    print("inside load function")

    # data = [{"value":"chuck norris is great", "id":"1"}]  # sample data
    print(data)
    
    ## Set up the google BQ connection
    credentials = service_account.Credentials.from_service_account_file('storied-link-399820-72dd239c9bc9.json')
    project_id = 'project-id'
    client = bigquery.Client(credentials=credentials, project=project_id)

    # Reference your BigQuery dataset and table
    dataset_id = 'dataset1'
    table_id = 'raw_chuck_norris_jokes'

    # Load data into BigQuery
    table_ref = client.dataset(dataset_id).table(table_id)
    errors = client.insert_rows_json(table_ref, data)
    print(errors)
    if not errors:
        return "Data loaded into BigQuery successfully", 200
    else:
        return "Failed to load data into BigQuery", 500


@app.route('/capture-data', methods=['GET'])
def capture_data():
    api_url = 'https://api.chucknorris.io/jokes/random'  # Replace with the actual API URL
    response = requests.get(api_url)
    if response.status_code == 200:
        data = [response.json()]

        ## calling the fucntion to insert data into the BQ
        errors = load_data(data)
        print(errors)

        return jsonify(data)
    else:
        return "Failed to fetch data from the API", 500

if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", 8080)),host='0.0.0.0',debug=True)
    # app.run(debug=True)
