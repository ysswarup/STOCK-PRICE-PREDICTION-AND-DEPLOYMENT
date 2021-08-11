#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('wordnet')
from nltk.stem import LancasterStemmer, WordNetLemmatizer, PorterStemmer
from nltk.tokenize import word_tokenize
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.metrics import accuracy_score, classification_report
from textblob import TextBlob
import string
import pickle
import streamlit as st

pickle_in = open("model.pkl","rb")
regressor = pickle.load(pickle_in)

def lemmat(text):
    lemma=WordNetLemmatizer()
    words=word_tokenize(text)
    return ' '.join([lemma.lemmatize(word) for word in words])

def getsubjectivity(text):
    return TextBlob(text).sentiment.subjectivity
def getpolarity(text):
    return TextBlob(text).sentiment.polarity

def char_rmvl(text):
    new=[char for char in text if char not in string.punctuation]
    vl=''.join(new)
    new.clear()
    return vl

def preprocess(Headlines):
    Headlines1 = [ x.lower() for x in Headlines]
    Headlines1 = [char_rmvl(x) for x in Headlines1]
    stop = stopwords.words('english')
    Headlines1 = [' '.join([word for word in s.split() if word not in (stop)]) for s in Headlines1]
    Headlines1 = [lemmat(s) for s in Headlines1]
    return Headlines1

def price(High,Low,Open,Volume,Headlines):
    ml = pd.DataFrame()
    ml['Volume']=Volume,Volume
    ml['Open']=Open,Open
    ml['High']=High,High
    ml['Low']=Low,Low
    ml['Headlines']=Headlines,Headlines
    ml['Headlines']=ml['Headlines'].astype(str)
    sid= SentimentIntensityAnalyzer()
    ml['compound'] = ml['Headlines'].apply(lambda x: sid.polarity_scores(x)['compound'])
    ml['negative'] = ml['Headlines'].apply(lambda x: sid.polarity_scores(x)['neg'])
    ml['neutral'] = ml['Headlines'].apply(lambda x: sid.polarity_scores(x)['neu'])
    ml['positive'] = ml['Headlines'].apply(lambda x: sid.polarity_scores(x)['pos'])

    ml['subjectivity']=ml['Headlines'].apply(getsubjectivity)
    ml['polarity']=ml['Headlines'].apply(getpolarity)

    k= ml[['Volume','Open','High','Low','compound','negative','neutral','positive','subjectivity','polarity']]
    return k

def main():
    st.title("Apple Inc. Stock Price Prediction")
    html_temp = """
    <div style="background-color:#FFD700;padding:10px">
    <h2 style="color:black;text-align:center;">APPLE CLOSE PRICE PREDICTOR</h2>
    </div>
    """

    st.markdown(html_temp,unsafe_allow_html=True)
    High = st.text_input("High")
    Low = st.text_input("Low")
    Open = st.text_input("Open")
    Volume = st.text_input("Volume")
    Headlines= st.text_input("Headlines")
    Headlines=list(Headlines.split("-"))
    hdlines1 = preprocess(Headlines)
    kn=pd.DataFrame()
    kn=price(High,Low,Open,Volume,hdlines1)
    kn1=np.array(kn)


    ans=''
    if st.button("Predict"):
        ans = regressor.predict(kn1)[0]
    st.success('Predicted Close Price : $ {}'.format(ans))
    if st.button("About"):
        st.text("Close price of the Stock is predicted based on news headlines and historical data using Linear Regression")
        
if __name__ =='__main__':
    main()


# In[ ]:




