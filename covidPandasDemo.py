# Pandas Demo
# For Pandas Lightning Talk
# Copyright Nick Piacente, David Cayll, Ziam Ghaznavi

import pandas as pd
import matplotlib.pyplot as plt

#confirmed = pd.read_csv('time_series_19-covid-Confirmed.csv')
#deaths = pd.read_csv('time_series_19-covid-Deaths.csv')
#recovered = pd.read_csv('time_series_19-covid-Recovered.csv')

deaths_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv'
confirmed_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv'
recovered_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv'

deaths = pd.read_csv(deaths_url)
confirmed = pd.read_csv(confirmed_url)
recovered = pd.read_csv(recovered_url)

usDeaths = deaths['Country/Region'] == 'US'
showDeaths = deaths[usDeaths][['Province/State', '3/20/20']]
sortedDeaths = showDeaths.sort_values( by='3/20/20', ascending=False)
top50Deaths = sortedDeaths[:50].plot(kind='bar',x='Province/State',y='3/20/20')

usconfirmed = confirmed['Country/Region'] == 'US'
showconfirmed = confirmed[usconfirmed][['Province/State', '3/20/20']]
sortedconfirmed = showconfirmed.sort_values( by='3/20/20', ascending=False)
top50confirmed = sortedconfirmed[:50].plot(kind='bar',x='Province/State',y='3/20/20')

#usRecovered = recovered['Country/Region'] == 'US'
##hasComma = ',' in deaths['Province/State']
#showRecovered = recovered[usRecovered][['Province/State', '3/20/20']]
#
#plot = showDeaths.plot(kind='bar',x='Province/State',y='3/20/20')

# added a random file