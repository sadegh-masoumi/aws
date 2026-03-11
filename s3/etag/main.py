#!/usr/bin/env python3
import argparse
import boto3
from botocore.exceptions import ClientError

BUCKET = "aws-buckt-test-skcjdv"
s3 = boto3.client("s3")


def put_object(key, file_path):
    with open(file_path, "rb") as f:
        response = s3.put_object(Bucket=BUCKET, Key=key, Body=f)
    etag = response["ETag"].strip('"')
    print(f"Uploaded: {key}")
    print(f"ETag:     {etag}")


def get_object(key, output_path):
    response = s3.get_object(Bucket=BUCKET, Key=key)
    data = response["Body"].read()
    etag = response["ETag"].strip('"')
    with open(output_path, "wb") as f:
        f.write(data)
    print(f"Downloaded: {key} -> {output_path}")
    print(f"ETag:       {etag}")


def get_etag(key):
    response = s3.head_object(Bucket=BUCKET, Key=key)
    etag = response["ETag"].strip('"')
    print(f"Object: {key}")
    print(f"ETag:   {etag}")


def main():
    parser = argparse.ArgumentParser(description="S3 CLI for aws-buckt-test-skcjdv")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # put
    put_parser = subparsers.add_parser("put", help="Upload a file to the bucket")
    put_parser.add_argument("key", help="S3 object key (e.g. folder/file.txt)")
    put_parser.add_argument("file", help="Local file path to upload")

    # get
    get_parser = subparsers.add_parser("get", help="Download a file from the bucket")
    get_parser.add_argument("key", help="S3 object key")
    get_parser.add_argument("output", help="Local path to save the file")

    # etag
    etag_parser = subparsers.add_parser("etag", help="Get ETag of an object")
    etag_parser.add_argument("key", help="S3 object key")

    args = parser.parse_args()

    try:
        if args.command == "put":
            put_object(args.key, args.file)
        elif args.command == "get":
            get_object(args.key, args.output)
        elif args.command == "etag":
            get_etag(args.key)
    except ClientError as e:
        print(f"Error: {e.response['Error']['Message']}")
    except FileNotFoundError as e:
        print(f"File not found: {e}")


if __name__ == "__main__":
    main()