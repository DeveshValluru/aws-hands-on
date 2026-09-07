import boto3

#establist connection
s3 = boto3.client("s3")

response = s3.list_buckets()

for bucket in response["Buckets"]:
    print(bucket["Name"])

BUCKET = "devesh-s3-lab-1234"

#upload file

s3.upload_file("../hello.txt", BUCKET, "from-python.txt")
print("uploaded hello.txt as key 'from-python.txt'")


response = s3.list_objects_v2(Bucket=BUCKET)

print("\n Objects in bucket:")

for obj in response["Contents"]:
    print(f"{obj['Key']} ({obj['Size']} bytes)")


#download file from s3 to local

#way1
s3.download_file(BUCKET, "from-python.txt", "downloaded-by-python.txt")
print("\n Downloaded to downloaded-by-python.txt")

#way2
response = s3.get_object(Bucket=BUCKET, Key="from-python.txt")
data = response["Body"].read()
print("Object content in memory:", data)
print("Type of data:", type(data))

#Deleting the object

response = s3.list_objects_v2(Bucket=BUCKET)

for obj in response.get("Contents", []):
    s3.delete_object(Bucket=BUCKET, Key=obj["Key"])
    print(f"Deleted object: {obj['Key']}")

#now empty bucket can be removed

s3.delete_bucket(Bucket=BUCKET)
print(f"Deleted bucket: {BUCKET}")
