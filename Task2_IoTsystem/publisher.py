import paho.mqtt.client as mqttClient
import time

def on_connect(client, userdata, flags, rc):
    if rc == 0:

        print("Connected to broker")

        global Connected  # Use global variable
        Connected = True  # Signal connection

    else:

        print("Connection failed")


Connected = False  # global variable for the state of the connection

broker_address = "172.20.0.3"
port = 1883

client = mqttClient.Client("Python")  # create new instance
client.on_connect = on_connect  # attach function to callback
client.connect(broker_address, port=port)  # connect to broker

client.loop_start()  # start the loop

while Connected != True:  # Wait for connection
    time.sleep(0.1)

def temperature_change(value, flag):
    if flag == 1:
        value +=1
    else:
        value -=1
    if value%10 == 0:
        flag *= -1
    return (value, flag)

try:
    flag = 1
    value = 0
    while True:
        value, flag = temperature_change(value, flag)
        temp = "temperature,site=room value=" + str(value)
        print(temp)
        client.publish("sensors", temp)
        time.sleep(2)

except KeyboardInterrupt:

    client.disconnect()
    client.loop_stop()
