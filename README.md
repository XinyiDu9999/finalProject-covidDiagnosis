# Final Project: A Rule-based Expert System on COVID-19 Diagnosis

## Background

Although COVID-19 is on the decline, its impact is still fresh in our minds. There is much to be learned from this global pandemic,
which can help us control and prevent similar outbreaks in the future. That's why I created this system, which enables people to self-diagnose COVID-19 infection through a machine learning model. 
With some adjustments, this system can also be applied to predict the infection of other diseases.

## Introduction
This system uses a set of predefined rules to analyze patient responses to a series of questions and determine the COVID-19 infection. This system is designed to be user-friendly and can be accessed
by patients via browsers who are seeking medical advice or diagnosis. These predefined rules are achieved by a machine learning model which is a decision tree. 

One advantage of a rule-based expert system on COVID-19 diagnosis by questionnaires is that it can provide a
quick and easy way for patients to assess their risk of infection without having to visit a healthcare facility. It can
also potentially reduce the workload of healthcare professionals by automating some of the diagnostic tasks.

## Definition of Rule-based Expert System

(Ishan Ayus et al., 2021)An expert system can be theoretically defined as a DSS which can mimic human’s thinking process to solve domain-specific
problems. The design of expert system mostly requires three major components: 
- Knowledgebase (KB): It contains set of factual rules and relevant data about an intended problem domain which are stored using some standard knowledge representation techniques. 
- Inference Engine (IE): The IE can be considered as the brain of expert system whose job is to derive conclusions from KB using some inference mechanism when queried by the user.
- User Interface (UI): The user of the expert system interacts with it through user interface. The queries asked by users are forwarded from UI to IE and IE uses KB to give the answer to users. 


## Three Components of this Expert System on Covid Diagnosis 

This system, in a nutshell, contains a model which is trained on a covid related dataset, and also  contains a website to accept queries from users.  
Corresponding to the components of an expert system, the dataset used to train the model is Knowledgebase (KB), since the model learnt the rules from the dataset. And the dataset contains the factors that are considered relevant to COVID confirmation by WHO.
On the other hands, The model works as the Inference Engine, which derives conclusions when queried by the user. Lastly, the website is the User Interface (UI), which forward the queries from users.

