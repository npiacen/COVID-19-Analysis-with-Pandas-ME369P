# Pandas Demo
# For Pandas Lightning Talk
# Copyright Nick Piacente, David Cayll, Ziam Ghaznavi

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#confirmed = pd.read_csv('time_series_19-covid-Confirmed.csv')
#deaths = pd.read_csv('time_series_19-covid-Deaths.csv')
#recovered = pd.read_csv('time_series_19-covid-Recovered.csv')

deaths_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Deaths.csv'
confirmed_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv'
recovered_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Recovered.csv'

deaths = pd.read_csv(deaths_url)
confirmed = pd.read_csv(confirmed_url)
recovered = pd.read_csv(recovered_url)

mostRecentDate = deaths.columns[-1]

usDeaths = deaths['Country/Region'] == 'US'
showDeaths = deaths[usDeaths][['Province/State', mostRecentDate]]
sortedDeaths = showDeaths.sort_values( by=mostRecentDate, ascending=False)
top50Deaths = sortedDeaths[:50].plot(kind='bar',x='Province/State',y=mostRecentDate)

usconfirmed = confirmed['Country/Region'] == 'US'
showconfirmed = confirmed[usconfirmed][['Province/State', mostRecentDate]]
sortedconfirmed = showconfirmed.sort_values( by=mostRecentDate, ascending=False)
top50confirmed = sortedconfirmed[:50].plot(kind='bar',x='Province/State',y=mostRecentDate)

#usRecovered = recovered['Country/Region'] == 'US'
##hasComma = ',' in deaths['Province/State']
#showRecovered = recovered[usRecovered][['Province/State', '3/20/20']]
#
#plot = showDeaths.plot(kind='bar',x='Province/State',y='3/20/20')

# added a random file

import matplotlib.font_manager as fm
# Font Imports
heading_font = fm.FontProperties(fname='PlayfairDisplay-Black.ttf', size=22)
subtitle_font = fm.FontProperties(fname='Roboto-Regular.ttf', size=12)
# Color Themes
color_bg = '#FEF1E5'
lighter_highlight = '#FAE6E1'
darker_highlight = '#FBEADC'

fig = plt.figure(figsize = (15,12))
grid_size = (3,2)
hosts_to_fmt = []
# Place A Title On The Figure
fig.text(x=0.8, y=0.95, s="Sources: John's Hopkins University",fontproperties=subtitle_font, horizontalalignment='left',color='#524939')
# Overlay multiple plots onto the same axis, which spans 1 entire column of the figure
large_left_ax = plt.subplot2grid(grid_size, (0,0), colspan=1, rowspan=3)

mostRecentFrame.plot(ax=large_left_ax,
    legend=True, color=['b', 'r'], title='All Tiers')
# Second graph overlayed on the secondary y axis
large_left_ax_secondary = mostRecentFrame.plot(
    ax=large_left_ax, label='Years of Backlog', linestyle='dotted',
    legend=True, secondary_y=True, color='g')
# Adds the axis for formatting later
hosts_to_fmt.extend([large_left_ax, large_left_ax_secondary])

# For each City Tier overlay a series of graphs on an axis on the right hand column
# Its row position determined by its index
for index, tier in enumerate(draw_tiers[0:3]):
    tier_axis = plt.subplot2grid(grid_size, (index,1))
    
    mostRecentFrame.plot(ax=tier_axis,title=tier, color='b', legend=False)
    
    ax1 = mostRecentFrame.plot(ax=tier_axis,linestyle='dashed', label='Purchased Units(sq.m,City Avg)', title=tier, legend=True, color='r')  
    
    ax2 =mostRecentFrame.plot(ax=tier_axis, linestyle='dotted', label='Yuan / sq.m', secondary_y=True, legend=True, color='black')
    
    ax2.set_ylim(0,30000)
hosts_to_fmt.extend([ax1,ax2])

A = np.array(['one', 'one', 'two', 'two', 'three', 'three'])
B = np.array(['start', 'end']*3)
C = [np.random.randint(10, 99, 6)]*6
df = pd.DataFrame(zip(A, B, C), columns=['A', 'B', 'C'])
df.set_index(['A', 'B'], inplace=True)
df
