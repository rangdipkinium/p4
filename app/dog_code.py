import io
import copy
import numpy as np
import base64
import tensorflow as tf
from keras.preprocessing import image
from keras.models import load_model
import keras.backend as K
from extract_bottleneck_features import *

# Read list of dog labels (133 total)
dog_names = list(np.load('dog_names.npy'))


# Load custom inception model
inception_model = load_model('saved_models/weights.best.inception.hdf5')



def path_to_tensor(img_encoded):
    """
    Loads image from app and decodes it. Then turns the image into 4D tensor

    Parameters:
        img_encoded (str): Encoded image passed in by dash app file upload


    Returns:
        4D tensor of image
    """


    # Make copy of image string
    itest = copy.copy(img_encoded)


    # Remove datatype from encoded image
    itest = img_encoded.split(',')[1]


    # Decode image str base64
    img_str = base64.b64decode(itest)


    # Then decode image from jpeg using tensorflow
    e = tf.image.decode_jpeg(img_str)



    # Convert PIL.Image.Image type to 3D tensor with shape (224, 224, 3)
    e1 = tf.image.resize(e, (224, 224))


    # Convert 3D tensor to 4D tensor with shape (1, 224, 224, 3) and return 4D tensor
    t2 = image.img_to_array(e1)
    t3 = np.expand_dims(t2, axis=0)


    # Make a copy of the final tensor
    t4 = copy.copy(t3)


    # Return Tensor
    return t4


def inception_predict_breed(img_encoded):
    """
    Loads image from app and decodes it using path_to_tensor.
    Then turns the predicted dog breed using tensorflow model.

    Parameters:
        img_encoded (str): Encoded image passed in by dash app file upload


    Returns:
        Predicted dog breed
    """


    # Extract bottleneck features
    bottleneck_feature = extract_InceptionV3(path_to_tensor(img_encoded))


    # Obtain predicted vector
    predicted_vector = inception_model.predict(bottleneck_feature)


    # Return dog breed that is predicted by the model
    return dog_names[np.argmax(predicted_vector)]


def human_dog_predict(img_encoded):
    """
    Loads image from app and decodes it using path_to_tensor.
    Creates a string with the .

    Parameters:
        img_encoded (str): Encoded image passed in by dash app file upload


    Returns:
        Predicted dog breed string to display in app
    """



    # Get predicted dog breed using passed in image
    predicted_dog_breed = inception_predict_breed(img_encoded)


    # Get predicted dog breed and format dog name
    if predicted_dog_breed is not None:
        predicted_dog_breed = ' '.join(predicted_dog_breed.split('.')[-1].split('_')).title()


    # Create string with predicted dog breed
    ps = 'The most similar dog breed is: {}'.format(predicted_dog_breed)


    # Clear backend Keras session for memory optimization
    K.clear_session()


    # Return string with prediction to display in app
    return (ps)
