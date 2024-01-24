import os

import flask
from dotenv import load_dotenv
from flask_restful import Api, Resource

app = flask.Flask(__name__)
api = Api(app)

def configure():
    load_dotenv()

class steamApiKey(Resource):
    def get(self):
        return {'steamApiKey': os.getenv('api_key')}

configure()
api.add_resource(steamApiKey, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)