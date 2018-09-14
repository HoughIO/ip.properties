from flask import Flask
from flask import jsonify, request
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_my_ip():
    return jsonify({'ip': request.remote_addr}), 200
