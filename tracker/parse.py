import csv
from datetime import datetime


def parse_datafile(filepath, sensor_type):
    """This reads in a data file and picks the right parser based on the sensor type"""
    if (sensor_type == "Raspberry Pi"):
        return parse_pi_csv(filepath)
    else:
        pass

def parse_pi_csv(filepath):
    datapoints = []
    with open(filepath) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            temperature = float(row['temperature']) 
            humidity = float(row['humidity'])
            timestamp = datetime.strptime(row['timestamp'], "%m/%d/%Y %H:%M:%S")            
            datapoint = {"temperature": temperature,
                         "humidity": humidity,
                         "timestamp": timestamp}
            datapoints.append(datapoint)

    return datapoints
