import boto3


class S3Store:
    
    def __init__(self, Region_name, AWS_access_key_id, AWS_secret_access_key,  Bucket):
        self.AWS_access_key_id = AWS_access_key_id
        self.AWS_secret_access_key = AWS_secret_access_key
        self.Region_name = Region_name
        self.Bucket = Bucket
        self.client = boto3.client(
            "s3",
            region_name=Region_name,
            aws_access_key_id=AWS_access_key_id,
            aws_secret_access_key=AWS_secret_access_key,
        )

    def uploading_files(self, filename, key_name):
        return self.client.upload_file(filename, self.Bucket, key_name)

    def downloading_files(self, keyname, onstoragename):
        return self.client.download_file(self.Bucket, keyname, onstoragename)

    def deleting_files(self, keyname):
        return self.client.delete_object(Bucket=self.Bucket, Key=keyname)



