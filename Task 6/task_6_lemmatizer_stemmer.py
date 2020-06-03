#!/usr/bin/env python
# coding: utf-8

# In[5]:

#stemming and lemmatization
#porter stemmer
import nltk
from nltk.stem import PorterStemmer
porterStemmer = PorterStemmer()
porterStemmer.stem('happiness')


# In[6]:


#18BCE0865


# In[7]:


#Porter stemmer does not work for 'happiness'


# In[8]:


from nltk.stem import LancasterStemmer
lancasterStemmer = LancasterStemmer()
lancasterStemmer.stem('happiness')


# In[9]:


#lancaster stemmer works for 'happiness'


# In[10]:


from nltk.stem import RegexpStemmer
regexpStemmer = RegexpStemmer('ing')
regexpStemmer.stem('sing')


# In[11]:


from nltk.stem import SnowballStemmer
SnowballStemmer.languages
frenchstemmer = SnowballStemmer('french')
frenchstemmer.stem('manges')


# In[12]:


len(SnowballStemmer.languages)


# In[13]:


porterStemmer.stem('porous')


# In[14]:


lancasterStemmer.stem('porous')


# In[15]:


#hahahahahah


# In[16]:


lancasterStemmer.stem('carefully')


# In[17]:


porterStemmer.stem('carefully')


# In[18]:


#clearly lancaster fails for carefully while porter succeeds


# In[19]:


lancasterStemmer.stem('dancing')


# In[20]:


porterStemmer.stem('dancing')


# In[21]:


porterStemmer.stem('purposefully')


# In[22]:


lancasterStemmer.stem('purposefully')


# In[23]:


from nltk.stem import WordNetLemmatizer


# In[32]:


lemmatizer = WordNetLemmatizer()
lemma = lemmatizer.lemmatize("dances")
print(lemma)


# In[33]:


porterStemmer.stem("dances")


# In[34]:


lancasterStemmer.stem('dances')


# In[ ]:




