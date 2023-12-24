from google.cloud import storage
import pandas

df = pandas.DataFrame([{'Name': 'A', 'Id': 100}, {'Name': 'B', 'Id': 110}])
df.head()


bucket_name = 'karan-test-bucket'
file_path = 'karan-test-bucket/test.csv'

# 1st method to store data from pandas to cloud storage bucket 

client = storage.Client()
bucket = client.get_bucket(bucket_name)

blob = bucket.blob(file_path)
blob.upload_from_string(df.to_csv(index=False))

