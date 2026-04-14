import psycopg2
import os
import csv
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from bs4 import BeautifulSoup
import re
import csv
import time


def remove_break_space(text):
    return re.sub(r"\u202f", "", text)


def get_one_way_flight_details (url, origin, destination, start_date, etl_create_date):
    # Launch a web browser (Chrome in this example)
    s = Service(executable_path='/Users/rajeevsingh/scripts/chromedriver')
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    print(f'searching for flight from {origin} to {destination}')
    print('reaching:- ', url)
    driver.get(url)
    time.sleep(2)
    # click on the drop down
    drop_down = driver.find_element(By.CLASS_NAME, "VfPpkd-aPP78e")
    drop_down.click()
    time.sleep(2)

    # Click on one way
    one_way_element = driver.find_element(By.XPATH, "//li[contains(., 'One way')]")
    one_way_element.click()
    time.sleep(2)

    # performing the browser automation here
    input_element = driver.find_element(By.CSS_SELECTOR, "input[jsname='yrriRe']")
    input_element.clear()
    input_element.send_keys(origin)
    time.sleep(2)

    # select the first value from the drop down
    drop_down_location = driver.find_element(By.CLASS_NAME, "CwL3Ec")
    drop_down_location.click()
    time.sleep(2)

    # fill the destination
    input_element = driver.find_element(By.CSS_SELECTOR, "input[aria-label='Where to? ']")
    input_element.send_keys(destination)
    time.sleep(2)

    # select the first entry from dropdown
    drop_down_location = driver.find_element(By.CLASS_NAME, "CwL3Ec")
    drop_down_location.click()
    time.sleep(2)

    # fill in the travel date
    travel_date_fill = driver.find_element(By.XPATH, "//input[@aria-label='Departure']")
    travel_date_fill.send_keys(start_date)
    time.sleep(2)

    # Click on Done button for date
    actions = ActionChains(driver)
    actions.move_by_offset(10, 10)
    actions.click()
    actions.perform()
    time.sleep(4)

    # click the search button
    search_button = driver.find_element(By.XPATH, '//span[contains(text(), "Search")]')
    search_button.click()
    time.sleep(4)

    driver.implicitly_wait(10)
    html = driver.page_source

    # Parse the HTML content
    soup = BeautifulSoup(html, 'html.parser')
    flight_containers = soup.find_all('div', class_='KhL0De')
    flight_list = []
    for flight_container in flight_containers:
        # Extract flight details
        airline = flight_container.find('div', class_='sSHqwe tPgKwe ogfYpf').find('span').text
        departure_time_element = flight_container.find('span',
                                                       attrs={'aria-label': lambda x: x and 'Departure time' in x})
        if departure_time_element:
            departure_time = departure_time_element.text
        else:
            departure_time = "N/A"

        arrival_time_element = flight_container.find('span', attrs={'aria-label': lambda x: x and 'Arrival time' in x})
        if arrival_time_element:
            arrival_time = arrival_time_element.text
        else:
            arrival_time = "N/A"
        # arrival_time = flight_container.find('span', aria-label=lambda x: x and 'Arrival time' in x).text
        duration = flight_container.find('div', class_='gvkrdb AdWm1c tPgKwe ogfYpf').text

        try:
            price = flight_container.find_all('span', role='text')[2].text
        except IndexError:
            price = "$0"

        price = price[1:]
        departure_airport = flight_container.find_all('span', class_='eoY5cb')[2].text
        arrival_airport = flight_container.find_all('span', class_='eoY5cb')[3].text
        curr_list = [origin, destination, start_date, airline, remove_break_space(departure_time),
                     remove_break_space(arrival_time), duration, price, departure_airport, arrival_airport,
                     etl_create_date]
        flight_list.append(curr_list)
    # Close the browser
    driver.quit()

    return flight_list


