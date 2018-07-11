"""
REST API Resource Routing
http://flask-restplus.readthedocs.io
"""

from datetime import datetime
from flask import request
from flask_restplus import Api

from app.api.rest.base import BaseResource, SecureResource
from app.api import api_rest


@api_rest.route('/resource/<string:resource_id>')
class ResourceOne(BaseResource):
    """ Sample Resource Class """

    def get(self, resource_id):
        timestamp = datetime.utcnow().isoformat()
        return {'timestamp': timestamp}

    def post(self, resource_id):
        json_payload = request.json
        return {'timestamp': json_payload}, 201


@api_rest.route('/secure-resource/<string:resource_id>')
class SecureResourceOne(SecureResource):

    def get(self, resource_id):
        timestamp = datetime.utcnow().isoformat()
        return {'timestamp': timestamp}

@api_rest.route('/upload')
class uploadResource(BaseResource):

    def post(self):
        json_payload = request.json
        # receive image here and process it
        print(json_payload)
        # change the response if needed
        return {'image_upload': 'success'}, 200
