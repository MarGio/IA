# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 13:21:30 2018

@author: mario
"""

# Importing the libraries
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(color_codes=True)
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('C:/Users/mario/OneDrive/Documentos/iris.csv')
dataset.head()

print(dataset.shape)

# more info on the data
print(dataset.info())

# descriptions
print(dataset.describe())

# class distribution
print(dataset.groupby('species').size())


from pandas.plotting import scatter_matrix
# Using seaborn pairplot to see the bivariate relation between each pair of features
sns.pairplot(dataset, hue="species")




#Create 3 DataFrame for each Species
setosa=dataset[dataset['species']=='setosa']
versicolor =dataset[dataset['species']=='versicolor']
virginica =dataset[dataset['species']=='virginica']

print(setosa.describe())
print(versicolor.describe())
print(virginica.describe())

#for each Species ,let's check what is petal and sepal distibutuon
plt.figure()
fig,ax=plt.subplots(1,2,figsize=(18, 10))

setosa.plot(x="sepal_length", y="sepal_width", kind="scatter",ax=ax[0],label='setosa',color='r')
versicolor.plot(x="sepal_length",y="sepal_width",kind="scatter",ax=ax[0],label='versicolor',color='b')
virginica.plot(x="sepal_length", y="sepal_width", kind="scatter", ax=ax[0], label='virginica', color='g')

setosa.plot(x="petal_length", y="petal_width", kind="scatter",ax=ax[1],label='setosa',color='r')
versicolor.plot(x="petal_length",y="petal_width",kind="scatter",ax=ax[1],label='versicolor',color='b')
virginica.plot(x="petal_length", y="petal_width", kind="scatter", ax=ax[1], label='virginica', color='g')


ax[0].set(title='Sepal comparasion ', ylabel='sepal-width')
ax[1].set(title='Petal Comparasion',  ylabel='petal-width')
ax[0].legend()
ax[1].legend()


plt.figure()
fig,ax=plt.subplots(1,2,figsize=(18, 10))

setosa.plot(x="sepal_length", y=0, kind="scatter",ax=ax[0],label='setosa',color='r')
versicolor.plot(x="sepal_length",y=1,kind="scatter",ax=ax[0],label='versicolor',color='b')
virginica.plot(x="sepal_length", y=2, kind="scatter", ax=ax[0], label='virginica', color='g')


ax[0].set(title='Sepal comparasion ', ylabel='sepal-width')

ax[0].legend()

# plt.show()
# plt.close()

#satosa   - satosa Petal are relatively smaller than rest of species .can be easily separable from rest of Species 
#versicolor & virginica are also separable in Petal comprasion
#satoa sepal are smallest in length and largest in Width than other species