from flask import make_response,Flask, flash, redirect, render_template, request, url_for, session
from app import *
import utils.bot

# Main Page
@app.route('/')
def home():
    return render_template('index.html')

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(utils.bot.get_response(userText))