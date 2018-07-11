from keras.models import load_model
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

import pickle

PATH_TO_MODEL = 'encoder.h5'
PATH_TO_OUT_ENCODINGS = 'out_encodings.pckl'
PATH_TO_PRODUCTIDS = 'productIds.pckl'
PATH_TO_VARIANTIDS = 'variantIds.pckl'

model = load_model(PATH_TO_MODEL)

with open(PATH_TO_OUT_ENCODINGS, 'rb') as f:
    out_encodings = pickle.load(f)

with open(PATH_TO_PRODUCTIDS, 'rb') as f:
    productIds = pickle.load(f)

with open(PATH_TO_VARIANTIDS, 'rb') as f:
    variantIds = pickle.load(f)

def model_predict(image_as_np_array, model=model, out_encodings=out_encodings, productIds=productIds, variantIds=variantIds):
    in_encoding = model.predict([image_as_np_array])
    scores = np.reshape(cosine_similarity(in_encoding, out_encodings), (-1))

    ret = []

    for i, score in enumerate(scores):
        ret.append(
            {
                'productId' : productIds[i],
                'variantId' : variantIds[i],
                'confidence' : score,
            }
        )

    return ret