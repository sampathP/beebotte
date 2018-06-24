import paho.mqtt.client as mqtt
import json

TOKEN = "[Beebotteのトークン]"
HOST = "mqtt.beebotte.com"
TOPIC = "[作成したチャンネル/リソース]"
CACERT = "mqtt.beebotte.com.pem"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

client = mqtt.Client()
client.username_pw_set("token:%s"%TOKEN)
client.on_connect = on_connect
client.on_message = on_message
client.tls_set(CACERT)
client.connect(HOST, port=8883, keepalive=60)
client.loop_forever()