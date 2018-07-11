from flask import request
from flask_restplus import Api
import json

from app.api.rest.base import BaseResource, SecureResource
from app.api import api_rest


def get_info(listOfMatches):
    # sort the list of dictionaries by confidence in descending order
    # take only the first 10 products
    sortedList = sorted(listOfMatches, key=itemgetter('confidence'), reverse=True)[:10]

    # for each of the 10 products, call the sephora endpoint to get product name, brand, price, variant image, variant name
    for product in sortedList:
                r = request.get('https://luxola-staging-api.herokuapp.com/api/v2/products/' + item.get('productId') + '?include=variants').json()
                listOfIncluded = r.data.included
                #retrieve the variant dictionary
                variant = next((v for v in listOfIncluded if v['id'] == item.get('variantId')), None)
                variantName = variant.attributes.name
                variantPrice = variant.attributes.price
                variantImage = variant.attributes.image-url
                productName = variant.attributes.product-name
                brandName = variant.attributes.brand-name

    return json.dumps([variantName, variantPrice, variantImage, productName, brandName])
