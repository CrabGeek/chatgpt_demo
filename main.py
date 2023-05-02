import configparser
import json
import logging
import os

from flask import Flask, render_template, request, abort
from core import apitokenpool as apipool
from core import querybot as bot

app = Flask(__name__, template_folder='template')
log = logging.getLogger()
config = configparser.ConfigParser()


def init():
    config.read('./config.ini')
    app.config['UPLOAD_FOLDER'] = config.get('UPLOAD', 'upload_folder')

    log.setLevel(config.get('LOG', 'log_level'))
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('%(asctime)s-%(levelname)s: %(message)s'))

    log.addHandler(handler)

    pool = apipool.ApiTokenPool()
    pool.set(config.get('OPENAI', 'api_tokens').split(','))


@app.route('/')
def index():
    return render_template('index.html')


@app.route(rule='/query', methods=['POST'])
def query():
    data = request.get_json()
    if not data or data == '' or not data['query'] or data['query'] == '':
        log.warning('user question is empty')
        abort(400)
    log.info(data['query'])
    # TODO: query via OPENAI
    queryBot = bot.QueryBot()
    answer = queryBot.query(data['query'])
    log.info(f'AI answer: [{answer}]')
    rep = {
        'response': answer
    }
    return json.dumps(rep)


@app.route(rule='/query/file/upload', methods=['POST'])
def query_file():
    file = request.files['file']
    if file:
        log.info(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        rep = {
            'response': 'Thanks'
        }
        return json.dumps(rep)


if __name__ == '__main__':
    init()
    app.run(host='0.0.0.0', port=8567)
