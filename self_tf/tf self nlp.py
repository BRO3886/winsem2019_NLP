#!/usr/bin/env python
# coding: utf-8

# In[2]:


import warnings; warnings.simplefilter('ignore')


# In[24]:


from tensorflow.keras.preprocessing.text import Tokenizer
tokenizer = Tokenizer(num_words = 100)
sentences = [
    'I love my dog',
    'I love my cat',
    'You love my rat?',
]
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index
print(word_index)


# In[26]:


from tensorflow.keras.preprocessing.text import Tokenizer
tokenizer = Tokenizer(num_words = 100)
sentences = [
    'I love my dog',
    'I love my cat',
    'You love my rat?',
    'Don\'t you thnk you\'re becoming fat?'
]
tokenizer.fit_on_texts(sentences)

word_index = tokenizer.word_index
sequences = tokenizer.texts_to_sequences(sentences)

print(word_index)
print(sequences)


# In[28]:


'''
how to handle out of vocabulary, here we also see how powerful the tokenizer is 
we can see it generates a list of sequences of tokens from previously generated tokens on
completely new sentences.
'''

tokenizer = Tokenizer(num_words = 100, oov_token = '<OOV>')
sentences = [
    'I love my dog',
    'I love my cat',
    'You love my rat?',
    'Don\'t you thnk you\'re becoming fat?'
]
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index

test_data = [
    'I think I love my cat',
    'She loves me!'
]
sequences = tokenizer.texts_to_sequences(test_data)

print(word_index)
print(sequences)


# In[36]:


'''
here we see padding. Padding is used to make the sentences the same len
we make a matrix of token sequences
'''
from tensorflow.keras.preprocessing.sequence import pad_sequences

tokenizer = Tokenizer(num_words = 100, oov_token = '<OOV>')

sentences = [
    'I love my dog',
    'I love my cat',
    'You love my rat?',
    'Don\'t you thnk you\'re becoming fat?'
]
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index

sequences = tokenizer.texts_to_sequences(sentences)

padded = pad_sequences(sequences)

print(word_index)
print(sequences)
print('\n')
print(padded)


# In[44]:


from tensorflow.keras.preprocessing.sequence import pad_sequences

tokenizer = Tokenizer(num_words = 100, oov_token = '<OOV>')

sentences = [
    'I love my dog',
    'I love my cat',
    'You love my rat?',
    'Don\'t you thnk you\'re becoming fat?'
]
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index

sequences = tokenizer.texts_to_sequences(sentences)

padded = pad_sequences(sequences,padding='post',maxlen =5, truncating='post')

print(word_index)
print(sequences)
print('\n')
print(padded)


# In[46]:


'''
reading sarcasm headlines json 
from https://rishabhmisra.github.io/publications/
'''

import json

def parse_data(file):
    for l in open(file,'r'):
        yield json.loads(l)
        
data = list(parse_data('./Sarcasm_Headlines_Dataset_v2.json'))
data


# In[47]:


sentences = []
labels = []
urls = []

for item in data:
    sentences.append(item['headline'])
    labels.append(item['is_sarcastic'])
    urls.append(item['article_link'])
sentences


# In[52]:


tokenizer = Tokenizer(oov_token = '<OOV>')
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index

sequences = tokenizer.texts_to_sequences(sentences)

padded = pad_sequences(sequences, padding = 'post')


# In[51]:


print(word_index)


# In[54]:


print(sentences[3])
print(sequences[3])
print(padded[3])
print(padded.shape)


# In[ ]:




