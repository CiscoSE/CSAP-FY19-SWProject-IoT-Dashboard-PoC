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

import sqlite3
import datetime

def init():
    conn = sqlite3.connect('sensor.sqlite3')
    create_table(conn)
    conn.close()


def create_table(conn):
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS answers (takenat TIMESTAMP, temperature INTEGER, humidity INTEGER)''')
    conn.commit()

def add_new(temperature, humidity):
    conn = sqlite3.connect('sensor.sqlite3')
    now = datetime.datetime.now().ctime()
    c = conn.cursor()
    c.execute('''INSERT INTO answers (takenat, temperature,humidity ) VALUES (?,?,?)''', (now[8:16],temperature,humidity))
    conn.commit()

def read_table():
    conn = sqlite3.connect('sensor.sqlite3')
    c = conn.cursor()
    c.execute(''' SELECT * FROM answers ''')
    rows = c.fetchall()

    for row in rows:
        print(row)


def read_line():
    conn = sqlite3.connect('sensor.sqlite3')
    c = conn.cursor()
    c.execute(''' SELECT * FROM answers ''')
    rows = c.fetchone()

def delete_table():
    conn = sqlite3.connect('sensor.sqlite3')
    c = conn.cursor()
    c.execute('''DROP TABLE answers''')
    conn.commit()

    
