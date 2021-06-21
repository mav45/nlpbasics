#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import pandas as pd


# In[31]:


sentences = """Amazon.com, Inc. engages in the retail sale of consumer products and subscriptions in North America and internationally. The company operates through three segments: North America, International, and Amazon Web Services (AWS).\n"""
sentences += """Alphabet Inc. provides online advertising services in the United States, Europe, the Middle East, Africa, the Asia-Pacific, Canada, and Latin America. The company offers performance and brand advertising services.\n"""
sentences += """Tesla, Inc. designs, develops, manufactures, leases, and sells electric vehicles, and energy generation and storage systems in the United States, China, and internationally.\n"""
sentences += """Facebook, Inc. develops products that enable people to connect and share with friends and family through mobile devices, personal computers, virtual reality headsets, and in-home devices worldwide."""


# In[32]:


corpus = {}


# In[33]:


for i, sent in enumerate(sentences.split('\n')):
    corpus['sent{}'.format(i)] = dict((tok,1) for tok in sent.split())


# In[34]:


df = pd.DataFrame.from_records(corpus).fillna(0).astype(int).T
df[df.columns[:20]]


# In[26]:


df = df.T


# In[30]:


df.sent0.dot(df.sent4)


# In[ ]:




