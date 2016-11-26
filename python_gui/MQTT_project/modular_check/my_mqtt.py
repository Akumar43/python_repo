import paho.mqtt.client as mqtt
import time

from appli import *
message="hello"
mqttc = mqtt.Client()

global MQ_topic,MQ_username,MQ_password,MQ_servername,MQ_port,MQ_client

MQ_topic='/test/topic'
MQ_username="fcfvaydb"
MQ_password="MmIWxonlCM7u"
MQ_servername="m12.cloudmqtt.com"
MQ_port=11523
MQ_client=60

def update(server_name,Username,Password,Port,topic,client_id):
    MQ_topic=topic
    MQ_username=Username
    MQ_password=Password
    MQ_servername=server_name
    MQ_port=Port
    MQ_client=client_id
    print "server_name " + MQ_servername + " \nUsername " + MQ_username + " \nPassword " + MQ_password + "\nPort " +MQ_port
    print "\ntopic " + MQ_topic + "\nclient_id " + MQ_client


    

def on_connect(mosq, obj, rc):
    mqttc.subscribe(MQ_topic, 0)
    print("rc: " + str(rc))
    print "hello connect"

def on_message(mosq, obj, msg):
    global message
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    message = msg.payload
    print "hello msg"
    

def on_publish(mosq, obj, mid):
    print("mid: arya" + str(mid))
    print "hello pub"

def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))
    print "hello sub"

def est_connect():
    global mqttc
    
    # Assign event callbacks
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
    mqttc.on_publish = on_publish
    mqttc.on_subscribe = on_subscribe

    # Connect

    mqttc.username_pw_set(MQ_username, password=MQ_password)
    mqttc.connect(MQ_servername,MQ_port,MQ_client)
    mqttc.publish("/test/topic","connection estd")
    print "topic published"


def tx(a):
    mqttc.publish("/test/topic","b")
    print "topic published"
    
est_connect()
while True:
    print("staying alive")
    time.sleep(1)
    
