#!/usr/bin/env python
# coding: utf-8

# # Final Assignment Numpy

# In[1]:


import numpy as np


# In[2]:


x=np.genfromtxt(r"C:\Users\Surya\Desktop\Desktop\python\tipsf.csv",delimiter=",", skip_header=1 )


# In[3]:


x


# In[120]:


#1>what is the total bill value
totalBillvalue = x[:, 1].sum()


# In[6]:


totalBillvalue 


# In[121]:


#2>what is the total tip value

totaltipsvalue = x[:, 2].sum()


# In[122]:


totaltipsvalue


# In[127]:


#4>how many smokers are there
smoker=x[:,4]


# In[73]:


smoker


# In[77]:


h=smoker[(smoker>0)]


# In[79]:


np.sum(h)


# In[134]:


#7>what is the min and max tip given 
max=np.max(x[:, 2])
min=np.min(x[:, 2])
print("minimum tip is ",min)
print("maximum tip is ",max)


# In[136]:


#5>what is the average tip given by female and male
s=np.sum(x[:,2].take(np.where(x[:,3]==0)))
g=np.sum(x[:,2].take(np.where(x[:,3]==1)))
z=np.unique(x[:,3],return_counts=True)
q,w=z
print(s/w[0],"Avg Tip Female")
print(g/w[1],"Avg Tip Male")


# In[137]:


#3>count of how many times sun,sat,thu,fri are there.
z=np.unique(x[:,5],return_counts=True)
a,b=z
j=0
for i in a:
    if(i==0):
        print("NO of Sundays = ",b[j])
        j+=1
    elif(i==1):
        print("No of Saturdays = ",b[j])
        j+=1
    elif(i==2):
        print("No of Thursdays = ",b[j])
        j+=1
    elif(i==3):
        print("No of Fridays = ",b[j])
        j+=1  


# In[140]:


#6>how much amount have been spent by female and male.
I=np.sum(x[:,1].take(np.where(x[:,3]==0)))
J=np.sum(x[:,1].take(np.where(x[:,3]==1)))
print("Total amount spent by female: ",np.round(I))
print("Total amount spent by male: ",np.round(J))


# In[142]:


#9>find out the average size
z=np.unique(x[:,7],return_counts=True)
a,b=z
avg=np.sum(x[:,7])/np.sum(b)
print("Average of size = ",np.round(avg))


# In[145]:


#10>find how many female smokers and male smokers are there
z=np.unique(x[:,3].take(np.where((x[:,4]==1))),return_counts=True)
a,b=z
for i in a:
    if(i==0):
        print("Female smokers : ",b[0])
    else:
        print("Male smokers : ",b[1])


# In[149]:


#8>how many male and female are going for dinner and lunch
z=np.unique(x[:,3].take(np.where((x[:,6]==1))),return_counts=True)      #lunch        0 means female 1 means male
a,b=z
y=np.unique(x[:,3].take(np.where((x[:,6]==0))),return_counts=True)       #dinner
c,d=y
for i in a:
    if(i==0):
        print("Number of females going for lunch",b[0])
        print("Number of females going for dinner",d[0])
    else:
         print("Number of males going for lunch",b[1])
         print("Number of males going for dinner",d[1])


# In[176]:


m=np.genfromtxt(r"C:\Users\Surya\Desktop\Desktop\python\train_extended.csv",delimiter=",",skip_header=1)


# In[177]:


m


# In[179]:


#1>what is the maximum and minnimum length?

x=np.max(m[:,0])
print("Maximum length is ",x)
y=np.min(m[:,0])
print("Minimum length is ",y)


# In[180]:


#2>find out the difference between max and min length.

def f(x):
    return np.max(x)-np.min(x)
np.apply_along_axis(f,0,m
                    
                    [:,0])


# In[181]:


#3>find column wise average.

def f1(x):
    return np.sum(x)/200000
np.apply_along_axis(f1,0,m)
    


# In[182]:


#4>find out all the age whose height is gereater than 0.4

z=m[:,7].take(np.where(m[:,2]>0.4))
print(z.shape)
print(z)


# In[183]:


#5>what is the average height and weight of the persons whose age is greater than 10.

height=m[:,2].take(np.where(m[:,7]>10))
count=height.shape
weight=m[:,3].take(np.where(m[:,7]>10))
count1=weight.shape
l1=list(count)
l2=list(count1)
print("Average height = ",np.sum(height)/l1[1])
print("Average weight = ",np.sum(weight)/l2[1])


# In[184]:


#6>what is the shell weight

np.round(np.sum(m[:,6]))


# In[185]:


#7>how many persons belongs to each and every unique age

np.unique(m[:,7],return_counts=True)


# In[186]:


#8>what is the differemce between shucked weight and viscera weight

z=np.sum(m[:,4])
x=np.sum(m[:,5])
print("Difference between shucked weight and viscera weight = ",np.round(z-x))


# In[208]:


#9>what is the average height of the persons whose age is between 14 and 19.

x1=np.array(m[:,2].take(np.where((m[:,7]>14) & (m[:,7]<19))))
np.mean(x1)


# In[ ]:




