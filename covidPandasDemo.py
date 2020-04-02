# Pandas Demo
# For Pandas Lightning Talk
# Copyright Nick Piacente, David Cayll, Ziam Ghaznavi

import pandas as pd
import matplotlib.pyplot as plt
import datetime

# formatting for Jupyter Notebook
pd.options.display.max_columns = None
pd.options.display.max_rows = None

deaths_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
confirmed_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'

Deaths = pd.read_csv(deaths_url)
Confirmed = pd.read_csv(confirmed_url)

type(Confirmed)

# also works
#type(Deaths)

# formatting for Jupyter Notebook
pd.options.display.max_columns = 13
pd.options.display.max_rows = None

# get the most recent data of data
mostRecentDate = Deaths.columns[-1] # gets the columns of the matrix

# try 'Confirmed', 'Deaths'
dataName = 'Confirmed'

data = eval(dataName)

# show the data frame
data.sort_values(by=mostRecentDate, ascending = False).head(10)

# drop Lat and Long, they won't be needed
countryFrames = data.drop(['Lat','Long'], axis=1)

# save this index variable to save the order.
index = countryFrames.columns.drop(['Province/State']) 

# The pivot_table method will eliminate duplicate entries from Countries with more than one city
countryFrames.pivot_table(index = 'Country/Region', aggfunc = sum)

# formatting using a variety of methods to process and sort data
finalFrame = countryFrames.transpose().reindex(index).transpose().set_index('Country/Region').sort_values(by=mostRecentDate, ascending=False).transpose()

#try other amounts
topAmount = 10
finalFrame.iloc[:, :topAmount].plot(figsize=(15, 10), title = "Data from COVID in the Top {} Countries - {} as of {}".format(topAmount,dataName, mostRecentDate))

#date logic
month,day,year = map(int,mostRecentDate.split('/'))
dateFormatted = datetime.date(year+2000,month,day)

dateForURL = dateFormatted.strftime("%m-%d-%Y.csv") 
mostRecent_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/' + dateForURL
mostRecentFrame = pd.read_csv(mostRecent_url)

mostRecentFrame

# filters the dataframe to the criteria below.
state = 'Texas' # try others
data = 'Confirmed' # try 'Deaths', 'Recovered', and 'Active'

frameToPlot = mostRecentFrame.sort_values(by=data, ascending = False).copy()
frameToPlot.rename(columns = {'Combined_Key':'County/State','Admin2':'County'}, inplace = True)

# This creates a true/false table which filters the data
selectedState = frameToPlot['Province_State'] == (state)
selectedCountry = frameToPlot['Country_Region'] == 'US'

frameToPlot[selectedState]

####################################
########  VISUALIZE THE DATA #######
####################################

fig = plt.figure(figsize = (15,15))
fig.suptitle('COVID-19 Data in America and Abroad', size = 32)
grid_size = (15,15)

# Place A Title On The Figure
fig.text(x=0.8, y=0.05, s='Sources: John\'s Hopkins University', horizontalalignment='left')
# Overlay multiple plots onto the same axis, which spans 1 entire column of the figure
bottom_ax = plt.subplot2grid(grid_size, (7,0), colspan=15, rowspan=8)
upper_left_ax = plt.subplot2grid(grid_size, (0,0), colspan=7, rowspan=6)
upper_right_ax = plt.subplot2grid(grid_size, (0,10), colspan=7, rowspan=6)

frameToPlot[selectedState][:10].plot(ax = upper_left_ax, kind='barh', x = 'County', y = [data], title = 'Data for Counties in {}, Top 10 - {} as of {}'.format(state, data,mostRecentDate), legend = False) 
frameToPlot[selectedCountry][:20].plot(ax = upper_right_ax, kind='barh', x = 'County/State', y = [data], title = 'Data for Counties in US, Top 20 - {} as of {}'.format(data, mostRecentDate), color = 'C1', legend = False) 
finalFrame.iloc[:, :topAmount].plot(ax=bottom_ax, title = "Data from COVID in the Top {} Countries - {}".format(topAmount,dataName))

fig.savefig('COVID-19_Dashboard_{}.jpeg'.format(mostRecentDate.replace('/','_')))