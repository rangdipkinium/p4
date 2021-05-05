


# Table of Contents

0. [Project Overview](#motivation)
1. [Problem Statement](#problem)
2. [metrics](#metrics)
3. [Installation](#installation)
4. [File Descriptions](#files)
5. [Results](#results)
6. [Licensing, Authors, and Acknowledgements](#licensing)



## Project Overview <a name="motivation"></a>
When humans look at images, we take for granted that our brain can process the image and decide what the image contains fairly quickly. The goal of my CNN and CNNs in general (at least for image recognition and classification) is to replicate this process algorithmically and to teach our computer how to do this. With this in mind, the aim of this project was to define and train a Convolutional Neural Network (CNN) that could predict dog breeds from images of dogs. 
The final CNN used in the app was built using transfer learning from Google's InceptionV3 CNN, with additional training on dog-specific images provided by udacity.  


## Problem Statement<a name="problem"></a>
Using images provided by udacity, my main objective was to create and train a CNN that could predict dog breeds from images of dogs. 
The image dataset used to train, validate, and test my CNN consisted of 8351 different dog images, with 133 different dog breeds given as labels. This data was provided by Udacity. The images were also passed through Google's InceptionV3 model before being passed into my CNN's layers. 

## Metrics <a name="metrics"></a>
```
Train on 6680 samples, validate on 835 samples
Epoch 1/20
6560/6680 [============================>.] - ETA: 0s - loss: 2.9215 - acc: 0.4096Epoch 00001: saving model to saved_models/weights.best.inception.hdf5
6680/6680 [==============================] - 3s 506us/step - loss: 2.9058 - acc: 0.4115 - val_loss: 0.8396 - val_acc: 0.7521
Epoch 2/20
6600/6680 [============================>.] - ETA: 0s - loss: 1.5602 - acc: 0.6258Epoch 00002: saving model to saved_models/weights.best.inception.hdf5
6680/6680 [==============================] - 3s 455us/step - loss: 1.5630 - acc: 0.6254 - val_loss: 0.7016 - val_acc: 0.7940
Epoch 3/20
6620/6680 [============================>.] - ETA: 0s - loss: 1.3627 - acc: 0.6725Epoch 00003: saving model to saved_models/weights.best.inception.hdf5
6680/6680 [==============================] - 3s 456us/step - loss: 1.3683 - acc: 0.6716 - val_loss: 0.7009 - val_acc: 0.8132
Epoch 4/20
6640/6680 [============================>.] - ETA: 0s - loss: 1.3000 - acc: 0.6962Epoch 00004: saving model to saved_models/weights.best.inception.hdf5
6680/6680 [==============================] - 3s 455us/step - loss: 1.3050 - acc: 0.6963 - val_loss: 0.6377 - val_acc: 0.8060
Epoch 5/20
6580/6680 [============================>.] - ETA: 0s - loss: 1.2519 - acc: 0.7216Epoch 00005: saving model to saved_models/weights.best.inception.hdf5
6680/6680 [==============================] - 3s 455us/step - loss: 1.2463 - acc: 0.7225 - val_loss: 0.6217 - val_acc: 0.8311
Epoch 6/20
6580/6680 [============================>.] - ETA: 0s - loss: 1.2271 - acc: 0.7315Epoch 00006: saving model to saved_models/weights.best.inception.hdf5
6680/6680 [==============================] - 3s 458us/step - loss: 1.2286 - acc: 0.7313 - val_loss: 0.6577 - val_acc: 0.8335
Epoch 7/20
6600/6680 [============================>.] - ETA: 0s - loss: 1.2021 - acc: 0.7373Epoch 00007: saving model to saved_models/weights.best.inception.hdf5
6680/6680 [==============================] - 3s 453us/step - loss: 1.2014 - acc: 0.7370 - val_loss: 0.7178 - val_acc: 0.8335
Epoch 8/20
6660/6680 [============================>.] - ETA: 0s - loss: 1.1534 - acc: 0.7452Epoch 00008: saving model to saved_models/weights.best.inception.hdf5
6680/6680 [==============================] - 3s 457us/step - loss: 1.1560 - acc: 0.7446 - val_loss: 0.6361 - val_acc: 0.8539
Epoch 9/20
6660/6680 [============================>.] - ETA: 0s - loss: 1.1716 - acc: 0.7616Epoch 00009: saving model to saved_models/weights.best.inception.hdf5
6680/6680 [==============================] - 3s 458us/step - loss: 1.1706 - acc: 0.7617 - val_loss: 0.7195 - val_acc: 0.8419
Epoch 10/20
6560/6680 [============================>.] - ETA: 0s - loss: 1.1529 - acc: 0.7651Epoch 00010: saving model to saved_models/weights.best.inception.hdf5
6680/6680 [==============================] - 3s 460us/step - loss: 1.1499 - acc: 0.7654 - val_loss: 0.7758 - val_acc: 0.8335
Epoch 11/20
6620/6680 [============================>.] - ETA: 0s - loss: 1.1003 - acc: 0.7715Epoch 00011: saving model to saved_models/weights.best.inception.hdf5
6680/6680 [==============================] - 3s 459us/step - loss: 1.1020 - acc: 0.7716 - val_loss: 0.8044 - val_acc: 0.8311
Epoch 12/20
6640/6680 [============================>.] - ETA: 0s - loss: 1.1262 - acc: 0.7768Epoch 00012: saving model to saved_models/weights.best.inception.hdf5
6680/6680 [==============================] - 3s 456us/step - loss: 1.1267 - acc: 0.7766 - val_loss: 0.7426 - val_acc: 0.8407
Epoch 13/20
6580/6680 [============================>.] - ETA: 0s - loss: 1.1331 - acc: 0.7737Epoch 00013: saving model to saved_models/weights.best.inception.hdf5
6680/6680 [==============================] - 3s 457us/step - loss: 1.1349 - acc: 0.7738 - val_loss: 0.7040 - val_acc: 0.8503
Epoch 14/20
6560/6680 [============================>.] - ETA: 0s - loss: 1.0911 - acc: 0.7787Epoch 00014: saving model to saved_models/weights.best.inception.hdf5
6680/6680 [==============================] - 3s 456us/step - loss: 1.1042 - acc: 0.7778 - val_loss: 0.7750 - val_acc: 0.8479
Epoch 15/20
6600/6680 [============================>.] - ETA: 0s - loss: 1.0813 - acc: 0.7912Epoch 00015: saving model to saved_models/weights.best.inception.hdf5
6680/6680 [==============================] - 3s 456us/step - loss: 1.0862 - acc: 0.7907 - val_loss: 0.8453 - val_acc: 0.8551
Epoch 16/20
6560/6680 [============================>.] - ETA: 0s - loss: 1.1084 - acc: 0.7945Epoch 00016: saving model to saved_models/weights.best.inception.hdf5
6680/6680 [==============================] - 3s 453us/step - loss: 1.1076 - acc: 0.7940 - val_loss: 0.8314 - val_acc: 0.8359
Epoch 17/20
6640/6680 [============================>.] - ETA: 0s - loss: 1.1697 - acc: 0.7869Epoch 00017: saving model to saved_models/weights.best.inception.hdf5
6680/6680 [==============================] - 3s 455us/step - loss: 1.1686 - acc: 0.7871 - val_loss: 0.8226 - val_acc: 0.8395
Epoch 18/20
6560/6680 [============================>.] - ETA: 0s - loss: 1.1474 - acc: 0.7971Epoch 00018: saving model to saved_models/weights.best.inception.hdf5
6680/6680 [==============================] - 3s 454us/step - loss: 1.1506 - acc: 0.7966 - val_loss: 0.8446 - val_acc: 0.8491
Epoch 19/20
6580/6680 [============================>.] - ETA: 0s - loss: 1.1042 - acc: 0.7983Epoch 00019: saving model to saved_models/weights.best.inception.hdf5
6680/6680 [==============================] - 3s 456us/step - loss: 1.1002 - acc: 0.7985 - val_loss: 0.8792 - val_acc: 0.8371
Epoch 20/20
6580/6680 [============================>.] - ETA: 0s - loss: 1.0823 - acc: 0.8024Epoch 00020: saving model to saved_models/weights.best.inception.hdf5
6680/6680 [==============================] - 3s 455us/step - loss: 1.0801 - acc: 0.8030 - val_loss: 0.8824 - val_acc: 0.8599

```


When using the app, keep the image size below 1MB for optimum performance!



## Installation and Run <a name="installation"></a>
The app uses the following non-standard packages: To see a list of all of the packages required to run the app, please look at the requirements.txt file in `app_heroku`. 

```
Keras==2.4.3
dash==1.20.0
dash_core_components==1.16.0
opencv_python==4.5.1.48
tensorflow==2.4.1
dash_html_components==1.1.3
Pillow==8.2.0
```
## File Descriptions <a name="files"></a>

`dog_app.ipynb : This file contains all of the work to build the model used in the app`

`dog_app.html : This is a copy of dog_app.ipynb`

`dog_app.pdf : This is a copy of dog_app.ipynb`

`app_heroku : This folder contains all of the files needed to deploy the app to heroku, or to run the app locally`

        - `saved_models` : This folder contains all of the saved CNN model weights
        
        - `app.py` : This is the main app file
        
        - `dog_code.py` : This file reads in images in the app and applies the model to them





#### Run:
##### To view the app in Heroku: https://dogdash.herokuapp.com

##### To run the app locally, follow these steps:

1. `cd app_heroku`
2. `pip install --user virtualenv`
3. `virtualenv env`
4. `source venv/bin/activate`
5. `pip install -r requirements.txt`
6. `python app.py`



When using the app, keep the image size below 1MB for optimum performance!





## Results<a name="results"></a>
![file](dog_app.png)

## Licensing, Authors, Acknowledgements<a name="licensing"></a>
Transfer learning models such as InceptionV3, VGG16, and VGG19 were used. Acknowledgement goes to Udacity for the jupyter notebook template
