#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns

import matplotlib as mpl
import matplotlib.pyplot as plt
matplotlib inline


# In[2]:


import numpy as np
import pandas as pd
import seaborn as sns

import matplotlib as mpl
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


print('Matplotlib version: ', mpl.__version__)


# In[5]:


print(plt.style.available)


# In[6]:


from numpy.random import randn,randint, uniform, sample


# In[10]:


x=np.arange(0,10)
y=np.arange(11,21)
x


# In[12]:


x = np.arange(1,11)
y =  3 * x + 5
plt.title("Line plot")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.plot(x,y,  'go--', linewidth=1, markersize=5)
plt.title('line plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')


# In[19]:


x = np.arange(1,11)
y =  3 * x + 5
plt.title("Line plot")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.plot(x,y)


# In[13]:


x = np.arange(1,11)
y =  3 * x + 5
x


# In[14]:


y


# In[49]:


x = np.arange(1,11)
y =  3 * x + 5
x
plt.title("Line plot")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.plot(x,y,  'go--', linewidth=1, markersize=5)


# In[23]:


x = np.arange(0, 4 * np.pi, 0.1)
y = np.sin(x)
plt.title("sine waveform")

#plot the points using matplotlib
plt.plot(x, y, color='b')
#plt.show()


# In[25]:


x=np.arange(0,10)
y=x*x
x


# In[26]:


y


# In[27]:


plt.plot(x,y)


# In[30]:


x =np.arange(0,10)
y= 3*x + 10
#pit plot
plt.plot(x,y, 'ro--')
#plt.plot(x,y, r*, linestyle='dashed', linewidth=2, markersize=12)
plt.xlabel('x-axis', color='blue')
plt.ylabel('y-axis',color='blue')
plt.title('2d-Diagram', color='green')


# In[33]:


## creating subplots

plt.subplot(2,2,1)
plt.plot(x,y,'r--')
plt.subplot(2,2,2)
plt.plot(x,y,'g*--')
plt.subplot(2,2,3)
plt.plot(x,y,'bo')
plt.subplot(2,2,4)
plt.plot(x,y,'go')


# In[44]:


x =[1,2,3,4,5,6,7]  #days of weeks
y = [160,150,140,145,175,165,180]  #sales
plt.title("Line plot", )
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.plot(x,y,  'go--', linewidth=1, markersize=5)

#plt.plot(x,y)
#plt.show()


# In[35]:


x


# In[36]:


y


# In[37]:


plt.plot(x,y)


# In[38]:


days = [1,2,3,4,5,6,7]  #days of weeks
sales_1 = [160,150,140,145,175,165,180]  #sales of company 1
sales_2 = [70,90,160,150,140,145,175]   #sales of company 2


# In[45]:


##practice exercise : plot a line plot betweena and b:
a=np.arange(40,50)
b=np.arange(50,60)

plt.plot(a,b)
plt.show()


# In[46]:


#subplot(
#compute the x and y coordinates for points on sine and cosine curves.)
x = np.arange(0, 5 * np.pi, 0.1)


# In[ ]:




