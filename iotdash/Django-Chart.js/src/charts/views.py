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

from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response
import sqlite3

User = get_user_model()

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html', {"customers": 10})


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        conn = sqlite3.connect('[PATH-TO-SENSOR-DB]')
        def get_timestamp(conn):
            cursor = conn.execute("SELECT takenat FROM answers")
            return cursor

        def get_temp(conn):
            cursor = conn.execute("SELECT temperature FROM answers")
            return cursor

        def get_humid(conn):
            cursor = conn.execute("SELECT humidity FROM answers")
            return cursor


        time = get_timestamp(conn)
        temp = get_temp(conn)
        humid = get_humid(conn)
        data = {
                "labels": time,
                "default": temp,
                "humidity": humid,
        }
        return Response(data)

