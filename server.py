#!/usr/bin/env python

from flask import Flask, send_file, send_from_directory
from dotenv import find_dotenv, load_dotenv
from os import environ

load_dotenv(find_dotenv())
app = Flask(__name__)

HOST = str(environ.get("HOST"))
PORT = int(environ.get("PORT"))

@app.route("/")
def _():
  return send_file("./index.html")

@app.route("/index")
def index():
  return send_file("./index.html")

@app.route("/index.html")
def index_html():
  return send_file("./index.html")

@app.route("/favicon.ico")
def favicon_ico():
  return send_file("./favicon.ico")

@app.route("/style.css")
def style_css():
  return send_file("./style.css")

@app.route("/fonts.css")
def font_css():
  return send_file("./fonts.css")

@app.route("/script.js")
def script_js():
  return send_file("./script.js")

@app.route("/particle.js")
def particle_js():
  return send_file("./particle.js")

@app.route("/assets/<path:path>")
def assets(path):
  return send_from_directory("assets", path)

@app.route("/font/<path:path>")
def font(path):
  return send_from_directory("font", path)

if __name__ == "__main__":
  app.run(
    port=PORT,
    host=HOST,
    debug=False
  )