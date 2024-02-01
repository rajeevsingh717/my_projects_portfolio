import datetime
import logging
import os

from helper_functions import getmostactive25_stocks, write_csv_file, file_upload_google_storage



def datacollection(request):
  logging.info("starting the function here")
  data = getmostactive25_stocks()

  # writing the captured data to local CSV file
  logging.info("writing the captured data to local CSV file")
  filename="raw_most_active_25_stocks"+datetime.datetime.now().strftime('_%Y-%m-%d_%H:%M:%S')+".csv"
  write_csv_file(data, filename)

  # saving the file to gcs
  logging.info("saving the file to gcs")
  project_id = os.environ.get('project_id')
  bucket_name = os.environ.get('gcs_bucket_name')
  gcs_file_name = "most_active_25_stocks/"+filename # path with file name
  file_upload_google_storage(project_id, bucket_name, gcs_file_name, filename)
 

  return data

if __name__=='__main__':
  datacollection(request)