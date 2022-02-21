import pandas as pd
import pyarrow
import openpyxl
import xlsxwriter
import fsspec
import gcsfs
import io
from datetime import datetime, date
from google.cloud import storage
from google.cloud import bigquery
import time
from datetime import datetime, date

#PROJECT VARIABLES
def readfile(file_path):
  client = storage.Client()
  bucket = client.bucket("key-cash")
  blob = bucket.blob(file_path)
  return blob.download_as_bytes()

#CREATING DATA INGESTION FUNCTION AND INSERTING SCHEMA
def loadbq(df, event):
  client = bigquery.Client()
  table_id = "curso-data-flow.cashchallenge.LANDING_TABLE"
  job_config = bigquery.LoadJobConfig(
  write_disposition='WRITE_APPEND',
  schema=[
  bigquery.SchemaField("id","STRING"),
  bigquery.SchemaField("name","STRING"),
  bigquery.SchemaField("idade","INTEGER"),
  bigquery.SchemaField("credito_solicitado","INTEGER"),
  bigquery.SchemaField("data_solicitacao","STRING"),
  ],
  )
  load_job = client.load_table_from_dataframe(
  df, table_id, job_config=job_config
  )
  load_job.result()
  destination_table = client.get_table(table_id)
  print("Carregado {} linhas.".format(destination_table.num_rows))

#WRITING TO BQ
def hello_gcs(event, context):
  content = readfile(event["name"])
  json = pd.read_json(content)
  df_json = pd.json_normalize(data=json['clientes'])
  loadbq(df_json,event)
