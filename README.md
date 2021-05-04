

# Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [File Descriptions](#files)
4. [Results](#results)
5. [Licensing, Authors, and Acknowledgements](#licensing)

### Installation and Run <a name="installation"></a>

#### Packages
* [SQLAlchemy](https://pypi.org/project/SQLAlchemy/)

* [nltk](https://pypi.org/project/nltk/)

* [scikit-learn](https://scikit-learn.org/stable/install.html)

* [plotly](https://plotly.com/python/getting-started/)

#### Run:


In the project directory run these commands in sequence:
1. `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
2. `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`
3. `python app/run.py`



## File Descriptions <a name="files"></a>
```
├── ETL Pipeline Preparation.ipynb
├── ML Pipeline Preparation.ipynb
├── README.md
├── app
│   ├── run.py
│   └── templates
│       ├── go.html
│       └── master.html
├── data
│   ├── disaster_categories.csv
│   ├── disaster_messages.csv
│   └── process_data.py
└── models
    └── train_classifier.py
```

0. `disaster_messages.csv`           : Dataframe with disaster-related messages.
1. `disaster_categories.csv`         : Label classification for each disaster-related message. 
2. `ETL Pipeline Preparation.ipynb`  : A Jupyter notebook that walks through the data cleaning and preparation.
3. `ML Pipeline Preparation.ipynb`   : A Jupyter Notebook that walks through the ML pipeline. There are a lot of useful notes here.
4. `process_data.py`                 : Processes the data for the pipeline.
5. `train_classifier.py`             : Trains pipeline on train data, shows F1_score on test data, and saves classifier for Flask App. 
6. `run.py`                          : Runs the Flask app. 


## Results<a name="results"></a>
The main output is Flask app that categorizes disaster-related messages using a multi-label classifier. There are also some cool plots of the train data on the home page. 
## Licensing, Authors, Acknowledgements<a name="licensing"></a>
[Plotly](https://plotly.com/chart-studio-help/json-chart-schema/) documentation code was used for the pie chart on the home page. Other parts of code are from Udacity.
