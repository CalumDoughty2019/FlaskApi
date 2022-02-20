import flask
from flask import request, jsonify
import sys

app = flask.Flask(__name__) # Create a flask object called app
app.config["DEBUG"] = True # Have an audit trail

# Create some test data for our catalog in the form of a list of dictionaries
books = [
    {'id': 0,
     'title': 'Data and Computer Communication',
     'author': 'William Stallings',
     'ISBN': '9781292014388',
     'year_published': '2014'},
    {'id': 1,
     'title': 'Computer Networks',
     'author': 'Andrew Tanenbaum & David Wetherall',
     'ISBN': '9781292024226',
     'year_published': '2015'},
    {'id': 2,
     'title': 'Mastering Networks',
     'author': 'William Buchanan',
     'first_sentence': '9780333748046',
     'year_published': '1999'}
]

@app.route('/', methods=['GET']) # Decorator called route
def home():
    return '''<h1>TextBook Archive</h1>
    <p>A prototype API for distant reading of computer networking textbooks.</p>'''

@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

# app.run()
# sys.exit(0)
@app.route('/api/v1/resources/books', methods=['GET']) # /api/v1/resources/books?id=0
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for book in books:
        if book['id'] == id:
            results.append(book)

    # Use the jsonify function from Flask to convert our list of Python dictionaries to the JSON format.
    return jsonify(results)

app.run()