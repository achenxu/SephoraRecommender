from datetime import datetime
from flask import request
from flask_restplus import Api
from app.api.rest.base import BaseResource, SecureResource
from app.api import api_rest
from app.api.rest.consumer import Consume

@api_rest.route('/upload')
class uploadResource(BaseResource):

    def post(self):
        json_payload = request.json
        uploadedImage = request.files['photos']
        print(uploadedImage)
        response = Consume(uploadedImage)
        return {'hello' : response}, 200