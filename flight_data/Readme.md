## Bugs
    Bug#1 - get_flight_details function is not fetching the data for round trip flight search. Not able to change the travel date when the browser is opened.

## Future changes & improvement    
    change#1 - Be able to invoke the one way/ round trip searches from flask app by button push. Also show the data on html page.
    Show the data in the ascending order of prices
    
    chnage#2 - find the 30 days flight data seperatly from source to target airport and vice versa. 
    Then find the best combination of start and end travel dates from the dataset by considering multiple factors like price and preferred travel date
    

## Files and executables description and purpose
    round_trip_flight_data.py - Python file to get the round trip data. Run this to saerch for round trip flights
        round_trip_config_vars.py - Python file to keep flight related variables which are used to lookup for flights

    one_way_flight_data.py - Python file to get the one way flight data. Can use this to search for next "n" number of days to search for flights. 
        one_way_config_vars.py - Python file to keep flight related variables which are used to lookup for flights
    
    functions_code.py - Python file which has functions to lookup flight details and also to load flight data into postgres SQL
        get_one_way_flight_details - Function to get one way flight data
        get_flight_details - Function to get round trip flight data
        load_one_way_raw_data - load the one way flight data in postgres
        load_raw_data - load the round trip flight data in postgres
        
        


## How to make a local folder as git repo
    Run the following command inside the local folder which you want to convert in git repo

        git init -b main       
        git add .    
        git commit -m "first commit for flight_data app"
    
    Then add the local folder to "add local repository" on the "file" menu in Github desktop. Then push it to origin




## database commands
    
    --------round_trip_flight_details-------
    truncate table flight_details
    
    drop table flight_details;
    
    create table flight_details (
    from_city varchar(100),
    to_city varchar(100),
    start_date varchar(100),  
    return_date varchar(100), 
    airline varchar(100), 
    departure_time varchar(100), 
    arrival_time varchar(100), 
    duration varchar(100), 
    price varchar(100), 
    departure_airport varchar(100), 
    arrival_airport varchar(100), 
    etl_create_date varchar(100))
    
    
    select * from flight_details;
    
    select * from flight_details order by cast(price as int)


    --------one_way_flight_details-------
    truncate table one_way_flight_details;
    
    drop table one_way_flight_details;
    
    create table one_way_flight_details (
    from_city varchar(100),
    to_city varchar(100),
    travel_date varchar(100),  
    airline varchar(100), 
    departure_time varchar(100), 
    arrival_time varchar(100), 
    duration varchar(100), 
    price int, 
    departure_airport varchar(100), 
    arrival_airport varchar(100), 
    etl_create_date varchar(100));
    
    select * from one_way_flight_details;
    
    select * from one_way_flight_details order by cast(price as int)
