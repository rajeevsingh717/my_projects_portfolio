FROM python:3
ADD getdata.py .
ADD cust.csv .
RUN pip install pandas
CMD [ "python", "./getdata.py" ]
