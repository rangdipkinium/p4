

# Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [File Descriptions](#files)
4. [Results](#results)
5. [Licensing, Authors, and Acknowledgements](#licensing)

### Installation and Run <a name="installation"></a>


#### Run:


In the project directory run these commands in sequence:
1. `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
2. `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`
3. `python app/run.py`



## Results<a name="results"></a>
The main output is Flask app that categorizes disaster-related messages using a multi-label classifier. There are also some cool plots of the train data on the home page. 
## Licensing, Authors, Acknowledgements<a name="licensing"></a>
[Plotly](https://plotly.com/chart-studio-help/json-chart-schema/) documentation code was used for the pie chart on the home page. Other parts of code are from Udacity.
