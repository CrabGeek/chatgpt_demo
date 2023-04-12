import json

from flask import Flask, render_template, request, abort, Response

from util import is_valid_request_json

app = Flask(__name__, template_folder='template')


@app.route('/')
def index():
    return render_template('index.html')


@app.route(rule='/query', methods=['POST'])
def query():
    if not request.json:
        abort(400)
    data = json.loads(request.get_data())
    if not is_valid_request_json(data):
        abort(400)
    print(data)
    rep = {
        'response': 'Thanks'
    }
    return json.dumps(rep)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8567)
