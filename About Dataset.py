#!/usr/bin/env python
# coding: utf-8

# # Project Movie Industry  Data Analysis
# ### Dataset Description
# Is the movie industry dying? is Netflix the new entertainment king? Those were the first questions that lead me to create a datasetfocused on movie revenue and analyze it over the last decades
# ### Questions
# * What are the factors that affect the company's revenues, whether by increase or decrease?

# In[1]:


# import libraries
import numpy as np
import pandas as pd 

import seaborn as sns
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib.inline', '')
#('ggplot') A color package related to the drawing, and it is selected to determine the shape of the resulting drawing
plt.style.use('ggplot') 
from matplotlib.pyplot import figure
matplotlib.rcparams['figure.figsize'] = (12, 8)


# # Data Wrangling

# In[2]:


# read in the data
df = pd.read_csv(r'E:\abdo fahmy\Data analysis\Movie Industry prog\movies.csv')
df.head()


# In[3]:


# See the shape of the data
df.shape


# In[4]:


# Information about the data
df.describe()


# In[5]:


# Information about the data
df.info()


# In[6]:


# check for duplications
df.duplicated().mean()


# In[7]:


# data lost by for loop and (isnull)
for colm in df.columns:
    value_null = np.mean(df[colm].isnull())    
    print(f"{colm} - {value_null} %")


# In[8]:


# knowledge data type
df.dtypes 


# # Data Cleaning

# In[9]:


# Fill in the blank values
df['runtime'] = df['runtime'].fillna(0) 
df['votes'] = df['votes'].fillna(0)
df['budget'] = df['budget'].fillna(0)
df['gross'] = df['gross'].fillna(0)


# In[10]:


# transformation data type
df['runtime']= df['runtime'].astype(int)
df['votes']= df['votes'].astype(int)
df['budget']= df['budget'].astype(int)
df['gross']= df['gross'].astype(int)


# In[11]:


df.dtypes 


# In[12]:


# Delete negative data
df.drop(index=5445, inplace=True)
df.drop(index=7445, inplace=True)
df.drop(index=3045, inplace=True)


# In[13]:


# Delete duplicate rows
df.drop_duplicates(inplace= True)


# In[14]:


# net profit ranking
df = df.sort_values(by=['gross'], inplace=False, ascending=False)
df.head()


# In[15]:


pd.set_option('display.max_rows', None)


# ### General look for numerical data

# In[16]:


df.hist(column=['gross','budget' ],figsize=(16,6.5),bins=25,color='MediumSeaGreen');


# * General look for numerical data gross and budget 
# * There is a very close relationship

# ## Creating Scatter Plots

# In[17]:


# Comparison between budget and total revenue
# and Creating Scatter Plots
plt.scatter(x=df['budget'], y=df['gross'], alpha=0.6, color='red')
plt.title('Comparison of budget, revenue')
plt.xlabel('budget')
plt.ylabel('gross')
plt.show()


# * There is a coefficient of correlation and relationship
# * The higher the budget, the higher the revenue

# In[18]:


# plot budget vs gross as seaborn
sns.regplot(x=df['budget'], y=df['gross'],scatter_kws={"color":"red"}, line_kws={"color":"blue"},)
plt.title('Comparison of budget,revenue', color='black');


# * Here proves the positive correlation

# In[19]:


# Consider the strength of the link
corr_matrix = df.corr(method='pearson') #--->>>> pearson, kendall, spearman )
corr_matrix


# * budget = 0.309212 , gross = 0.256331
# * There is a great interest
# * He entered with us votes --->>> 0.222427

# ## heat map

# In[20]:


# Photography by correlation budget and gross
sns.heatmap(corr_matrix, annot=True)
plt.title('Correlation matrix for Numeric Features')
plt.xlabel('Movie features')
plt.ylabel('Movie features')
plt.show();


# * Here it turned out that there is a strong positive relationship between the budget and the gross
# * And the votes affect a large percentage

# In[22]:


# transform the object to category
df_numerized = df
for colm_name in df_numerized.columns:
    if(df_numerized[colm_name].dtype == 'object'):
        df_numerized[colm_name] = df_numerized[colm_name].astype('category')
        df_numerized[colm_name] = df_numerized[colm_name].cat.codes                 
df_numerized.head()


# In[21]:


df.head()


# In[23]:


# Heat map after converting all columns to category
plt.figure(figsize=(15,8))
correlation_df = df_numerized.corr(method='pearson')
sns.heatmap(correlation_df, annot=True)
plt.title('Correlation matrix for Numeric Features')
plt.xlabel('Movie features')
plt.ylabel('Movie features')
plt.show()


# * votes affects score
# * Votes and budget affect the gross

# In[24]:


# Consider the strength of the link
df_numerized.corr()


# In[25]:


corr_mat = df_numerized.corr()
corr_price = corr_mat.unstack()
corr_price.head()


# In[26]:


corr_price.sort_values().head()


# In[27]:


high_coor = corr_price[(corr_price)> 0.5]
high_coor


# # Conclusions
# * budget = 0.309212 , gross = 0.256331 There is a great interest
# * Here it turned out that there is a strong positive relationship between the budget and the gross
# * And the votes affect a large percentage
# * votes affects score
# * Votes and budget affect the gross
# 

# # limitations of
# * Other analyzes did not give a clear relationship

# In[ ]:




