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
            timestamp = datetime.strptime(row['Date / Time'], "%m/%d/%Y %H:%M:%S")
            temperature = float(row['Temperature C']) 
            humidity = float(row['Humidity'])
            datapoint = {"timestamp": timestamp,
                         "temperature": temperature,
                         "humidity": humidity}
            datapoints.append(datapoint)

    return datapoints