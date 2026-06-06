import paho.mqtt.client as mqtt
import random
import time

BROKER = "localhost"
TOPIC_TEMP = "factory/machine1/temp"
TOPIC_VIB = "factory/machine1/vibration"

client = mqtt.Client()
client.connect(BROKER, 1883, 60)

while True:
    temp = round(random.uniform(25, 90), 2)
    vib = round(random.uniform(0.1, 6.0), 2)

    client.publish(TOPIC_TEMP, temp)
    client.publish(TOPIC_VIB, vib)

    print(f"Temp: {temp} | Vib: {vib}")
    time.sleep(2)
