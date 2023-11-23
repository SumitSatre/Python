#!/usr/bin/env python
# coding: utf-8

# In[100]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn import metrics


# In[101]:


df=pd.read_csv("weight-height.csv")


# In[102]:


df.columns


# In[103]:


df.isna()


# In[104]:


df.tail()


# In[105]:


print(df.to_string())


# In[106]:


df.shape


# In[107]:


df.dtypes


# In[108]:


print(df.duplicated())


# In[109]:


X=df.iloc[:,1:2]
Y=df.iloc[:,2]


# In[110]:


X


# In[111]:


Y


# In[112]:


X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2)


# In[113]:


X_train


# In[114]:


X_test


# In[115]:


Y_train


# In[116]:


Y_test


# In[117]:


reg=LinearRegression()


# In[118]:


reg.fit(X_train,Y_train)


# In[119]:


y_pred=reg.predict(X_test)


# In[120]:


y_pred


# In[121]:


print(reg.coef_)


# In[122]:


print(reg.intercept_)


# In[123]:


plt.scatter(X_test,Y_test)
plt.plot(X_test,y_pred,color="red")
plt.show()


# In[125]:


print("Mean Squerd Error ",metrics.mean_squared_error(Y_test,y_pred))


# In[126]:


print("Mean absolute Error ",metrics.mean_absolute_error(Y_test,y_pred))


# In[127]:


print("R-squered Error ",reg.score(X_train,Y_train))


# In[ ]:




