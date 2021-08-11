# TITLE : Predicting Stock Prices for Large Cap Technology Companies

## DATASETS USED

-  Nasdaq:  https://www.nasdaq.com/
-  Xignite: https://www.xignite.com/


## OVERVIEW:
             Data Segmentation and Data Cleaning 
             Exploratory Data Analysis 
             Training the model based on the data available
             Model Deployment Using Streamlit and Heroku

## DATASETS:
  The dataset consists of 9 years’ worth of stock price data for 20 large-cap-technology 
companies and the NASDAQ-100 Technology Sector Index dating from 11/14/2012 to 11/14/2021. And other dataset consists of headlines of different companies from 01/01/2015 to 
06/23/2021.

SL.NO	     ATTRIBUTES	          DESCRIPTION
     1.	        DATE	       Date of the stock value
     2.	        OPEN	       Opening price of stock
     3.         CLOSE/LAST	 Closing price of stock
     4.	        HIGH	       Highest point of the price of stock at the exchange
     5.	        LOW        	 Lowest point of the price of stock at the exchange
     6.	        VOLUME	     Volume of stock is average of total traded stocks at the exchange over a period of time.
     7.	        HEADLINES	   Companies headlines on a particular day


## TEXT PREPROCESSING 
Text preprocessing is an important task and critical step in text analysis and Natural language processing (NLP). It transforms the text into a form that is predictable and analysable so that machine learning algorithms can perform better. 
There are different ways to preprocess the text. Here are some of the approaches of preprocessing the text. 
• Removing Punctuations 
• Converting Headlines to lower case 
• Tokenization 
• Removing white space 
• normalization 

## TRAINING AND TESTING THE MODEL: 
The following models are trained and tested for this Project Models are: 
            • Linear Regression 
            • LSTM Neural network

Table : Model Fitting :Finding the best algorithm
            Accuracy Linear Regression 
            Accuracy 99.822 93.338
            we used linear regression model for the deployment.


## DEPLOYMENT: 
The project deployment is done using “Streamlit and Heroku”. Streamlit is an app 
framework to deploy machine learning apps built using Python. It is an opensource framework which is similar to the Shiny package in R. Heroku is a 
platform-as-a-service (PaaS) that enables deployment and managing applications 
built in several programming languages in the cloud.
 Steps to deploy 
Step 1: Run your Streamlit App Locally
Step 2: Create a GitHub repository
Step 3: Create a requirements.txt, setup.sh, and Procfile.
Step 3: Connect to Heroku

Check the link for the deployed Application:
            o https://apple-stock-price-predictor.herokuapp.com/
