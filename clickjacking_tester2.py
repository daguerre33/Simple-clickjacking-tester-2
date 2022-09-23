#!/usr/bin/python3

from requests_html import HTMLSession

session = HTMLSession()
url = input("Url (eg. http://www.example.com): ")
response = session.get(url)
content = response.headers
if content.__contains__("X-Frame-Options"):
        print("iframe is not possible")
else:
        print("iframing is possible!")



