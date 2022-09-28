import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

mqttBroker = "192.168.178.46"
port = 8883
topic = "sniplite"
client = mqtt.Client("SnipLiteSender")
client.connect(mqttBroker, port)

while True:
    randNumber = uniform(20.0, 21.0)
    client.publish(topic, randNumber)
    print("Just published " + str(randNumber) + " to topic " + topic)
    time.sleep(1)
