#!/usr/bin/env python
# coding: utf-8

# In[1]:


from nltk.corpus import brown


# In[2]:


brown


# In[4]:


brown.categories()


# In[5]:


brown.words(categories = "science_fiction")[:100]


# In[6]:


from nltk.corpus import inaugural


# In[10]:


inaugural.fileids()


# In[21]:


for i in inaugural.words('1933-Roosevelt.txt'):
    print(i, end = " ")


# In[14]:


'''
here ma'am is revising the previous class topics
'''


# In[22]:


from nltk.corpus import webtext


# In[23]:


webtext.fileids()


# In[28]:


webtext.words('pirates.txt')[:20]


# In[34]:


#print first 20 words from each file

file_ids = webtext.fileids()
for file in file_ids:
    print(file)
    print(webtext.words(file)[:20])
    

    


# In[35]:


#downloading a text from ANC, analysing the data
#http://www.anc.org/data/masc/downloads/data-download/
import nltk
f = open('tweets1.txt','r')
text = f.read()


# In[37]:


print(text)


# In[40]:


text1 = text.split()
print(text1)


# In[50]:


text2 = nltk.Text(text1)
print(text2)


# In[52]:


text2.concordance('good')


# In[5]:


#project gutenberg
#we will attempt to open a book url in project gutenberg and analyse the text

from urllib import request

url = "http://www.gutenberg.org/files/2554/2554-0.txt"

response = request.urlopen(url)

raw_data = response.read().decode('utf8')


# In[4]:


raw_data


# In[56]:


text1 = raw_data.split()


# In[63]:


len(text1)


# In[6]:


#tokenizing with nltk.tokenize.word_tokenize

from nltk.tokenize import word_tokenize
tokens = word_tokenize(raw_data)
len(raw_data)


# In[ ]:




