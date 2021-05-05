


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
