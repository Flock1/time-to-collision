import numpy as np
from keras.models import model_from_json
import cv2

def scale(X):
    X = X.astype('float32')
    X /= 255.0
    return X


def pre_process(img, x1=319, x2=70, row_start=400, col_start=600):
    cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
    cv_img = cv2.bilateralFilter(cv_img,9,75,75)
    crop_img = cv_img[row_start:row_start+x1,col_start:col_start+x2]
    crop_img = crop_img.reshape(-1, x1,x2,1)
    crop_img = scale(crop_img)
    return crop_img



def get_model():
    # load json and create model
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("model.h5")
    
    loaded_model.compile(loss='binary_crossentropy', 
                         optimizer='rmsprop', 
                         metrics=['accuracy'])
    return loaded_model


loaded_model = get_model()
    
def predict(x):
    scores = loaded_model.predict(x)
    return np.argmax(scores)


def get_image_class(x):
    x = pre_process(x)
    return predict(x)

    
