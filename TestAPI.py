import json
import flask
from flask import request, jsonify
import sys

app = flask.Flask(__name__) # Create a flask object called app
app.config["DEBUG"] = True # Have an audit trail

# Create some test data for our catalog in the form of a list of dictionaries
file = open("resources/results.json", 'r')
json_data = json.load(file)

@app.route('/', methods=['GET']) # Decorator called route
def home():
    return '''<h1>Test Archive</h1>
    <p>An API for checking test results.</p>'''

@app.route('/api/v1/resources/tests/all', methods=['GET'])
def api_all():
    return jsonify(json_data)

# app.run()
# sys.exit(0)
@app.route('/api/v1/resources/tests', methods=['GET']) # /api/v1/resources/tests?TestNumber=4
def api_id():
    if 'TestNumber' in request.args:
        testNo = int(request.args['TestNumber'])
    else:
        return "Error: No TestNumber field provided. Please specify a TestNumber."

    # Create an empty list for our results
    results = []

    for test in json_data:
        if test['Test Number'] == testNo:
            results.append(test)

    # Use the jsonify function from Flask to convert our list of Python dictionaries to the JSON format.
    return jsonify(results)

app.run()