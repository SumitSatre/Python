#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# DATA PREPROCESSING

# In[2]:


df=pd.read_csv('heart.csv')


# In[3]:


df


# In[4]:


df.isna()


# In[5]:


df.isna().sum()


# In[6]:


df=df.fillna(df.mean())


# In[7]:


df.mean()


# In[8]:


df


# In[9]:


df.head()


# In[10]:


df.tail()


# In[11]:


df=df.astype({'oldpeak':'int'})


# In[12]:


df


# In[13]:


print(df.to_string())


# In[14]:


print(df.iloc[10:25,2:7])


# In[15]:


df.shape


# In[16]:


df.dtypes


# In[17]:


df['age'].mean()


# In[18]:


(df==0).sum()


# In[19]:


print(df.iloc[:,0:1])


# In[20]:


df['age']


# FINISH DATA PROCESSING

# Train Test Spliting

# In[21]:


col=df[['age','sex','cp','trestbps','chol']]


# In[22]:


col


# In[23]:


X=df.drop('target',axis='columns')


# In[24]:


X


# In[25]:


Y=df['target']


# In[26]:


Y


# In[27]:


from sklearn.model_selection import train_test_split


# In[28]:


X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.25)


# In[29]:


X_train


# In[30]:


X_train.shape


# In[31]:


X_test


# In[32]:


X_test.shape


# In[33]:


Y_train


# In[34]:


Y_train.shape


# In[35]:


Y_test


# In[36]:


Y_test.shape


# In[37]:


from sklearn.linear_model import LogisticRegression


# In[38]:


Reg=LogisticRegression()


# In[39]:


Reg.fit(X_train,Y_train)


# In[40]:


y_pred=Reg.predict(X_test)


# In[41]:


y_pred


# In[42]:


from sklearn.metrics import accuracy_score


# In[43]:


print(accuracy_score(Y_test,y_pred))


# In[44]:


from sklearn.metrics import classification_report


# In[45]:


from sklearn.metrics import confusion_matrix


# In[46]:


import seaborn as sns


# In[47]:


print(classification_report(Y_test,y_pred))


# In[48]:


print(confusion_matrix(Y_test,y_pred))
sns.heatmap(confusion_matrix(Y_test,y_pred),annot=True)


# In[ ]:




