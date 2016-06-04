from flask import Flask
from flask import request
from flask import redirect
from flask import url_for
from flask import render_template

import 

TITLE = 'gitcha'

app = Flask(__name__)

@app.route('/')
def index():
    query = request.args.get('query', '')

    output = []
    if query:
        param = make_query_param(query)
        output = request_to_engine(param)

    return render_template('index.html', title=TITLE)

def make_query_param(query):
    pass

if __name__ == "__main__":
    app.run(debug=True)
