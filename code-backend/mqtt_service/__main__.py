import json
from pprint import pprint

import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish


from lib import config

CONF = config.loadConfig("config/config.yaml").get("mqtt")

HOST = None
CNANNEL = None
PORT = None
MAC_ADDR = None


def init():
    global HOST, CNANNEL, PORT, MAC_ADDR
    HOST = CONF.get("host")
    CNANNEL = CONF.get("channel")
    PORT = CONF.get("port")
    MAC_ADDR = CONF.get("device-mac")


def connected(c, d, f, r):
    global CNANNEL
    print("Connected!")
    c.subscribe(CNANNEL)


def rcv(c, d, m):
    global CNANNEL, MAC_ADDR
    print(f"Recieved {str(m.payload, encoding='utf-8')}")
    c.subscribe(CNANNEL)


def run():
    global HOST, PORT
    client = mqtt.Client()

    client.on_connect = connected
    client.on_message = rcv

    client.connect(HOST, PORT, 60)
    client.loop_forever()


if __name__ == "__main__":
    init()
    run()
