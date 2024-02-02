# docker_data_pipeline
Data pipeline built using docker container. Picking file and dropping the file in S3

Performing following steps using docker container:
	
	1) Copy raw data from s3 to conatiner along with other dependecny(packages like pandas, numpy)
	2) processing the data using python
	3) Copying the processed data back to AWS S3 bucket.

Other info:
	
	1) Command to build the container 
		docker build -t docker_data_pipeline .

	2) Command to run the container 
		docker run docker_data_pipeline 

Files need to run the full application:-
	
	1) Dockerfile - to get all the dependency
	2) change_salary.py - Python program to process the data
	3) requirements.txt - contains the list of all the packages needed for python program
	4) Readme - Optional file - Just needed to explain all aspect of Application.


