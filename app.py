from collections import OrderedDict
from datetime import datetime

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    experience = (datetime.now() - datetime(year=2014, month=10, day=1)).days
    experience = int(experience / 360)
    response = OrderedDict(
        about=f'Software engineer with {experience} years experience, focused on Backend engineering.',
        contact={
            'email': 'adiyatmubarak@gmail.com',
            'twitter': 'https://twitter.com/adiyatmubarak',
            'linkedin': 'https://www.linkedin.com/in/adiyatmubarak/',
            'github': 'https://github.com/Keda87',
            'stackoverflow': 'https://stackoverflow.com/users/story/1936697',
            'blog': 'https://adiyatmubarak.wordpress.com/'
        },
    )
    return jsonify(response)
