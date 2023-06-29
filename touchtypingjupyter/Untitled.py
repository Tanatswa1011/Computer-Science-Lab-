#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('Touch.csv')
df.head()


# In[20]:


import pandas as pd
import plotly.express as px

df = pd.read_csv('Touch.csv')
df.head()

print(df.columns)
fig = px.bar(df, x='Words / min', y='Error Rate')
fig.show()


# Here is a data representation of my error rate according to my words per min

# In[21]:


import pandas as pd
import plotly.express as px

df = pd.read_csv('Touch.csv')
df.head()

# Check the column names in your DataFrame
print(df.columns)

# Update the column name in the px.scatter() function
fig = px.line(df, x='Date ', y='mistakes ')
fig.show()


# This data representation represents the amount of mistake I have done according to the days if we analyse it we see a huge spikes after a long time of not practicing touch typing 
