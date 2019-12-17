# to collect environmental data from Raspberry Pi

from sense_hat import SenseHat 
from datetime import datetime
from csv import writer
import time
import csv


sense = SenseHat()
delay = 60

def get_sense_data():
    sense_data = []

    sense_data.append(sense.get_temperature())
    sense_data.append(sense.get_humidity())
    sense_data. append(datetime.now().isoformat())

    return sense_data

with open('data.csv', 'w', newline='') as f:
    data_writer = writer(f)

    data_writer.writerow(['temperature', 'humidity', 'timestamp'])

    while True:
        data = get_sense_data()
        data_writer.writerow(data)
        time.sleep(delay)


##sample data written from this script that we collected from the GRA space is in pi-data.csv
