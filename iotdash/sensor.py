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

from sense_hat import SenseHat #import SenseHat packages
import database
import webex

sense = SenseHat()  #establish connection to hat

# Set threshold for temperature to alert admin
temp_threshold = 80

# Get temperature
temp = sense.get_temperature()
tempF = temp *(9/5) + 32
intTempF = int(tempF) - 40
# Subtracting 40 accounts for the processor running hot on the Pi
# print("Temperature in F = " +str(intTempF))



# Get pressure and print to console
# pressure = sense.get_pressure()
# print("Pressure = " +str(pressure))


# Get humidity
humidity = sense.get_humidity()
intHumidity = int(humidity)
# print("Humidity = " +str(intHumidity))

# Connect to table
database.init()

# Add values to database
database.add_new(intTempF, intHumidity)

# Read table for debug purposes
database.read_table()


# Check temperature and alert the user
if (intTempF > temp_threshold): 
    webex.webex_alert("Temperature on Solar Panel 1 is %s degrees F" % (str(intTempF)))


