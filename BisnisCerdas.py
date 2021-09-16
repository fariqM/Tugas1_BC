#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pds


# In[2]:


import csv


# In[3]:


df = pds.read_csv('tugasPertemuan1.csv')


# In[4]:


df.head()


# In[8]:


df.hist(column='TotalPay', bins=25, grid=False, figsize=(12,8), color='#9155FD', zorder=2, rwidth=0.9)


# In[ ]:




