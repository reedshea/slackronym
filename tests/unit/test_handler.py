import json
from urllib.parse import parse_qs

import pytest

from slackronym import app


@pytest.fixture()
def apigw_event():
    """ Generates Event"""

    return {
        "version": "2.0",
        "routeKey": "$default",
        "rawPath": "/",
        "rawQueryString": "",
        "headers": {
            "content-length": "419",
            "x-amzn-tls-version": "TLSv1.3",
            "x-forwarded-proto": "https",
            "x-forwarded-port": "443",
            "x-forwarded-for": "127.0.0.1, 127.0.0.2",
            "accept": "application/json, text/plain, */*",
            "x-amzn-tls-cipher-suite": "TLS_AES_128_GCM_SHA256",
            "host": "1234567890.execute-api.us-east-1.amazonaws.com",
            "content-type": "application/x-www-form-urlencoded",
            "accept-encoding": "gzip, compress, deflate, br",
            "user-agent": "axios/1.6.8"
        },
        "requestContext": {
            "accountId": "anonymous",
            "apiId": "1234567890",
            "domainName": "1234567890.execute-api.us-east-1.amazonaws.com",
            "domainPrefix": "1234567890",
            "http": {
                "method": "POST",
                "path": "/",
                "protocol": "HTTP/1.1",
                "sourceIp": "127.0.0.1",
                "userAgent": "axios/1.6.8"
            },
            "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
            "routeKey": "$default",
            "stage": "$default"
        },
        "body": "dG9rZW49MTIzNDU2Nzg5MHRva2VuJnRlYW1faWQ9dGVhbTEyMyZ0ZWFtX2RvbWFpbj1kZXZlbG9wbWVudCZjaGFubmVsX2lkPWNoYW5uZWwxMjMmY2hhbm5lbF9uYW1lPWNoYW5uZWxfbmFtZTEyMyZ1c2VyX2lkPXVzZXJfaWQxMjMmdXNlcl9uYW1lPXVzZXJuYW1lMTIzJmNvbW1hbmQ9JTJGZXhwbGFpbiZ0ZXh0PWkxOG4mYXBpX2FwcF9pZD1hcHBfaWQxMjMmaXNfZW50ZXJwcmlzZV9pbnN0YWxsPWZhbHNlJnJlc3BvbnNlX3VybD1odHRwcyUzQSUyRiUyRmhvb2tzLnNsYWNrLmNvbSUyRmNvbW1hbmRzJTJGcmVzcG9uc2VfdXJsMTIzJnRyaWdnZXJfaWQ9dHJpZ2dlcl9pZDEyMw==",
        "isBase64Encoded": True
        }

def test_lambda_handler(apigw_event):

    ret = app.lambda_handler(apigw_event, "")

    post_data = base64.b64decode(apigw_event['body']).decode()
    parsed_data = parse_qs(post_data)    
    
    assert ret["statusCode"] == 200
    assert "command" in parsed_data
    assert parsed_data["command"] == ["/explain"]