- Model Building:  
The model building process is documented in the [ModelBuilding.ipynb](./ModelBuilding.ipynb)  notebook. This process consists of three steps:  
    - Data Analysis:  
  This dataset is from kaggle (link:https://www.kaggle.com/datasets/hemanthhari/symptoms-and-covid-presence). It contains over 5000 data rows, each with 21 features, including the symptoms, geographical information, recent activity
and COVID test results.  
  - Data Processing:  
After visualizing the influence of each feature on COVID diagnosis, some features with low influence were dropped, leaving 12 features. 
These features were transformed to binary values, with 1 representing "yes" and 0 representing "no".
  - Model Training:  
   A decision tree model was built using the sklearn library, and the dataset was split into a training set and a test set in an 8:2 ratio. 
The 11 conditions were used as input values, and the COVID feature was used as the output value. The model achieved an accuracy score of 97%, and was saved for later use.

- Website Building:  
The second part of this project involved building a user-friendly website using the Django framework. 
The website features two pages: a questionnaire for users to answer, and a page displaying the predicted result and advice based on the user's answers. 
The website leverages the trained model to make predictions. See the accompanying screenshots below for more details.


## How to run
The Github link for this project:  https://github.com/XinyiDu9999/finalProject-covidDiagnosis  

### Requirements
Environment: Python3, Juypter  
These packages are required for running the project (both the ipynb and the website):
- django
- numpy
- matplotlib
- pandas
- seaborn
- scikit-learn

### Run the Jupypter Notebook (ModelBuilding.ipynb)
> **Note:** please make sure the juypter package has been installed   

Open the file and run all cells

### Run the website (under directory /mysite)
run these commands:   
```cd ./mysite```  
```pip3 install -r requirements.txt```   
```python3 manage.py runserver```   
access the website by this url: http://127.0.0.1:8000/
> **Note:** if you use python1 or python2, please use pip and python instead of pip3 and python3

## Results (Screenshots and Demo)
This is the main page:  
It contains many questions and a submit button  
<img src="https://i.ibb.co/S6qzGsv/Screenshot-2023-04-24-at-12-07-35-PM.png" alt="OpenAI logo" width="50%"/>

This is an example of result page :  
<img src="https://i.ibb.co/F3yTmMS/Screenshot-2023-04-24-at-12-07-55-PM.png" alt="OpenAI logo" width="50%"/>

Video demo:
url to youtube: https://youtu.be/Dly9Mgj8jrI

## Explain the Decision

In this project, a rule-based expert system is built using the decision tree. The decision tree is a flowchart-like 
structure that consists of internal nodes for testing attributes, branches for showing test results, and leaf nodes for indicating class labels. The decision tree can be transformed into decision rules, where the outcome is the content of the leaf node, and the conditions along the path form a conjunction in the if clause. Typically, the rules have the form "if condition1 and condition2 and condition3, then outcome" (Quinlan, J. R et al., 1987).

Due to its popularity in classification problems and the property of the decision tree, it is used in this project 
instead of manually writing a series of if and else statements. The decision tree model was trained on a dataset that contains COVID-19 symptoms and test results. The conditions, including symptoms and demographic information, were transformed into multidimensional input values, and the COVID-19 results were used as the target output results. By learning from the dataset, this model learned the rules of whether to output 1 or 0 on a specific input.

## Limitations

1. Limitation on Dataset:  
The dataset used in this project consists of only 5000 data points with 20 features, and it was collected in a specific 
environment. As a result, the model trained on this limited dataset may not be well generalized to other environments, due to the small size and limited scope of the dataset.

2. Limitation of Target Users:  
It is important to note that the model developed in this project is not intended for use in a severely ill emergency 
department or hospitalized patients, or for screening asymptomatic individuals. The model's purpose is to assist in the diagnosis of COVID-19 in symptomatic patients in a primary care setting.

3. Other issues  
The system relies on patients accurately reporting their symptoms, activity and other information, which may not always be the case. 
Additionally, the system may miss important details or nuances that a human expert would be able to identify


## Conclusion
Overall, a rule-based expert system on COVID-19 diagnosis can be a useful tool in supporting healthcare
professionals and patients in the diagnosis and management of COVID-19. However, it should be used in
conjunction with human expertise and clinical judgment, rather than as a replacement for it.

## Literature Review

In recent years, expert systems have emerged as a promising solution to support quick and accurate diagnosis of diseases. One such system, ESCOVID, was proposed by Ayus, I. et al. in 2023. This system utilizes a set of rules to aid common healthcare workers in predicting and diagnosing COVID-19 without consulting a medical expert. Ayus, I. et al. also discussed the fundamentals and architecture of expert systems. In another paper published in the same year, Betelhem Zewdu Wubineh et al. presented an expert system for COVID-19 diagnosis based on symptom analysis. This system aims to assist individuals in taking precautionary measures and seeking appropriate medical care.

Multivariable logistic regression has been used to identify independent predictors of COVID-19 in earlier studies, such as Alepis, E. et al. (2013). Based on the results, a weighted clinical prediction rule was developed to generate stratified likelihood ratios for varying scores. These papers have provided inspiration for the development of a COVID-19 pre-diagnosis expert system that relies on a series of rules.

After conducting thorough research, the decision tree method was selected for the development of the expert system. Decision tree techniques have been widely used to build classification models that closely resemble human reasoning and are easy to comprehend, as highlighted by Kotsiantis, S.B. et al. (2013). The use of decision trees in the COVID-19 pre-diagnosis expert system is expected to enhance accuracy and facilitate better decision-making for both healthcare workers and individuals seeking a preliminary diagnosis.


### references
1. Ayus, I., Panigrahi, N. (2021). A Decision Support System Using Rule-Based Expert System for COVID-19 Prediction and Diagnosis. In: Nandan Mohanty, S., Saxena, S.K., Satpathy, S., Chatterjee, J.M. (eds) Applications of Artificial Intelligence in COVID-19 . Medical Virology: From Pathogenesis to Disease Control. Springer, Singapore. https://doi.org/10.1007/978-981-15-7317-0_7

2. Betelhem Zewdu Wubineh , Ayodeji Olalekan Salau , Sepiribo Lucky Braide. (2023). Knowledge Based Expert System for Diagnosis of COVID-19 . Journal of Pharmaceutical Negative Results, 1242–1249. https://doi.org/10.47750/pnr.2023.14.03.165

3. Alepis, E., & Lambrinidis, C. (2013). M-health: Supporting automated diagnosis and electronic health records. Springerplus, 2, 103

4. Kotsiantis, S.B. Decision trees: a recent overview. Artif Intell Rev 39, 261–283 (2013). https://doi.org/10.1007/s10462-011-9272-4
5. Quinlan, J. R. (1987). "Simplifying decision trees". International Journal of Man-Machine Studies.
27 (3): 221–234. CiteSeerX 10.1.1.18.4267. doi:10.1016/S0020-7373(87)80053-6.
















