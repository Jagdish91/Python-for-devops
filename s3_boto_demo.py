import boto3
import os

# ----------- S3 Client Setup -----------
s3_client = boto3.client('s3', region_name='us-west-2')
bucket_name = 'boto-demo-temp-s3learning-opertions123432'

# ----------- 1. Create Bucket (only once) -----------

s3_client.create_bucket(
     Bucket=bucket_name,
     CreateBucketConfiguration={'LocationConstraint': 'us-west-2'}
 )

# ----------- 2. List all Buckets -----------
buckets = s3_client.list_buckets()
for b in buckets:
    print(b['Name'])

# ----------- 3. Upload a File -----------
file_name = 'test_file.txt'
with open(file_name, 'w') as f:
    f.write("Hello AWS S3! This is a test file using Boto3.")

s3_client.upload_file(file_name, bucket_name, file_name)
print(f"Uploaded '{file_name}' to bucket '{bucket_name}'")

# ----------- 4. List Objects in Bucket -----------
objects = s3_client.list_objects_v2(Bucket=bucket_name)
if 'Contents' in objects:
    print("Objects in bucket:")
    for obj in objects['Contents']:
        print(" -", obj['Key'])
else:
    print("Bucket is empty")


# ----------- 6. Get Bucket ACL -----------
acl = s3_client.get_bucket_acl(Bucket=bucket_name)
print("Bucket ACL:", acl)

 ----------- 7. Delete Object (cleanup) -----------

s3_client.delete_object(Bucket=bucket_name, Key=file_name)
print(f"Deleted '{file_name}' from bucket '{bucket_name}'")

# ----------- 8. Delete Bucket (cleanup) -----------

s3_client.delete_bucket(Bucket=bucket_name)
print(f"Deleted bucket '{bucket_name}'")

# ----------- Cleanup Local Files -----------
os.remove(file_name)
os.remove(download_path)