def load_one_way_raw_data(data):
    # Database connection parameters
    dbname = 'postgres'
    user = 'postgres'
    password = ''
    host = 'localhost'  # or your database host
    port = '5432'  # or your database port

    # Connect to the PostgreSQL database
    try:
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        cursor = conn.cursor()
        print("Connected to the database")

        # Specify the path to your CSV file
        csv_file = data

        # Open the CSV file and read its contents
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row if present
            for row in reader:
                # Insert each row into the database table
                cursor.execute(
                    "INSERT INTO one_way_flight_details (from_city, to_city, travel_date, airline, departure_time, arrival_time, duration, price, departure_airport, arrival_airport, etl_create_date) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    row
                )
            print("CSV data inserted into the table")

        # Commit the transaction
        conn.commit()

    except psycopg2.Error as e:
        print("Error connecting to the database:", e)

    finally:
        # Close the database connection
        if conn is not None:
            conn.close()
            print("Database connection closed")


def load_raw_data(data):
    # Database connection parameters
    dbname = 'postgres'
    user = 'postgres'
    password = ''
    host = 'localhost'  # or your database host
    port = '5432'  # or your database port

    # Connect to the PostgreSQL database
    try:
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        cursor = conn.cursor()
        print("Connected to the database")

        # Specify the path to your CSV file
        csv_file = data

        # Open the CSV file and read its contents
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row if present
            for row in reader:
                # Insert each row into the database table
                cursor.execute(
                    "INSERT INTO flight_details (from_city, to_city, start_date, return_date, airline, departure_time, arrival_time, duration, price, departure_airport, arrival_airport, etl_create_date) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    row
                )
            print("CSV data inserted into the table")

        # Commit the transaction
        conn.commit()

    except psycopg2.Error as e:
        print("Error connecting to the database:", e)

    finally:
        # Close the database connection
        if conn is not None:
            conn.close()
            print("Database connection closed")


def get_flight_details(url, origin, destination , start_date, return_date, etl_create_date):
    # Launch a web browser (Chrome in this example)
    s = Service(executable_path='/Users/rajeevsingh/scripts/chromedriver')
    driver = webdriver.Chrome(service=s)

    request_url = url.format(origin, destination, start_date, return_date)
    print(request_url)
    print(f'searching for flight from {origin} to {destination}. Start_date is {start_date} and return_date is {return_date}' )
    driver.get(request_url)
    time.sleep(5)
    driver.implicitly_wait(10)
    html = driver.page_source

    # Parse the HTML content
    soup = BeautifulSoup(html, 'html.parser')
    flight_containers = soup.find_all('div', class_='KhL0De')
    flight_list = []
    for flight_container in flight_containers:
        curr_list = []
        # Extract flight details
        airline = flight_container.find('div', class_='sSHqwe tPgKwe ogfYpf').find('span').text
        departure_time_element = flight_container.find('span', attrs={'aria-label': lambda x: x and 'Departure time' in x})
        if departure_time_element:
            departure_time = departure_time_element.text
        else:
            departure_time = "N/A"

        arrival_time_element = flight_container.find('span', attrs={'aria-label': lambda x: x and 'Arrival time' in x})
        if arrival_time_element:
            arrival_time = arrival_time_element.text
        else:
            arrival_time = "N/A"
        # arrival_time = flight_container.find('span', aria-label=lambda x: x and 'Arrival time' in x).text
        duration = flight_container.find('div', class_='gvkrdb AdWm1c tPgKwe ogfYpf').text
        price = flight_container.find_all('span', role='text')[2].text
        price = price[1:]
        departure_airport = flight_container.find_all('span', class_='eoY5cb')[2].text
        arrival_airport = flight_container.find_all('span', class_='eoY5cb')[3].text
        curr_list = [origin, destination, start_date, return_date, airline, remove_break_space(departure_time), remove_break_space(arrival_time), duration, price, departure_airport, arrival_airport, etl_create_date]
        flight_list.append(curr_list)
    # Close the browser
    driver.quit()

    return flight_list