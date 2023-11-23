#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix , accuracy_score ,classification_report
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import seaborn as sns


# In[2]:


df=pd.read_csv('Admission_Predict.csv')


# In[3]:


df.columns


# In[4]:


#it removes the extra space between the Columns name
df.columns = df.columns.str.rstrip()


# In[5]:


df.columns


# In[6]:


df.shape


# In[7]:


df.head()


# In[8]:


#Here we set the chance of admit in the 0 and 1 formate

df.loc[df['Chance of Admit']>0.75,'Chance of Admit']=1
df.loc[df['Chance of Admit']<0.75,'Chance of Admit']=0


# In[9]:


df


# In[10]:


#input variable
x=df.iloc[:,1:7]
y=df.iloc[:,8]


# In[11]:


y.value_counts()


# In[12]:


y=y.astype('int')


# In[13]:


sns.countplot(x=y)


# In[14]:


xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.25)


# In[15]:


xtrain.shape


# In[16]:


xtest.shape


# In[17]:


xtest


# In[18]:


ytrain.shape


# In[19]:


ytrain


# In[20]:


ytest.shape


# In[21]:


model = DecisionTreeClassifier(criterion='entropy')


# In[22]:


model.fit(xtrain,ytrain)


# In[23]:


y_pred=model.predict(xtest)


# In[24]:


y_pred


# In[25]:


print(accuracy_score(ytest,y_pred))


# In[26]:


result=pd.DataFrame({
    'actual':ytest,
    'predicted':y_pred
})


# In[27]:


result


# In[28]:


print(classification_report(ytest,y_pred))


# In[29]:


matrix = confusion_matrix(ytest,y_pred)
print("Confusion Matrix is :",matrix)


# In[30]:


sns.heatmap(matrix,annot=True)


# In[31]:


new=[[334,117,5,4.0,4.5,9.07]]
model.predict(new)[0]


# In[32]:


from sklearn.tree import plot_tree
import matplotlib.pyplot as plt


# In[35]:


plt.figure(figsize=(16,12))
plot_tree(model,fontsize=8,filled=True,rounded=True,class_names=['0','1'],feature_names=df.columns)


# In[ ]:





# In[ ]:




