##submit a build job to Google Cloud Build,
gcloud builds submit --tag gcr.io/storied-link-399820/chucknorrisjokes

##to deploy the job
gcloud run deploy --image gcr.io/storied-link-399820/chucknorrisjokes

## create a schedular
gcloud scheduler jobs create http scheduler_chuck_norris_jokes_ingestion \
--schedule="*/2 * * * *" \
--uri="https://chucknorrisjokes-idscha5xgq-ue.a.run.app/capture-data" \
--http-method="GET" \
--time-zone="America/New_York" \
--oidc-service-account-email="cloud-dts-sa-737d400d@stor-link-399.iam.gserviceaccount.com" \
--description="pulling chuck norris jokes" \
--project="storied-link-399820"

##to run the schedular
gcloud scheduler jobs run scheduler_chuck_norris_jokes_ingestion


