#!/usr/bin/python3
#Python script that fetches https://alx-intranet.hbtn.io/status
 import urllib.request

 request = urllib.request.Request("https://alx-intranet.hbtn.io/status")

 with urllib.request.urlopen(request) as response:
     body = response.read()
     print("\t- type: {}".format(type(body)))
     print("\t- content: b{}".format(body))
     print("\t- utf8 content: {}".format(body.decode("utf-8")))
