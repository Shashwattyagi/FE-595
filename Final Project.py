#!/usr/bin/env python
# coding: utf-8

# In[1]:


#-----------------------loading all the required packages/libraries-----------------------#

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams

import plotly.tools as tls
import plotly.offline as py
from plotly.offline import init_notebook_mode, iplot, plot
import plotly.graph_objs as go
init_notebook_mode(connected=True)
import warnings



#----------------------- loading the dataset-----------------------#
dataset = pd.read_csv("D:/Work/Stevens Institute of Technology/SEM 3/FE 595/Final/General US info.csv", encoding='ISO-8859-1' )



#-----------------------creating a smaller vauable for city count-----------------------#
city_count = dataset.city.value_counts()



#-----------------------function to plot the cities coming up most times in the dataset-----------------------#
def show_city_frequency(number_of_city = 10):
    plot_1 = go.Histogram(
        x=dataset[dataset.city.isin(city_count[:number_of_city].index.values)]['city'],
        showlegend=False)

    ## Creating the grid for the above plot
    fig = tls.make_subplots(rows=1, cols=1)
    
    ## appending the plot on to the grid
    fig.append_trace(plot_1,1,1)

    ## displaying the figure
    fig['layout'].update(showlegend=True, title="Frequency of cities in the dataset ")
    return iplot(fig)



#-----------------------variable "number_of_city" will hold all number of city the user enters on the webpage-----------------------#
number_of_city = 20 ## here we will get the value from "number of cities" on the home page, this will give the top # of cities, by default it will be 10



#-----------------------calling the function to show the cities most in the dataset-----------------------#
show_city_frequency(number_of_city)




#-----------------------creating the lists for all the values that user want to see about the cities-----------------------#
rent , population , mortgage, salary, degree, age = [],[],[],[],[],[]



#-----------------------mapping all the values that user wants to see about the city to all the values available in the data set-----------------------#
for each in dataset.columns.values:
    if 'rent' in each:
        rent.append(each)
    if 'population' in each:
        population.append(each)
    if 'mortgage' in each:
        mortgage.append(each)
    if "salary" in each:
        salary.append(each)
    if "degree" in each:
        degree.append(each)
    if ("age" in each) and ('mortgage' not in each):
        age.append(each)

        

#-----------------------variable "city_name" will hold all the city names that user slects on the webpage-----------------------#
city_name = ['Atlantic City','Edison','Marlboro','Chicago','New York','Washinton DC','Los Vegas','Texas']  ## here we will put the list of cities that user has selected



#-----------------------creating a list of all the columns available for the value in the dataset-----------------------#        
name = 'salary' ## here we will put the value from the third drop down, by default thi is set as population

## creating list of the columns the variable "col" on the basis of what is selected on the webpage 
if name == 'rent':
    col = rent
if name == 'mortgage':
    col = mortgage
if name == 'salary':
    col = salary
if name == 'population':
    col = population
if (name == 'age'):
    col = age
if name == 'degree':
    col = degree    
    
col

#-----------------------creating TITLE for each type of plot-----------------------#                        
#city_name = ['Atlantic City','Edison','Marlboro','Chicago','New York','Washinton DC']

Title = None

if "population" in col[0]:
    Title ='POPULATION'
if "rent" in col[0]:
    Title = 'RENT'
if "salary" in col[0]:
    Title = 'FAMILY SALARY'
if "mortgage" in col[0] :
    Title = 'MORTGAGE'
if "degree" in col[0]:
    Title = 'GRADUATE RATE'
if ("age" in col[0])and ("mortgage" not in col[0]):
    Title = 'AGE'
    


#-----------------------creating BAR PLOT for the data collected-----------------------#                         
def show_bar_plot(city_name,col,Title):
    fig = tls.make_subplots(rows=1, cols=1) 
    for city in city_name:
        for each in col:
            plot = go.Bar(
                            x=dataset[dataset['city']==city]['city'],
                            y=dataset[dataset['city']==city][each]
                              ,showlegend=True
                              ,name=each + ' --- ' + city
                        )
            
            fig.append_trace(plot, 1, 1)
    fig['layout'].update( title=Title)
    return iplot(fig)

#show_bar_plot(city_name,col)



#-----------------------creating BOX PLOT for the data collected-----------------------#   
def show_box_plot(city_name,col,Title):
    fig = tls.make_subplots(rows=1, cols=1) 
    for city in city_name:
        for each in col:
            plot = go.Box(
                            x=dataset[dataset['city']==city]['city'],
                            y=dataset[dataset['city']==city][each]
                              ,showlegend=True
                              ,name=each + ' --- ' + city
                        )
            
            fig.append_trace(plot, 1, 1)
    fig['layout'].update( title=Title)
    return iplot(fig)  


#show_box_plot(city_name,col)



#-----------------------creating PLOT which user user wants on the basis of dropdown on the webpage-----------------------#  
type_graph = 'box plot' ## here we will put the value from type of graph drop down, by default it is box plot

if type_graph == 'bar plot':
    show_bar_plot(city_name,col,Title)
else: 
    show_box_plot(city_name,col,Title)                        


# In[ ]:




