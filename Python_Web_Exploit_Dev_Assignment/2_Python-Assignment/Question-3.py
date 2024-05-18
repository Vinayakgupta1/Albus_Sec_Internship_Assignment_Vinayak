# Q.3 Write a program to automate Sending HTTP Request to web server.

import requests

def send_http_request(url):
    response = requests.get(url)
    if response.status_code == 200:
        print("Request successful!")
        print("Response:")
        print(response.text)
    else:
        print("Request failed with status code:", response.status_code)

url = input("Enter the URL:- ")
send_http_request(url)