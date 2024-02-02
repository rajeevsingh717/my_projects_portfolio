import pandas as pd
import time
import csv
import os
import sys
import boto3


AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
INPUT_FILE_NAME = os.environ['INPUT_FILE_NAME']

client = boto3.client("s3",region_name='us-east-1',
                         aws_access_key_id=AWS_ACCESS_KEY_ID,
                         aws_secret_access_key=AWS_SECRET_ACCESS_KEY)


# downloading the file from s3 to local folder
client.download_file('rajeev-dev', 'raw/'+INPUT_FILE_NAME, INPUT_FILE_NAME)


#Print the files in docker root directory
# files = os.listdir()
# for file in files:
#     print(file)


#reading the file
df=pd.read_csv("employee.csv")


df1 = df.copy()
df1["new salary"] = df1["salary"]*10


#print(os.getcwd())


##converting into list
header = list(df1)
rows =[]
for i in range (0,len(df1)):
  value = list(df1.iloc[i])
  rows.append(value)

processed_file_name="new_salary.csv"

with open(processed_file_name, 'w') as csvfile:
  csvwriter = csv.writer(csvfile) 
  csvwriter.writerow(header)
  csvwriter.writerows(rows)


##copying the file to S3 from docker file system
client.upload_file(processed_file_name, "rajeev-dev", "processed/"+processed_file_name)



print(rows)
