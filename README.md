# Final Project: A Rule-based Expert System on COVID-19 Diagnosis

## Introduction

This system uses a set of predefined rules to analyze patient responses to a series of questions and determine the
likelihood of a COVID-19 infection. This type of system is designed to be user-friendly and can be accessed
 by patients via browsers who are seeking medical advice or diagnosis. These predefined rules are achieved by decision 
tree which is a decision support hierarchical model.

## Two Components of the Project

This project consists of two parts: model building and website building. The first part (shown in the jupypter file
ModelBuilding.ipynb) utilized the Covid Dataset.cs to build a decsion tree model. The second part is
a website built on Django web framework, where one web page shows a questionnaire that users can answer, and another web
page shows the prediction result according to the answers of those questions. This website leveraged the trained model to do prediction. 

## Purpose of the Project

One advantage of a rule-based expert system on COVID-19 diagnosis by questionnaires is that it can provide a
quick and easy way for patients to assess their risk of infection without having to visit a healthcare facility. It can
also potentially reduce the workload of healthcare professionals by automating some of the diagnostic tasks.

## How to run

### Requirements
These packages are required for running the project (both the ipynb and the website):
- django
- numpy
- matplotlib
- pandas
- seaborn
- scikit-learn

Actually, they have been included in requirements.txt. You can run the command to install these packages:
```pip install -r requirements.txt```
  (before that, you can create a virtual environment by :```python3 -m venv venv``` 
and activate that environment by: ```source venv/bin/activate``` )

### Run the Jupypter Notebook (ModelBuilding.ipynb)
- Method 1: Open the file and run all cells
- Method 2: run the command (please make sure the juypter has been installed):
jupyter nbconvert --execute ModelBuilding.ipynb

### Run the website (under directory /mysite)
run these commands:
```cd ./mysite```
```python manage.py runserver```
access the website by this url: http://127.0.0.1:8000/


## Results (Screenshots)
This is the main page:




## Explain the decision

## Issues

## References















