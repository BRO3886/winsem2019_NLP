#!/usr/bin/env python
# coding: utf-8

# In[1]:

#stopwords such as and, their, them
from nltk.corpus import stopwords


# In[10]:


from datetime import datetime
datetime.now()


# In[2]:


stopwords.words('english')


# In[3]:


import nltk
entries = nltk.corpus.cmudict.entries()


# In[4]:


len(entries)


# In[5]:


for entry in entries:
    print(entry)


# In[7]:


stopwords.words('german')


# In[8]:


for entry in entries[0:50]:
    print(entry)


# In[11]:


from nltk.corpus import wordnet as wn
wn.synsets('motorcar')


# In[12]:


wn.synset('car.n.01').lemma_names()


# In[13]:


wn.synsets('')


# In[14]:


text = '''Daniel Wroughton Craig (born 2 March 1968) is an English actor. He trained at the National Youth Theatre and graduated from the Guildhall School of Music and Drama in 1991, before beginning his career on stage. His film debut was in the drama The Power of One (1992). Other early appearances were in the historical television war drama Sharpe's Eagle (1993), Disney family film A Kid in King Arthur's Court (1995), the drama serial Our Friends in the North (1996) and the biographical film Elizabeth (1998).'''


# In[15]:


text


# In[16]:


import nltk
texts = [text]


# In[17]:


texts


# In[23]:

#sentence and word tokenization
for text in texts:
    sentences = nltk.sent_tokenize(text)
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
    tagged_words = nltk.pos_tag(words)
print(tagged_words)


# In[27]:

#tweet by a tweleb
donald = '''All is well :D Missiles launched from Iran at two military bases located in Iraq. Assessment of casualties & damages taking place now. So far, so good! We have the most powerful and well equipped military anywhere in the world, by far! I will be making a statement tomorrow morning.'''


# In[28]:


from nltk.tokenize import TweetTokenizer


# In[29]:

#tweettokenizer recognises modern lingo
TweetTokenizer().tokenize(donald)


# In[39]:


texts = [donald]
for text in texts:
    sentences = nltk.sent_tokenize(text)
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        print(words)
        print('\n')
        tagged_words = nltk.pos_tag(words)
        print(tagged_words)
        print('\n')
print('\n')
print(sentences)


# In[53]:


from nltk.corpus import brown
news_text = brown.words(categories = 'fiction')
fdist = nltk.FreqDist(w.lower() for w in news_text)
modals =['can','could','may','might']
for m in modals:
    print(m+':',fdist[m])


# In[ ]:




