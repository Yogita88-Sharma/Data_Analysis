#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import matplotlib.pyplot as plt
import warnings
from matplotlib import style
warnings.filterwarnings("ignore")


# In[18]:


df=pd.read_csv("air.csv")
df.head()


# In[19]:


# Print dataset shape
df.shape


# In[20]:


# dataset's basic info
df.info()


# In[21]:


# All the columns name of dataset
df.columns


# In[22]:


# number of columns in dataset
len(df.columns)


# In[23]:


# basic statistic about every numerical columns data
df.describe()


# In[24]:


# boolean array of null data
df.isnull()


# In[25]:


# Null vallues in each column
df.isnull().sum()


# In[26]:


# percentage of values that are Null in column
df.isnull().sum()*100/len(df)


# In[27]:


#filling empty cells

data=pd.read_csv("air.csv")

x = data["PM2.5"].mean()
data["PM2.5"].fillna(x, inplace = True)

x1 = data["PM10"].mean()
data["PM10"].fillna(x1, inplace = True)

x2 = data["NO"].mean()
data["NO"].fillna(x2, inplace = True)

x3 = data["NO2"].mean()
data["NO2"].fillna(x3, inplace = True)

x4 = data["NOx"].mean()
data["NOx"].fillna(x4, inplace = True)

x5 = data["NH3"].mean()
data["NH3"].fillna(x5, inplace = True)

x6 = data["CO"].mean()
data["CO"].fillna(x6, inplace = True)

x7 = data["SO2"].mean()
data["SO2"].fillna(x7, inplace = True)

x8 = data["O3"].mean()
data["O3"].fillna(x8, inplace = True)

x9 = data["Benzene"].mean()
data["Benzene"].fillna(x9, inplace = True)

x10 = data["Toluene"].mean()
data["Toluene"].fillna(x10, inplace = True)

x11 = data["Xylene"].mean()
data["Xylene"].fillna(x10, inplace = True)

x12 = data["AQI"].mean()
data["AQI"].fillna(x12, inplace = True)

data.drop_duplicates(inplace = True)

print('data with no null values')
#drop in last column is it could gentrate errors future
data=data.drop("AQI_Bucket",axis=1)
print(data)
#properly arranges the date and and saves it Air2.csv without index
data['Date'] = pd.to_datetime(data['Date'])
data.to_csv("Air2.csv",index=False)


# In[28]:


# Extracting all the cities in dataset
all_Cities = df['City'].unique()
all_Cities


# In[29]:


# Number of cities in dataset
len(all_Cities)


# In[30]:


# Air quality ratings
df['AQI_Bucket'].unique()


# In[31]:


# Number of days when Ahmedabad had Very Bad air quality
very_Poor_Air_Ahmedabad = df[ (df['City']=='Ahmedabad') & (df['AQI_Bucket']=='Very Poor')]
len(very_Poor_Air_Ahmedabad)


# In[32]:


# City with the best air quality in past 
city_Data_List = []
for city in all_Cities:
    city_Data_List.append(df[ (df['City']==city) & (df['AQI_Bucket']=='Good')])
    
city_Data_List = list(map(lambda x:len(x),city_Data_List))
all_Cities[city_Data_List.index(max(city_Data_List))]


# In[33]:


df1=pd.read_csv("Air2.csv",index_col=None)


#creates a new dataframe
newdf=pd.DataFrame()
newdf=df1.copy()
print(newdf)
#newdf.plot()
#gets all the columns other then the date and year
newdf_column=list(newdf.columns[2:])
print(newdf_column)

#adds a new column named Year
newdf["Year"]=newdf["Date"].str[:4].astype('int32')

#sort the data according to years
t2015=newdf.loc[newdf['Year']==2015]
t2016=newdf.loc[newdf['Year']==2016]
t2017=newdf.loc[newdf['Year']==2017]
t2018=newdf.loc[newdf['Year']==2018]
t2019=newdf.loc[newdf['Year']==2019]
t2020=newdf.loc[newdf['Year']==2020]


Year=pd.DataFrame()
Year["Year"]=[2015,2016,2017,2018,2019,2020]
#gets the mean of the every column
for i in newdf_column :
    Year[i]=[t2015[i].mean(),t2016[i].mean(),t2017[i].mean(),t2018[i].mean(),t2019[i].mean(),t2020[i].mean()]

print(Year)
#indexing the column year
Year.set_index('Year',inplace=True)


# <h1>Analysis of the gases through out the years </h1>

# In[34]:


#ploting everything
plot_len=len(list(Year.columns))


plt.figure(figsize=(15,28))

plt.tight_layout()

font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 18,
        }

plt.style.use('ggplot')
for key,value in enumerate(list(Year.columns)) :
    plt.subplot(int(plot_len/2),int(plot_len/4),key+1)
    plt.plot(Year[value],c='red')
    plt.title(value,fontdict=font)


# <h1>Analysis of the gases in every city through out the year</h1>

# In[35]:


df1=pd.read_csv("Air2.csv",index_col=None)
#create the new dataframe
newdf=pd.DataFrame()
newdf=df1.copy()
#newdf.plot()
#gets all the columns other then the date and year
newdf_column=list(newdf.columns[2:])
newdf["Year"]=newdf["Date"].str[:4].astype('int32')
#print(newdf)
#gets the name of cities
cities=set(newdf['City'])
#gets the years
years=set(newdf['Year'])

per_year=[]
cnt=0
#processing Data and storing it in the list in following manner
# list[0][0]= name of gas
#list[0][1]=dataframe of the gas with the cities being columns and years being index
for gas in newdf_column:
    City=pd.DataFrame()
    for year in years:
        for city in cities:
            City.loc[city,year]=newdf.loc[(newdf['Year']==year) & (newdf['City']==city)][gas].mean()
    per_year.append([])
    per_year[cnt].append(gas)
    per_year[cnt].append(City)
    cnt+=1


# In[36]:


#note this might not work with matplotlib :)
for i in range(len(pd.DataFrame(per_year[0][1]).columns)):
    pd.DataFrame(per_year[0][1]).plot.bar(title=per_year[i][0])


# In[ ]:




