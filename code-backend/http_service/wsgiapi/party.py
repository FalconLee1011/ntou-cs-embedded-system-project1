import requests
from flask import Blueprint, request, jsonify

party = Blueprint("party", __name__)


@party.route("", methods=["GET"])
def hello():
    return "General Kenobi, Hello, there! (WTF)"
