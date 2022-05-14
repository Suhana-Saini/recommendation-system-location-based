#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#imports
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

from geopy.geocoders import Nominatim 

import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from sklearn.cluster import KMeans

df = pd.read_csv('C:\\Users\\ASUS\\Downloads\\locations.csv', sep=',')


#geopy in action
country = 'India'
city_names = df['location']

longitude =[]
latitude =[]
geolocator = Nominatim(user_agent="Trips")

for c in city_names.values:
    location = geolocator.geocode(c+','+ country)
    latitude.append(location.latitude)
    longitude.append(location.longitude)


#finishing touches!
input_city = input("Enter a city name: ")
cluster = df.loc[df['location'] == input_city, 'loc_clusters']
cluster = cluster.iloc[0]
cluster
cities = df.loc[df['loc_clusters'] == cluster, 'location']
cities
for c in range(len(cities)):
    if cities.iloc[c] == input_city:
        continue
    else:
        print(cities.iloc[c])


# In[ ]:


#imports
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

from geopy.geocoders import Nominatim 

import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from sklearn.cluster import KMeans

df = pd.read_csv('C:\\Users\\ASUS\\Downloads\\locations.csv', sep=',')


#geopy in action
country = 'India'
city_names = df['location']

longitude =[]
latitude =[]
geolocator = Nominatim(user_agent="Trips")

for c in city_names.values:
    location = geolocator.geocode(c+','+ country)
    latitude.append(location.latitude)
    longitude.append(location.longitude)


#finishing touches!
input_city = input("Enter a city name: ")
cluster = df.loc[df['location'] == input_city, 'loc_clusters']
cluster = cluster.iloc[0]
cluster
cities = df.loc[df['loc_clusters'] == cluster, 'location']
cities
for c in range(len(cities)):
    if cities.iloc[c] == input_city:
        continue
    else:
        print(cities.iloc[c])


# In[ ]:




