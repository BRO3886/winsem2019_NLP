#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk


# In[2]:


from nltk.tokenize import word_tokenize


# In[18]:


sentence = "The little yellow dog barked at the big black cat"


# In[19]:

#tokenization
tokenized_sentence = word_tokenize(sentence)


# In[20]:


tokenized_sentence


# In[21]:

#pos taggging
from nltk import pos_tag


# In[22]:


pos_tagged_sentence = pos_tag(tokenized_sentence)


# In[23]:


pos_tagged_sentence


# In[24]:


grammar = "NP: {<DT>?<JJ>*<NN>}"


# In[25]:


from nltk import RegexpParser


# In[26]:


cp = nltk.RegexpParser(grammar)


# In[27]:


result = cp.parse(pos_tagged_sentence)


# In[28]:


print(result)


# In[29]:

#drawing parse tree
result.draw()


# In[30]:


from nltk.corpus import state_union


# In[32]:


from nltk.tokenize import PunktSentenceTokenizer


# In[34]:


train_text = state_union.raw("2005-GWBush.txt")


# In[35]:


train_text


# In[38]:


sample_text = state_union.raw("2006-GWBush.txt")


# In[39]:


sample_text


# In[40]:


custom_sent_tokenizer = PunktSentenceTokenizer(train_text)


# In[41]:


tokenized = custom_sent_tokenizer.tokenize(sample_text)


# In[46]:


try:
    for i in tokenized[5:]:
        words = nltk.word_tokenize(i)
        tagged = nltk.pos_tag(words)
        namedEnt = nltk.ne_chunk(tagged, binary=False)
        namedEnt.draw()
except Exception as e:
    print(str(e))


# In[ ]:




