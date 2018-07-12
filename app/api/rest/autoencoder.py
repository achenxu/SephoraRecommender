from keras.models import load_model, Model
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

import pickle

PATH_TO_MODEL = 'autoencoder.h5'
PATH_TO_OUT_ENCODINGS = 'out_encodings.pckl'
PATH_TO_PRODUCTIDS = 'productIds.pckl'
PATH_TO_VARIANTIDS = 'variantIds.pckl'

# Load previsouly trained model
autoencoder = load_model(PATH_TO_MODEL)
# Get encoder layer from trained model
model = Model(inputs=autoencoder.input, outputs=autoencoder.get_layer('encoded').output)
model._make_predict_function()

with open(PATH_TO_OUT_ENCODINGS, 'rb') as f:
    out_encodings = pickle.load(f)

with open(PATH_TO_PRODUCTIDS, 'rb') as f:
    productIds = pickle.load(f)

with open(PATH_TO_VARIANTIDS, 'rb') as f:
    variantIds = pickle.load(f)

def model_predict(image_as_np_array, model=model, out_encodings=out_encodings, productIds=productIds, variantIds=variantIds):
    in_encoding = np.reshape(model.predict(np.array([image_as_np_array])), (1,-1))
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