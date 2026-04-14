from round_trip_config_vars import flight_query_details
from functions_code import load_raw_data, get_flight_details
from datetime import datetime
import csv


if __name__ == "__main__":
    current_timestamp = datetime.now().timestamp()
    current_datetime = datetime.fromtimestamp(current_timestamp)
    formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')

    url = flight_query_details['url']
    origin = flight_query_details['origin']
    destination = flight_query_details['destination']
    start_date = flight_query_details['start_date']
    return_date = flight_query_details['return_date']

    flight_list = get_flight_details(url, origin, destination, start_date, return_date, formatted_datetime)

    file_name = origin+'_'+destination+'_'+start_date+'_'+return_date+'_'+str(formatted_datetime)
    file_path = 'data/'+file_name
    if len(flight_list) > 0:
        print("found the flights")
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(flight_list)

    # loading data in postgres
    load_raw_data(file_path)


