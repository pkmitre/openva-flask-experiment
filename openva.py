# Simple example interface demonstrating a SOA approach that may be useful for openVA

import sys
from io import StringIO
from collections import OrderedDict
from flask import Flask, render_template, request
import requests
import csv
import json

app = Flask(__name__)

# Index just displays a file upload dialog
@app.route('/')
def index():
  return render_template("index.html")

# Process the uploaded file, displaying the intermediate steps and final result
@app.route('/upload', methods=['POST'])
def upload():

  # Grab the uploaded CSV
  csv_data = request.files['file'].read()

  # Transform to algorithm format using the pyCrossVA web service
  transform_url = 'http://127.0.0.1:5001/transform?input=2016WHOv151&output=InterVA5'
  transform_response = requests.post(transform_url, data=csv_data)

  # We need to convert the CSV to JSON
  transform_response_reader = csv.DictReader(StringIO(transform_response.text))
  algorithm_input_rows = []
  for row in transform_response_reader:
    # Replace blank key with ID and append to list for later jsonification
    algorithm_input_rows.append(OrderedDict([('ID', v) if k == '' else (k, v) for k, v in row.items()]))
  algorithm_input_json = json.dumps({ 'Input': algorithm_input_rows, 'HIV': 'l', 'Malaria': 'l' })
  # Note: Temporary hack to get to the required algorithm format
  algorithm_input_json = algorithm_input_json.replace('"0.0"', '"."').replace('"1.0"', '"y"')

  # Send to InterVA algorithm web service
  algorithm_url = 'http://127.0.0.1:5002/interva5'
  algorithm_response = requests.post(algorithm_url, data=algorithm_input_json)

  # Display results
  return render_template("upload.html", csv_data=csv_data.decode('utf-8'), transform_response=transform_response.text,
                         algorithm_input=algorithm_input_json, algorithm_response=algorithm_response.text)
