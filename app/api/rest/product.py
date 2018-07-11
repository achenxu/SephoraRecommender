from flask import request
from flask_restplus import Api
import json
from operator import itemgetter
import requests
from app.api.rest.base import BaseResource, SecureResource
from app.api import api_rest

def get_info(listOfMatches):
    # sort the list of dictionaries by confidence in descending order
    # take only the first 10 products
    sortedList = sorted(listOfMatches, key=itemgetter('confidence'), reverse=True)[:10]

    listOfProductInfoDictionaries = [];

    # for each of the 10 products, call the sephora endpoint to get product name, brand, price, variant image, variant name
    for product in sortedList:
                r = requests.get('https://sephora.sg/api/v2/products/' + product.get('productId') + '?include=variants', headers={'Accept-Language':'en-SG', 'Content-Type':'application/json'}).json()
                print(r.keys())
                listOfIncluded = r["included"]
                #retrieve the variant dictionary
                variant = next((v for v in listOfIncluded if v['id'] == product.get('variantId')), None)
                variantName = variant['attributes']['name']
                variantPrice = variant['attributes']['price']
                variantImage = variant['attributes']['image-url']
                productName = variant['attributes']['product-name']
                brandName = variant['attributes']['brand-name']

                productInfo = {"variantName": variantName, "variantPrice": variantPrice, "variantImage": variantImage, "productName": productName, "brandName": brandName}
                listOfProductInfoDictionaries.append(productInfo)


    return json.dumps(listOfProductInfoDictionaries)
