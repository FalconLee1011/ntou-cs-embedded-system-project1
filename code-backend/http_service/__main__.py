from flask import Flask
from flask_cors import CORS

from lib import config
from lib.db import MongoSession
from .wsgiapi.register import registerService


CONF = None
app = Flask(__name__)
CORS(app)


def init():
    global CONF
    CONF = config.loadConfig(f"config/config.yaml").get("http")
    MongoSession.establish_connection(CONF.get("db"))
    app.debug = CONF.get("app", {}).get("debug", False)
    registerService(app)
    printRegister()


def printRegister():
    for p in app.url_map.iter_rules():
        print(p)


def main():
    global CONF
    init()
    app.run(host=CONF.get("app", {})["host"], port=CONF.get("app", {})["port"])


if __name__ == "__main__":
    main()
