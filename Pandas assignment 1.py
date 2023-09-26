#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


mobiles=pd.read_csv(r"C:\Users\Surya\Desktop\Desktop\python\cleaned_all_phones.csv")


# In[4]:


mobiles


# # How many unique  mobile brands are there in the data provided

# In[5]:


mobiles["brand"].unique()


# # What is the average ram size of all the collected data
# 

# In[6]:


mobiles["ram(GB)"].mean()


# # Which phone is having the maximum and minimum battery capacity
# 

# In[7]:


a=mobiles["battery"].max()

mobiles.loc[mobiles["battery"]==a,["phone_name"]]


# # which phone is having the minimum battery?

# In[11]:


a=mobiles["battery"].min()
mobiles.loc[mobiles["battery"]==a,["phone_name"]]


# # What is the maximum battery capacity provided by Huawei Company
# 

# In[13]:


a=mobiles.loc[mobiles["brand"]=="Huawei",["battery"]].max()
a


# # Which Phone brand is providing the highest and lowest ram

# In[15]:


a=mobiles["ram(GB)"].min()
b=mobiles.loc[mobiles["ram(GB)"]==a,["phone_name","brand","ram(GB)"]]
c=mobiles["ram(GB)"].max()
d=mobiles.loc[mobiles["ram(GB)"]==c,["phone_name","brand","ram(GB)"]]
print("PHONE BRANDS WITH LOWEST RAM\n",b)
print("PHONE BRANDS WITH HIGHEST RAM\n",d)


# # How many phones has android 7.0 as there operating system

# In[17]:


print(len(mobiles.loc[mobiles["os"]=="Android 7.0",["phone_name","os"]]))
mobiles.loc[mobiles["os"]=="Android 7.0",["phone_name","os"]]


# # which is the oldest phone announced and also give the announced dates.

# In[18]:


d=mobiles["announcement_date"].min()
mobiles.loc[mobiles["announcement_date"]==d,["brand","announcement_date"]]


# # Which brand produced maximum number of phone in the given data

# In[19]:


g=mobiles.groupby("brand")
a=g[["phone_name","brand"]].count()
a.loc["Xiaomi"]


# # which brand is having least no.of phones?

# In[21]:


g=mobiles.groupby("brand")
a=g[["phone_name","brand"]].count()
a.loc["Google"]


# # how many phones supports 4k video?

# In[23]:


print(len(mobiles.loc[mobiles["video_4K"]==True,["brand","phone_name"]]))
mobiles.loc[mobiles["video_4K"]==True,["brand","phone_name"]]


# # how many phones supports 8k video?

# In[24]:


print(len(mobiles.loc[mobiles["video_8K"]==True,["brand","phone_name"]]))
mobiles.loc[mobiles["video_8K"]==True,["brand","phone_name"]]


# # How many phones supports Li-Po and Li-ion Battery

# In[26]:


a=mobiles.loc[mobiles["battery_type"]=="Li-Po",["phone_name"]].count()
b=mobiles.loc[mobiles["battery_type"]=="Li-Ion",["phone_name"]].count()
print("phones that supports Li-po battery\n",a)
print("phones that supports Li-ion battery\n",b)


# # How many sony phones supports 720x1280 resolution

# In[27]:


print(len(mobiles.loc[mobiles["resolution"]=="720x1280",["brand","phone_name"]]))
mobiles.loc[mobiles["resolution"]=="720x1280",["brand","phone_name"]]


# # Print a pivot table for finding the average weights ,total weights,based on brand and battery type

# In[28]:


pd.pivot_table(mobiles,index="brand",columns="battery_type",values=["weight(g)"],aggfunc=["mean"])


# In[29]:


mobiles


# In[ ]:




