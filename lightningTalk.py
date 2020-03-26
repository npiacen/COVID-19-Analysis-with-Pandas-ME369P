#Pandas Lightning Talk Demo
#We will go over how to use pandas to import and process data related to the novel COVID-19 virus
#
#The first step is to import Pandas Also include matplotlib inline to show graphs in Pandas
#
#Copyright Nick Piacente, Ziam Ghaznavi, David Cayll

%matplotlib inline

import pandas as pd
import matplotlib.pyplot as plt

#Data Source
#Johns Hopkins University is compiling COVID-19 data from multiple sources daily. They publish the raw data on their Github page. We can find the most recent data at the link below:
#
#https://github.com/CSSEGISandData/COVID-19
#
#We can import the data related to global deaths, confirmed cases, and recovered cases using these links to their data

deaths_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
confirmed_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
Bring in data

#We can bring in data using the read_csv method. The data is now contained in a Pandas DataFrame

deaths = pd.read_csv(deaths_url)
confirmed = pd.read_csv(confirmed_url)

mostRecentDate = deaths.columns[-1] # gets the columns of the matrix

# formatting for Jupyter Notebook
pd.options.display.max_columns = 13
pd.options.display.max_rows = None

# try 'confirmed', deaths'
data = confirmed

# show the data frame
data.sort_values(by=mostRecentDate, ascending = False)

countryFrames = data.drop(['Lat','Long'], axis=1)

# formatting using a variety of methods to process and sort data
finalFrame = countryFrames.transpose().reindex(index).transpose().set_index('Country/Region').sort_values(by=mostRecentDate, ascending=False).transpose()

#try other amounts
topAmount = 20

# save this index variable to save the order.
index = countryFrames.columns.drop(['Province/State']) 

finalFrame.iloc[:, :topAmount].plot(figsize=(15, 10), title = "Deaths from COVID in the Top {} Countries".format(topAmount))

#Lets take a look at the most recent US Data
#Existing cases by day are tracked in a different CSV, labeled : 'MM-DD-YYYY.csv' in a different directory

dateForURL = '0' + mostRecentDate.replace('/','-')+ '20.csv' # will only work for a while
mostRecent_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/' + dateForURL
mostRecentFrame = pd.read_csv(mostRecent_url)

# filters the dataframe to the criteria below. Try 'China'or 'Canada'
state = 'US' # try others
data = 'Deaths' # try 'Deaths', 'Recovered', and 'Active'
selectedCountry = mostRecentFrame['Country_Region'] == (state)
hasData = mostRecentFrame[data] > 0

mostRecentFrame[selectedCountry & hasData].sort_values(by=data, ascending = False)

_[:30].plot(kind='bar', x='Combined_Key', y = data, figsize=(15, 10), title = '{} - COVID-19 in {}'.format(data,state))