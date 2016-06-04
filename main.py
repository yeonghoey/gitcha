import re
import multiprocessing

from flask import Flask
from flask import request
from flask import redirect
from flask import url_for
from flask import render_template

import predictionio

TITLE = 'gitcha'

USER_PATTERN = r'(\w|-)+'
REPO_PATTERN = r'{user}/(\w|-|\.)+'.format(user=USER_PATTERN)

app = Flask(__name__)
user_re = re.compile(USER_PATTERN)
repo_re = re.compile(REPO_PATTERN)

engine_client = predictionio.EngineClient(url="https://localhost:8000")

@app.route('/')
def index():
    query = request.args.get('query', '')

    output = None
    if query:
        output = request_to_engine(query)

    return render_template('index.html', title=TITLE, output=output)

def request_to_engine(query):
    if user_re.match(query):
        rep = engine_client.send_query({"user": query})
        return rep_to_output(rep)
    elif repo_re.match(query):
        rep = engine_client.send_query({"user": query})
        return rep_to_output(rep)
    else:
        return []

def rep_to_output(rep):
    return [ item_dict['item'] for item_dict in rep['itemScores']]

if __name__ == "__main__":
    app.run(host='0.0.0.0')
