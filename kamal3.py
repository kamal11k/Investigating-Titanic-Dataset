
# coding: utf-8

# The **RMS TITANIC** was a British passenger ship .The sinking of this ship is one of the most infamous shipwrecks in history.  On April 15, 1912, during her maiden voyage, it sank after colliding with an iceberg, killing 1502 out of 2224 passengers and crew. This sensational tragedy shocked the international community and led to better safety regulations for ships.
# 
# One of the reasons that the shipwreck led to such loss of life was that there were not enough lifeboats for the passengers and crew. Although there was some element of luck involved in surviving the sinking, some groups of people were more likely to survive than others.
# ![](http://static.bbc.co.uk/history/img/ic/640/images/resources/histories/titanic.jpg)

# 
# Now lets analyse the people who were more likely to survive .Here we can arise some questions
# * What is the percentage of male and female survived ?
# * Did Age play role in their survival ?
# * Which class passengers were more likely to survive?
# * What was the ticket fare for survivers and victims?
# 

# In[1]:

#imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic('matplotlib inline')


# In[2]:

# Loading data set

titanic=pd.read_csv('https://d17h27t6h515a5.cloudfront.net/topher/2016/September/57e9a84c_titanic-data/titanic-data.csv')


# In[3]:

#Showing first 5 rows in the dataset

titanic.head()


# In[4]:

titanic.shape


# As we see we have data about 891 passengers .However according to [wikipedia](https://en.wikipedia.org/wiki/RMS_Titanic) the no of passengers were 2224 .But we will consider this amount of dataset .So lets come to the first question i.e  
# ### What is the percentage of male and female survived ?

# In[5]:

#Categorising male and female we can get their ratios respectively

titanic.groupby('Sex').size()


# As we can see the no of *male* passengers is considerably higher than that of *females*.
# Now lets see **"how much male and female survived?"**

# In[6]:

titanic.groupby('Sex').Survived.sum()


# ###### As we can see the percentage of male survived is only 19% and  that of female is 74%. From this we can expect that the females were rescued with higher priority than males thats why the male survivers are very fewer than that of males. Lets plot to get a better view .

# In[7]:

ax=sns.barplot(titanic.Sex,titanic.Survived)
ax.set_title('Survival based on sex')


# Now lets come to the next question i.e **Did Age play role in their survival ?**

# Lets first see if there is any null values

# In[8]:

titanic.isnull().sum()


# #### Handling missing values

# In[9]:

#lets first exclude the rows with null Age

Removed_nullAge=titanic.dropna(subset=['Age'],axis=0)


# In[10]:

ax=sns.distplot(Removed_nullAge.Age)
ax.set_title('Distribution of age')
ax.set(ylabel='Survival Percentage',xlabel='Age')


# Now we can say most passengers are under age 20 to 40 .Now lets categorise the passengers into age groups so that we can analyse the survival according to different age groups.

# In[11]:

age_bins = [1, 15, 30, 45, 60, 80]
age_labels = ["Child","Young", "Middle-aged", "Senior", "Old"]
Removed_nullAge['Age_cat']=pd.cut(Removed_nullAge.Age,age_bins, labels=age_labels, 
    right=True, include_lowest=True)


# In[12]:

#Calculating the no of people survived
Removed_nullAge.groupby('Age_cat').Survived.sum()


# In[13]:

ax=sns.barplot(data=Removed_nullAge,x='Age_cat',y='Survived')
ax.set(ylabel='Survival Rate')
ax.set_title('Survival Rate based on age group')
sns.plt.show()


# 
# 
# 
# ##### The intresting thing is we can see the survival nuber of children is very high i.e greater than 60% where as the survival no of other groups are less 35% . Here we can say that both children and women were rescued first  .
# 
# 
# Now let move to the next question **"Which class passengers were more likely to survive?"**

# In[14]:

#grouping the dataset according to Pclass

titanic.groupby('Pclass').size()


# In[15]:

#t=titanic.groupby('Pclass').Survived.sum()
#plotting the mean of survival according to Pclass
ax=sns.barplot(titanic.Pclass,titanic.Survived)
ax.set_title('Survival Rate based on age group')
sns.plt.show()


# ###### Here we can see the survival of first class passengers is very high .whereas the number of 2nd class passengers is fewer and the survival no. of 3rd class passengers is the lowest .So we can expect the passengers of higher class were rescued with higher prioity than that of the lower ones which causes such a result .
# 
# 
# Now lets move to the next question i.e **"What was the ticket fare for survivers and victims?"** .Lets first see how the ticket price was varrying with Pclass

# In[16]:

#calculating mean of fares according to Pclass

titanic.groupby('Pclass').Fare.mean()


# In[17]:

#plotting the mean fare according to Pclass

ax=sns.barplot(titanic.Pclass,titanic.Fare)
ax.set_title('Fare based on Pclass')
sns.plt.show()


# ##### As we can see the mean fare rate of first class passengers was extremely high than that of the others .It shows they must be rich family or businessmen .That is why their survival rate was high as they were rescued with high priority .
# 
# 
# Now lets see if there were people having journey with no fare --

# In[18]:

# people going free of cost
titanic.loc[titanic.Fare==0,:].Name


# ##### When I googled all these names I found most of them are staffs or got pass to travel .Now lets see How many of them were lucky enough to get survived.

# In[19]:

ax=titanic.loc[titanic.Fare==0,:].groupby('Survived').size().plot(kind='pie')
ax.set_title('0 representing passengers who died')


# #### So  only a single person survived out of all others who were travelling free .So  we can say their journey was free of cost but the consequence was overpriced.
# 
# 

# ## Conclusion :

# #### After all the analysis we can say that the survival rate of female was significantly higher than the male passengers . And also we can say the Child aged passengers also had a higher survival rate than others . Also we found that the passengers in Pclass had a very high survival rate.
# 
# #### In the last observation we found that the passenger with free ticket had a less chance of survival which can be considered as a correlation but not a causation .
# 
# #### The main conclusion about the analysis is that the data set is not a good sample to perform some analysis and made conclusions about the population. Various issue and limitation with the dataset or report are :
# 
# * We did our analysis only taking 40% people into account which could have an effect in our analysis
# 
# 
# * The dataset has alot of missing value related to Age which may produce different trend.Its just that we dont know how it will affect
# 
# 
# * We haven't analysed the passenger survival based on cabin in which they stayed.
# 
# 
# 
