import json
import requests

from flask import Blueprint, request, jsonify

from http_service.model import party as db

party = Blueprint("party", __name__)


@party.route("", methods=["GET"])
def hello():
    return "General Kenobi, Hello, there! (WTF)"


@party.route("/store", methods=["POST"])
def store():
    args = request.get_json()
    db.storeData(args)
    return "ok"

@party.route("/latest", methods=["GET"])
def latest():
    args = request.args
    limit = int(args.get("limit", 10))
    res = db.getLatest(limit)
    return jsonify(res), 200

@party.route("/last", methods=["GET"])
def last():
    res = db.getLast()
    return jsonify(res), 200