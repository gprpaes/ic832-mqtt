import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado...")
    else: 
        print("Erro: " +str(rc))

def on_message(client, userdata, msg):
    print("Messagem recebida....\nTópico: "+ msg.topic +"\nMensagem: "+msg.payload.decode("utf-8"))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)

client.username_pw_set("publisher", "jp38F@D^zrandKBty")

client.connect("0e9e9d61e3b24bc6960fd0bfd6b4c1f6.s1.eu.hivemq.cloud", 8883)

msgs = ["Embarcados", "Rural", "UFRRJ", "Raspberry Pi", "Linux"]

for msg in msgs:
    print("Publicando no broker...")
    client.publish("UFRRJ/SI/SO Linux", msg)
    time.sleep(2)


client.loop_forever()
