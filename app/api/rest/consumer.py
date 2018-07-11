import requests
from app.api.rest.test import Receive

def Consume(uploadedImage):
    image_uploaded = uploadedImage.read()
    r = Receive(image_uploaded)
    print(r)

    # r = request(image_uploaded).json()
    #
    # # ensure the request was successful
    # if r["success"]:
    #     # loop over the predictions and display them
    #     for (i, result) in enumerate(r["predictions"]):
    #         print("{}. {}: {:.4f}".format(i + 1, result["label"],
    #                                       result["probability"]))
    #
    # # otherwise, the request failed
    # else:
    #     print("Request failed")
