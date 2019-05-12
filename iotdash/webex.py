'''
Copyright (c) 2019 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
'''

import requests

#note tokens and room-ID have been removed and should be replaced with desired values
def webex_alert(message):

    url = "https://api.ciscospark.com/v1/messages"

    payload = "{\n  \"roomId\": \"[ROOM-ID-HERE]\",\n  \"markdown\": \"%s\"\n}\n" % (message)
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer [TOKEN HERE]",
        'cache-control': "no-cache",
        'Postman-Token': "[POSTMAN-TOKEN-HERE]"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)
