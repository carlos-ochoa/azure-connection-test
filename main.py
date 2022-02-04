import pandas as pd
import pandas_gbq
from google.cloud import bigquery
from google.oauth2 import service_account

data = {
    'PersonID' : [1,2,3],
    'LastName' : ['Ochoa','Rico','Forero'],
    'FirstName' : ['Carlos','Juan','Juliana'],
    'Address' : ['1','2','3'],
    'City' : ['CDMX','Bogota','Bogota']
}

query = """SELECT * FROM linen-cipher-312918.test.Persons"""

df = pd.DataFrame(data)

table = "linen-cipher-312918.test.Persons"
key_path = "linen-cipher-312918-7f6148510d0b.json"

print("Authenticating with GCP...")

credentials = service_account.Credentials.from_service_account_file(
    key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

pandas_gbq.context.credentials = credentials
pandas_gbq.context.project = "linen-cipher-312918"

print("Writing Data to Test Table with pandas-gbq...")

df.to_gbq(table, if_exists = 'replace')

print("Reading Data from Test Table with pandas-gbq...")

df2 = pd.read_gbq(query)
print(df2)

print("Performing a reading query with BigQuery client...")
client = bigquery.Client(credentials=credentials, project=credentials.project_id,)

model_details_df = client.query(query).result().to_dataframe(create_bqstorage_client=True,)

print(model_details_df)