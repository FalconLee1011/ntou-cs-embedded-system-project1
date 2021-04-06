import json
from datetime import datetime
from pprint import pprint

from requests import post

import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish


from lib import config

CONF = config.loadConfig("config/config.yaml").get("mqtt")

HOST = CONF.get("host")
CNANNEL = CONF.get("channel")
PORT = CONF.get("port")
MAC_ADDR = CONF.get("device-mac")
BASE_URL = CONF.get("http-server-base-url")


def connected(c, d, f, r):
    print("Connected!")
    c.subscribe(CNANNEL)


def rcv(c, d, m):
    now = datetime.now()
    payload = str(m.payload, encoding="utf-8")
    print(f"[{now}] Recieved {payload}")
    c.subscribe(CNANNEL)
    try:
        post(f"{BASE_URL}/store", json={"raw": payload, "timestamp": str(now)})
    except:
        print("Connection to http server could not be establish.")
        print("Upload failed.")


def mian():
    client = mqtt.Client()

    client.on_connect = connected
    client.on_message = rcv

    client.connect(HOST, PORT, 60)
    client.loop_forever()


if __name__ == "__main__":
    mian()
