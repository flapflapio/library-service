#!/usr/bin/env python3s
from library_service.dataaccess.object.s3_object_store import S3Store
# import uvicorn

AWS_access_key_id = "AKIASUY3B4L3Q7QQFB7W"
AWS_secret_access_key = "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"
Region_name = "ca-central-1"
Bucket = 'sometesting'


# Runs the app in development mode
def main() -> None:
    # uvicorn.run("library_service.main:app", host="localhost", port=8080, reload=True)

    s3Store = S3Store(Region_name, AWS_access_key_id, AWS_secret_access_key, Bucket)

    response = s3Store.uploading_files("sample.json", "ethan1.json")
    print(response)

    response = s3Store.downloading_files("ethan1.json", "ondrive.json")
    print(response)

    response = s3Store.deleting_files("ethan1.json")
    print(response)


if __name__ == "__main__":
    main()
