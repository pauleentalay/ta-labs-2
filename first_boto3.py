import boto3
from datetime import datetime

s3 = boto3.client('s3')
response = s3.list_buckets()
print(f'Metadata: {response["ResponseMetadata"]["RequestId"]}')
# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(datetime.strftime(bucket["CreationDate"],"%Y-%m-%d %H:%M:%S"), bucket["Name"])


