# chuckNorissJokes
## Link to the Medium Story
https://medium.com/@rajsigh717/google-cloud-run-web-app-to-store-chucknorris-jokes-55823da78ba2

## overwriting the variable
export FLASK_APP=main

## Running the flask app
flask run

## kill the pid
kill -9 33977

## find the pids to kill
sudo lsof -i :5000


## table creation Script
create or replace table dataset1.raw_chuck_norris_jokes
(
categories array < string >,
created_at timestamp,
icon_url string,
id String,
updated_at timestamp,
url string,
value string
);

## sample insert query
insert  into dataset1.raw_chuck_norris_jokes values ([],'2020-01-05 13:42:29.569033','https://assets.chucknorris.host/img/avatar/chuck-norris.png', 'qJ9lipf0RFeWLTNGNbwCBg', '2020-01-05 13:42:29.569033', 'https://api.chucknorris.io/jokes/qJ9lipf0RFeWLTNGNbwCBg', 'The jokes are slacking, pick up the paste guys, or Chuck Norris will Virtually Roundhouse your asses!!')


## gcloud project list
gcloud projects list


## submit a build job to Google Cloud Build
gcloud builds submit --tag gcr.io/storied-link-399820/chucknorrisjokes

## to deploy the job
gcloud run deploy --image gcr.io/storied-link-399820/chucknorrisjokes


## to test docker image locally. following command builds the container
docker build -t chucknorrisjokes .

## to test docker image locally. command to run the conatiner
docker run  chucknorrisjokes


## Issue - 
There was an issue with the PORT not listning on Docker application. It was happening because of wrong syntax code which was added in docker file
Error that was found while testing the dcoker image locally - "gunicorn: error: unrecognized arguments: --log-level-debug". Then I removed these arguments from Dockerfile. That fixed the PORT issue.
