import requests
from app.api.rest.test import Receive
from app.api.rest.product import get_info

def Consume(uploadedImage):
    image_uploaded = uploadedImage.read()
    r = Receive(image_uploaded)
    #print(r)
    return get_info(r)
