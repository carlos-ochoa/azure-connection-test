import pandas as pd
import pandas_gbq
from google.cloud import bigquery
from google.oauth2 import service_account


query = """SELECT * FROM fh-bigquery.nyc.traffic_tickets LIMIT 10"""

table = "azure-performance-test.testAZ.parking violations"
key_path = "azure-performance-test-98fd0d574ffe.json"

print("Authenticating with GCP...")

credentials = service_account.Credentials.from_service_account_file(
    key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

pandas_gbq.context.credentials = credentials
pandas_gbq.context.project = "azure-performance-test"



#df.to_gbq(table, if_exists = 'replace')

print("Reading Data from Test Table with pandas-gbq...")

df2 = pd.read_gbq(query)
print(df2)

print("Writing Data to Test Table with pandas-gbq...")
df2.to_gbq(table, if_exists = 'replace')

print("Performing a reading query with BigQuery client...")
client = bigquery.Client(credentials=credentials, project=credentials.project_id,)

model_details_df = client.query(query).result().to_dataframe(create_bqstorage_client=True,)

print(model_details_df)