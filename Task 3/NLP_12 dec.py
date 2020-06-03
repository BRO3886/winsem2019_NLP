#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk


# In[2]:

#brown corpus of 1 million words
from nltk.corpus import brown


# In[3]:

#fiction,adventure etc
brown.categories()


# In[6]:


s = 0
for i in brown.categories():
    s+=1
s


# In[7]:


brown.words(categories = 'fiction')


# In[8]:


len(brown.words(categories = 'adventure'))


# In[11]:

#inaugural corpus of inaugural speeches made ny every POTUS
from nltk.corpus import inaugural


# In[12]:


inaugural.fileids()


# In[13]:


inaugural.words(fileids = '1861-Lincoln.txt',3)


# In[14]:


inaugural.words(fileids = '1861-Lincoln.txt')


# In[15]:


inaugural.words(fileids = '2009-Obama.txt')


# In[16]:


inaugural.words(fileids = '2017-Trump.txt')


# In[17]:


inaugral.words(fileids='2013-Obama.txt')


# In[18]:


inaugural.words(fileids='2013-Obama.txt')


# In[19]:


'''
from nltk.book import *
f = FreqDist(text1)
f.mostcommon(10)
'''


# In[1]:


from nltk.book import *


# In[2]:


f = FreqDist(text1)



# In[5]:


f.most_common(10)


# In[ ]:




