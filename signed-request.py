import boto3
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
import requests

session = boto3.Session()
credentials = session.get_credentials()
creds = credentials.get_frozen_credentials()

def signed_request(method, url, data=None, params=None, headers=None):
    request = AWSRequest(method=method, url=url, data=data, params=params, headers=headers)
    # "service_name" is generally "execute-api" for signing API Gateway requests
    SigV4Auth(creds, "service_name", REGION).add_auth(request)
    return requests.request(method=method, url=url, headers=dict(request.headers), data=data)

def main():
    url = f"my.url.example.com/path"
    data = {"environmentId": self._environment_id}
    headers = {'Content-Type': 'application/x-amz-json-1.1'}
    response = signed_request(method='POST', url=url, data=data, headers=headers)

if __name__ == "__main__":
    main()
