from flask import Flask, jsonify, abort, request, make_response, url_for
from pymongo import MongoClient
from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper
import json
import pandas as pd
app = Flask(__name__)

client = MongoClient()
db = client.arch

def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator
@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/flu/<string:yw>', methods=['GET'])
def get_tasks(yw):
    y, w= yw.split('-', 1)
    flu = db.fluData.find({"year": int(y), "week": int(w)})
    output = []
    for s in flu:
        output.append({'week': s['week'], 'year': s['year'],
                   'pneumonia_and_influenza_deaths': s['pneumonia_and_influenza_deaths'],
                   'all_deaths': s['all_deaths'], 'state': s['state'], 'region': s['region'],
                    'city': s['city']})
    return jsonify(output)


if __name__ == '__main__':
    app.run()