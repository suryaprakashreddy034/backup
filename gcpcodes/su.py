import os
from google.oauth2 import service_account
from google.cloud import bigquery

from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file(r"D:/workingcodes/gcptraining-321605-db605757c153.json")





client = bigquery.Client(credentials=credentials)
filename = 'D:/EmployeeData.json'
dataset_id = 'DatasetName'
table_id = 'TableName'

dataset_ref = client.dataset(dataset_id)
table_ref = dataset_ref.table(table_id)
job_config = bigquery.LoadJobConfig()
job_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
job_config.autodetect = True

with open(filename, "rb") as source_file:
    job = client.load_table_from_file(
        source_file,
        table_ref,
        location="europe-west1",  # Must match the destination dataset location.
        job_config=job_config,
    )  # API request

job.result()  # Waits for table load to complete.

print("Loaded {} rows into {}:{}.".format(job.output_rows, dataset_id, table_id))