#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np

sent = """During this period when I was drifting from door to door, job to job, friend to friend, meal to meal,
I did try nevertheless to rope off a little space for myself"""

tokens = str.split(sent)

lex = sorted(set(tokens))

', '.join(lex)


# In[3]:


num_tokens = len(token_sequence)
vocab_size = len(lex)
onehot_vectors = np.zeros((num_tokens, vocab_size), int)


# In[14]:


for i, word in enumerate(tokens):
    onehot_vectors[i, vocab.index(word)] = 1
' '.join(vocab)


# In[15]:


onehot_vectors


# In[6]:


import pandas as pd


# In[8]:


pd.DataFrame(onehot_vectors,  columns = vocab)


# In[ ]:




