import pandas as pd
from nltk.corpus import stopwords
import string


ds =pd.read_csv("spam.csv",encoding='latin1')
# print(ds.head())


# dropping NAN columns
ds.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace=True)
# print(ds.head())


# Lower case letters
def lowercase_text(text):
    text=text.lower()
    return text
ds['v2']=ds['v2'].apply(lowercase_text)
# print(ds.head())


#Removing puctuation
PUNCT_TO_REMOVE=string.punctuation
def remove_punctuation(text):
    text=text.translate(str.maketrans('','',PUNCT_TO_REMOVE))
    return text
ds['v2']=ds['v2'].apply(remove_punctuation)
# print(ds.head())


# Removing Stopwords
STOPWORDS=set(stopwords.words('english'))
def remove_stopwords(text):
    text= " ".join([word for word in str(text).split() if word not in STOPWORDS])
    return text
ds['v2']=ds['v2'].apply(remove_stopwords)
# print(ds.head())
