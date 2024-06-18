import boto3

BUCKET_NAME = "cloud-course-bucket-noor"

session = boto3.Session()

s3_client = session.client("s3")

s3_client.put_object(Bucket=BUCKET_NAME, Key="folder/hello.txt", Body="Hello, World!", ContentType="text/plain")
