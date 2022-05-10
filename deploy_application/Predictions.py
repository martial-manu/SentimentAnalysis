#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
import joblib
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences


# In[11]:


model = load_model('./model/sentiment')
maxlen = 50


# In[16]:


def predict(sentence):
    ip = []
    word_to_idx = joblib.load('word_to_idx.pkl')
    doom = sentence.split()
    print(doom)
    for j in range(len(doom)):
        if word_to_idx.get(doom[j]) is None:
            pass
        else :
            ip.append(word_to_idx[doom[j]])
    ip = pad_sequences([ip] , maxlen= maxlen , padding = 'post' , truncating = 'post')
    
    print(ip)
    ans = model.predict(ip)
    print(ans)
    res = np.argmax(ans)
    op = ["Positive :)" , "Negative :("]
    return op[res]




