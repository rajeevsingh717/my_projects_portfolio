from one_way_config_vars import one_way_flight_query_details
from functions_code import load_one_way_raw_data, get_one_way_flight_details
from datetime import datetime, timedelta
import csv

if __name__ == "__main__":
    current_timestamp = datetime.now().timestamp()
    current_datetime = datetime.fromtimestamp(current_timestamp)
    formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')

    url = one_way_flight_query_details['url']
    origin = one_way_flight_query_details['origin']
    destination = one_way_flight_query_details['destination']
    start_date = one_way_flight_query_details['start_date']
    num_of_days = one_way_flight_query_details['numofdays']

    for i in range(num_of_days):
        print(i, "----", start_date)
        flight_list = get_one_way_flight_details(url, origin, destination, start_date, formatted_datetime)

        file_name = origin+'_'+destination+'_'+start_date+'_'+str(formatted_datetime)
        file_path = 'data/'+file_name
        if len(flight_list) > 0:
            print("found the flights")
            with open(file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(flight_list)

            # loading data in postgres
            load_one_way_raw_data(file_path)
            print("job finished")

        # increasing the travel date by one day
        original_date = datetime.strptime(start_date, "%Y-%m-%d")
        new_date = original_date + timedelta(days=1)
        new_date_str = new_date.strftime("%Y-%m-%d")
        start_date = new_date_str


