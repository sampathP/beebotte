import paho.mqtt.client as mqtt
import json
import binascii
from bluepy.btle import Peripheral

TOKEN = "Beebotteのトークン"
HOST = "mqtt.beebotte.com"
TOPIC = "作成したチャンネル/リソース"
CACERT = "mqtt.beebotte.com.pem"
SWITCHBOT = "SwitchbotのMACアドレス"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    p = Peripheral(SWITCHBOT, "random")
    hand_service = p.getServiceByUUID("cba20d00-224d-11e6-9fb8-0002a5d5c51b")
    hand = hand_service.getCharacteristics("cba20002-224d-11e6-9fb8-0002a5d5c51b")[0]
    hand.write(binascii.a2b_hex("570100"))
    p.disconnect()

client = mqtt.Client()
client.username_pw_set("token:%s"%TOKEN)
client.on_connect = on_connect
client.on_message = on_message
client.tls_set(CACERT)
client.connect(HOST, port=8883, keepalive=60)
client.loop_forever()