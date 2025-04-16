# https://docs.aws.amazon.com/general/latest/gr/create-signed-request.html

import requests
import os
import datetime
import hmac
import hashlib
import urllib.parse
# 
# 
# 
def sort_dict(dict_in):
    dict_out = dict()

    keys = list(dict_in.keys())
    keys.sort()
    
    for key in keys:
        dict_out[key] = dict_in[key]

    return dict_out
# 
# 
# 
def make_request(method:str, service:str, action:str, params:dict = dict()):
    authentication_in_query_string = False

    data = dict()

    headers = dict()

    access_key_ID = os.getenv("AWS_KEY_ID")
    # print(access_ke<y_ID)

    access_key_secret = os.getenv("AWS_KEY_SECRET")
    # print(access_key_secret)

    now = datetime.datetime.now()
    x_amz_date = now.strftime("%Y%m%dT%H%M%SZ")
    date = now.strftime("%Y%m%d")

    algorithm = "AWS4-HMAC-SHA256"

    content_type = "application/x-www-form-urlencoded; charset=utf-8"
    # content_type = "application/json; charset=utf-8"

    region = "eu-west-2"

    credential = "{}/{}/{}/{}/aws4_request".format(access_key_ID, date, region, service)
    # print(credential)

    credential_scope = "{}/{}/{}/aws4_request".format(date, region, service)
    # print(credential_scope)

    host = "{}.{}.amazonaws.com".format(service, region)

    # lowercase characters and must appear in alphabetical order
    headers = {
        "Host": host,
        "X-Amz-Date": x_amz_date,
        "Content-Type": content_type,
    }
    headers = sort_dict(headers)
    # print(headers)

    canonical_headers = "".join(key.strip().lower() + ":" + value.strip() + "\n" for key, value in headers.items())
    # print(canonical_headers)

    # separated by semicolons (;) lowercase characters and must appear in alphabetical order
    signed_headers = "".join(key.strip().lower() + ";" for key in headers.keys())
    signed_headers = signed_headers[:-1]
    # print(signed_headers)

    #  If the absolute path is empty, use a forward slash character (/)
    canonical_uri = "/"
    # print(canonical_uri)

    params["Action"] = action
    params["Version"] = "2012-11-05"

    if method == "POST":
        data = params
        params = dict()

    if authentication_in_query_string:
        params["X-Amz-Algorithm"] = algorithm
        params["X-Amz-Credential"] = credential
        params["X-Amz-Date"] = x_amz_date
        params["X-Amz-SignedHeaders"] = signed_headers

    params = sort_dict(params)
    # print(params)

    # canonical_query_string = "".join(key + "=" + value + "&" for key, value in params.items())
    # canonical_query_string = canonical_query_string[:-1]
    canonical_query_string = urllib.parse.urlencode(params)
    # print(canonical_query_string)

    payload = ""

    hashed_payload = hashlib.sha256(payload.encode()).hexdigest()
    # print(hashed_payload)

    canonical_request = "{}\n{}\n{}\n{}\n{}\n{}".format(method, canonical_uri, canonical_query_string, canonical_headers, signed_headers, hashed_payload)
    print(canonical_request)
    print()

    hashed_canonical_request = hashlib.sha256(canonical_request.encode()).hexdigest()
    # print(hashed_canonical_request)

    string_to_sign = "{}\n{}\n{}\n{}".format(algorithm, x_amz_date, credential_scope, hashed_canonical_request)
    print(string_to_sign)
    print()

    kDate = hmac.new("AWS4".encode() + access_key_secret.encode(), date.encode(), hashlib.sha256).hexdigest()

    kRegion = hmac.new(kDate.encode(), region.encode(), hashlib.sha256).hexdigest()

    kService = hmac.new(kRegion.encode(), service.encode(), hashlib.sha256).hexdigest()

    kSigning = hmac.new(kService.encode(), "aws4_request".encode(), hashlib.sha256).hexdigest()

    signature = hmac.new(kSigning.encode(), string_to_sign.encode(), hashlib.sha256).hexdigest()
    print(signature)
    print()

    url = "https://{}".format(host)

    if authentication_in_query_string:
        params["X-Amz-Signature"] = signature
        # params["X-Amz-Security-Token"] = X_Amz_Security_Token
    
    else:
        authorization = "{} Credential={}, SignedHeaders={}, Signature={}".format(algorithm, credential, signed_headers, signature)
        # print(authorization)
        
        headers["Authorization"] = authorization

    if method == "POST":
        params = dict()

    req = requests.request(method, url, headers=headers, params=params, data=data, proxies=proxies, verify=False)

    print(req.status_code)
    print(req.text)
# 
# 
# 
def sqs_list_queues():
    method = "GET"

    service = "sqs"

    action = "ListQueues"

    make_request(method, service, action)
# 
# 
# 
def sqs_send_message():
    method = "GET"

    service = "sqs"

    action = "SendMessage"

    params = {
        "MessageBody": "This+is+a+test+message"
    }

    make_request(method, service, action, params)
# 
# 
# 
if __name__ == "__main__":
    proxies = dict()

    # proxies = {
    #     "https": "http://127.0.0.1:8080",
    #     "http": "http://127.0.0.1:8080",
    #     "socks": "socks5://127.0.0.1:8080",
    # }

    sqs_list_queues()
# 
# 
# 