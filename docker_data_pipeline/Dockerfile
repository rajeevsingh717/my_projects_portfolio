FROM python:3.7.6-buster

RUN echo "hello, i am in a container"

ENV AWS_ACCESS_KEY_ID=<access_key>
ENV AWS_SECRET_ACCESS_KEY=<secret_key>
ENV INPUT_FILE_NAME=employee.csv



RUN pip install --upgrade pip

RUN apt-get update && apt-get install -y awscli

RUN aws configure set aws_access_key_id $AWS_ACCESS_KEY_ID
RUN aws configure set aws_secret_access_key $AWS_SECRET_ACCESS_KEY	


ADD change_salary.py .

ADD requirements.txt .

#ADD employee.csv .

RUN pip install -r requirements.txt

CMD [ "python", "./change_salary.py" ]




