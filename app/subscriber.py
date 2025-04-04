
import paho.mqtt.client as mqtt

import psycopg2

import struct
import numpy as np
from numpy.random import default_rng
import flatbuffers
# from flatc-generated files
import TSData
import FuelCellMode

import sys
import time as tm
#import amqp
import os


print(os.getenv("BROKER_ADDRESS"))
print(os.getenv("BROKER_PORT"))
print(os.getenv("BROKER_USERNAME"))
print(os.getenv("BROKER_PASSWORD"))
print(os.getenv("DB_DATABASE"))
print(os.getenv("DB_USER"))
print(os.getenv("DB_PASSWORD"))
print(os.getenv("DB_HOST"))
print(os.getenv("DB_PORT"))



# Define the MQTT broker parameters
broker_address = os.getenv("BROKER_ADDRESS")
broker_port  = os.getenv("BROKER_PORT")
username = os.getenv("BROKER_USERNAME")
password = os.getenv("BROKER_PASSWORD")
# conn_address = str(broker_address)+":"+str(broker_port)


topic = "/sensors"

try:
    conn = psycopg2.connect(
        dbname=os.getenv("DB_DATABASE"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )
    cursor = conn.cursor()


# Define the callback function to handle incoming messages
    def on_message(client, userdata, msg):
        print('Received message')
        buf = bytearray(msg.payload)
        tsdata = TSData.TSData.GetRootAs(buf,0)
        print(tsdata.FcVoltage())
    # Wstawianie danych
        cursor.execute("INSERT INTO measurements (time, vehicle_type, fc_voltage, fc_current, fc_temperature, sc_motor_voltage, sc_current, motor_current, motor_speed, motor_pwm, vehicle_speed, h2_pressure, h2_leak_level, fan_rpm, gps_latitude, gps_longitude, gps_altitude, gps_speed, lap_number) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(tm.time(),'0',tsdata.FcVoltage(),tsdata.FcCurrent(),tsdata.FuelCellTemperature(),tsdata.ScVoltage(),tsdata.FcScCurrent(),tsdata.MotorCurrent(),tsdata.MotorSpeed(),tsdata.MotorPwm(),tsdata.VehicleSpeed(),tsdata.HydrogenPressure(),'2',tsdata.FanRpm(),tsdata.GpsLatitude(),tsdata.GpsLongitude(),tsdata.GpsAltitude(),tsdata.GpsSpeed(),tsdata.LapNumber()))
        conn.commit()
        print("Dane zostały wprowadzone!")


#    with amqp.Connection(conn_address) as c:
#        ch = c.channel()
#        ch.basic_consume(queue='test', callback=on_message, no_ack=True)
#        while True:
#            c.drain_events()

    # Create an MQTT client
    new_client = mqtt.Client()

    # Set the username and password for authentication
    new_client.username_pw_set(username=username, password=password)
    
    # Connect to the broker
    new_client.connect(host=broker_address, port=int(broker_port))

    # Subscribe to the topic
    new_client.subscribe((topic, 0))

    # Define the callback function to handle incoming messages
    new_client.on_message = on_message

    # Start the loop to receive messages
    new_client.loop_forever()


except Exception as e:
    print("Błąd:", e)
finally:
    cursor.close()
    conn.close()
    new_client.disconnect()
