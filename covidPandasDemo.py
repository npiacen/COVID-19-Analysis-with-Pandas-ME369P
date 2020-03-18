# Pandas Demo
# For Pandas Lightning Talk
# Copyright Nick Piacente

import pandas as pd
import matplotlib.pyplot as plt

confirmed = pd.read_csv('time_series_19-covid-Confirmed.csv')
deaths = pd.read_csv('time_series_19-covid-Deaths.csv')
recovered = pd.read_csv('time_series_19-covid-Recovered.csv')

plot = deaths.plot(kind='bar',x='Country/Region',y='3/16/20')