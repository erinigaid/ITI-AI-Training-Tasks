#lowercasing
def lowercase_text(text):
    return text.lower()
text='My Name Is Erini Sabry'
print("lower case: ",lowercase_text(text))

# remove punctuations
txt="Hello, Sam!"
mytable=txt.maketrans("S","P")
print("replaceing: ",txt.translate(mytable))

import string
PUNCT_TO_REMOVE=string.punctuation

def remove_punctuation(text):
    return text.translate(str.maketrans('','',PUNCT_TO_REMOVE))
text="I'm having a lot of punctuations!!.All special characters will be removed;);)is it so?##Yes"
print("removing punctuation: ",remove_punctuation(text))

# removing stop words
from nltk.corpus import stopwords
STOPWORDS=set(stopwords.words('english'))
def remove_stopwords(text):
    return "".join([word for word in str(text).split()if word not in STOPWORDS])
text="MMy name is Erini Sabry.\n I am a student in ACU."
print("removing stop words: ",remove_stopwords(text))

from nltk.stem import PorterStemmer
stemmer=PorterStemmer()
def stem_words(text):
    return"".join([stemmer.stem(word)for word in text.split()])
text="I love to play games. I like gaming very much. One of my favorite games is counter strikes"
print("stem words: ",stem_words(lowercase_text(text)))

import re
def remove_emoji(string):
    emoji_pattern = re.compile("["
                           "\U0001F600-\U0001F64F"  # emoticons
                           "\U0001F300-\U0001F5FF"  # symbols & pictographs
                           "\U0001F680-\U0001F6FF"  # transport & map symbols
                           "\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "\U00002702-\U000027B0"
                           "\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub('', string)
print(remove_emoji("😀😀 remove emojis 😀😀"))

