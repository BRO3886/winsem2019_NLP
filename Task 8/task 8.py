#!/usr/bin/env python
# coding: utf-8

# In[1]:


def gender_features(word):
    return {'last_letter':word[-1]}


# In[2]:


gender_features('Obama')


# In[3]:


from nltk.corpus import names


# In[4]:


names.words()


# In[11]:


labeled_names  = ([(name,'male')for name in names.words('male.txt')] + [(name,'female') for name in names.words('female.txt')]) 


# In[12]:


labeled_names


# In[13]:


import random
random.shuffle(labeled_names)


# In[14]:


featureSets = [(gender_features(n),gender) for (n,gender) in labeled_names]


# In[15]:


featureSets


# In[16]:


len(featureSets)


# In[37]:


train_set, test_set = featureSets[:5560], featureSets[5560:]


# In[38]:


len(train_set)


# In[39]:


len(test_set)


# In[40]:


from nltk import NaiveBayesClassifier


# In[42]:


classifier = NaiveBayesClassifier.train(train_set)


# In[55]:


classifier.classify(gender_features('Siddhartha'))


# In[56]:


classifier.classify(gender_features('Kenisha'))


# In[58]:


classifier.classify(gender_features('harbhajan'))


# In[63]:


classifier.show_most_informative_features()


# In[67]:


from nltk import word_tokenize


# In[72]:


from nltk.corpus import inaugural


# In[74]:



inaugural.fileids()


# In[75]:


inaugural.words(fileids = '2009-Obama.txt')


# In[79]:


words = inaugural.words(fileids = '2009-Obama.txt')


# In[80]:


words


# In[81]:


len(words)


# In[84]:


x = ''
for word in words:
    x=x+' '+word


# In[85]:


x


# In[86]:


token = word_tokenize(x)


# In[87]:


token


# In[ ]:




