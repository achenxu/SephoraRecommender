from app.api.rest.test import Receive
from app.api.rest.product import get_info
import numpy
from PIL import Image
import io
from app.api.rest.autoencoder import model_predict

def Consume(uploadedImage):

    image_uploaded = uploadedImage.read()
    image_data = image_uploaded
    rgb = Image.open(io.BytesIO(image_data)).convert("RGB")
    #print ("unresized: ", (numpy.array(rgb)).shape)
    resized = rgb.resize((500,500), Image.ANTIALIAS)
    numpy_array = numpy.array(resized)
    #print("resized: ", numpy_array.shape)

    r = model_predict(numpy_array)
    return get_info(r)
