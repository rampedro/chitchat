#!/usr/bin/python3
import os
import aiml

BRAIN_FILE="brain.dump"

k = aiml.Kernel()

# To increase the startup speed of the bot it is
# possible to save the parsed aiml files as a
# dump. This code checks if a dump exists and
# otherwise loads the aiml from the xml files
# and saves the brain dump.

if os.path.exists(BRAIN_FILE):
    print("Loading from brain file: " + BRAIN_FILE)
    k.loadBrain(BRAIN_FILE)
else:
    print("Parsing aiml files")
    k.bootstrap(learnFiles="std-startup.aiml", commands="load aiml b")
    print("Saving brain file: " + BRAIN_FILE)
    k.saveBrain(BRAIN_FILE)



import os
from flask import jsonify,Flask, render_template, request, redirect, url_for, abort
from werkzeug.utils import secure_filename
import requests
import urllib.request

app = Flask(__name__)








@app.route('/',methods=['GET'])
def index():
    
    while True:
        input_text = request.args.get('text') 
        response = k.respond(input_text)
        #print(response)
        
    
    
        return jsonify({"chitchat":response})



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=4500, debug=True)
