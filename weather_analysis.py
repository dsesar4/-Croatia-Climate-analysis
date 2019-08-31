import pandas as pd
import matplotlib.pyplot as plt

from pylab import rcParams
rcParams['figure.figsize'] = 15, 10

from init_analysis import *
from fetchers import *
from plotting_data import *
from ogimet_fetchers import *

month = None
season = None

print('\nWelcome to climate analysis for Croatia! Please enter following data: ')
b = int(input('One station(0) or group of major stations(1)? '))
if (b == 0):
    hdf = help_df()
    print('\n', hdf)    
    stat = int(input('Insert station ID: '))
    start_year = int(input('Insert starting year: '))
    num_of_years = int(input('Insert number of years: '))
    years = []
    for k in range (0, num_of_years):
        years.append(start_year + k)
    cities, cities_average, months = setting_env_one(stat)
    stations = [stat]
else:
    year = int(input('Year: '))
    cities, cities_average, stations, months = setting_env_many(year)
c = int(input('Seasonal(0) or monthly(1) analysis? '))
if (c == 0):
    season = int(input('Season: winter(0), spring(1), summer(2) or autumn(3)? '))
else:
    month = int(input('Month(by number): '))
print('\nThank you! Now please wait for analysis to finish!')

yp = ''

if (c == 0 and b == 1):    
    
    season_months, yp = setting_months(season)
    data_length, yp = setting_months(season)
    
    precip_average_season, icy_average_season, frosty_average_season, cold_average_season, warm_average_season, hot_average_season = average_fetcher_season(season_months, months, cities_average)
    icy_season, frosty_season, cold_season, warm_season, hot_season, night_season, precip_season, max_snow_season, cum_snow_season, snow_days_season, hum_season, max_temp_season, min_temp_season = stats_ogimet_seasonal(year, season_months, stations)
    
    if (year > 2010):    
        precip_DHMZ_season = DHMZ_precip_fetcher_season(year, cities, season_months)
        plotting_bar_precip(precip_average_season, precip_DHMZ_season, cities, months, month, year, yp)
    
    else:
        plotting_bar_precip(precip_average_season, precip_season, cities, months, month, year, yp)
    
    plotting_bar_data_night(max_temp_season, cities, months, month, year, yp, "max_temp")
    plotting_bar_data_night(min_temp_season, cities, months, month, year, yp, "min_temp")
    plotting_bar_data_night(hum_season, cities, months, month, year, yp, 'hmd')
       
    snd = str(input('Print snowy data(y/n)? '))
    tmd = str(input('Print day-type stats(y/n)? '))
    
    if (snd == 'y'):
        plotting_bar_data_snow(snow_days_season, cities, months, month, year, yp, "snwd")
        plotting_bar_data_snow(max_snow_season, cities, months, month, year, yp, "max")
        plotting_bar_data_snow(cum_snow_season, cities, months, month, year, yp, "cum")
        
    if (tmd == 'y'):
        plotting_bar_data(icy_season, icy_average_season, cities, months, month, year, yp, "icy")
        plotting_bar_data(frosty_season, frosty_average_season, cities, months, month, year, yp, "frosty")
        plotting_bar_data(cold_season, cold_average_season, cities, months, month, year, yp, "cold")
        plotting_bar_data(warm_season, warm_average_season, cities, months, month, year, yp, "warm")
        plotting_bar_data(hot_season, hot_average_season, cities, months, month, year, yp, "hot")
        plotting_bar_data_night(night_season, cities, months, month, year, yp, 'night')      
        
    print('\nStart script again for more insights!')

    
    
elif (c == 1 and b == 1):  
    
    data_length = [month]

    precip_average_month, icy_average_month, frosty_average_month, cold_average_month, warm_average_month, hot_average_month = average_fetcher_monthly(month, months, cities_average)
    icy_month, frosty_month, cold_month, warm_month, hot_month, night_month, precip_month, max_snow_month, cum_snow_month, snow_days_month, hum_month, max_temp_month, min_temp_month = stats_ogimet_monthly(year, month, stations)
    
    if (year > 2010):    
        precip_DHMZ_month = DHMZ_precip_fetcher_monthly(year, cities, month)
        plotting_bar_precip(precip_average_month, precip_DHMZ_month, cities, months, month, year, yp)
    
    else:
        plotting_bar_precip(precip_average_month, precip_month, cities, months, month, year, yp)

    plotting_bar_data_night(max_temp_month, cities, months, month, year, yp, "max_temp")
    plotting_bar_data_night(min_temp_month, cities, months, month, year, yp, "min_temp")
    plotting_bar_data_night(hum_month, cities, months, month, year, yp, 'hmd')
    
    snd = str(input('Print snowy data(y/n)? '))
    tmd = str(input('Print day-type stats(y/n)? '))
    
    if (snd == 'y'):
        plotting_bar_data_snow(snow_days_month, cities, months, month, year, yp, "snwd")
        plotting_bar_data_snow(max_snow_month, cities, months, month, year, yp, "max")
        plotting_bar_data_snow(cum_snow_month, cities, months, month, year, yp, "cum")
        
    if (tmd == 'y'):
        plotting_bar_data(icy_month, icy_average_month, cities, months, month, year, yp, "icy")
        plotting_bar_data(frosty_month, frosty_average_month, cities, months, month, year, yp, "frosty")
        plotting_bar_data(cold_month, cold_average_month, cities, months, month, year, yp, "cold")
        plotting_bar_data(warm_month, warm_average_month, cities, months, month, year, yp, "warm")
        plotting_bar_data(hot_month, hot_average_month, cities, months, month, year, yp, "hot")
        plotting_bar_data_night(night_month, cities, months, month, year, yp, 'night')
  
    print('\nStart script again for more insights!')


elif (c== 0 and b == 0):
    
    season_months, yp = setting_months(season)
    data_length, yp = setting_months(season)
    
    precip_average_season, icy_average_season, frosty_average_season, cold_average_season, warm_average_season, hot_average_season = average_fetcher_season(season_months, months, cities_average)
    icy_season, frosty_season, cold_season, warm_season, hot_season, night_season, precip_season, max_snow_season, cum_snow_season, snow_days_season, hum_season, max_temp_season, min_temp_season = stats_ogimet_seasonal_yearly(years, season_months, stations)
 
    if (years[0] > 2010):    
        precip_DHMZ_season = DHMZ_precip_fetcher_season_yearly(years, cities, season_months)
        plotting_bar_precip_yearly(precip_average_season, precip_DHMZ_season, years, months, month, yp, cities)
    
    else:
        plotting_bar_precip_yearly(precip_average_season, precip_season, years, months, month, yp, cities)
    
    plotting_bar_data_night_yearly(max_temp_season, years, months, month, yp, cities, "max_temp")
    plotting_bar_data_night_yearly(min_temp_season, years, months, month, yp, cities, "min_temp")
    plotting_bar_data_night_yearly(hum_season, years, months, month, yp, cities, 'hmd')

    snd = str(input('Print snowy data(y/n)? '))
    tmd = str(input('Print day-type stats(y/n)? '))
    
    if (snd == 'y'):
        plotting_bar_data_snow_yearly(snow_days_season, years, months, month, yp, cities, "snwd")
        plotting_bar_data_snow_yearly(max_snow_season, years, months, month, yp, cities, "max")
        plotting_bar_data_snow_yearly(cum_snow_season, years, months, month, yp, cities, "cum")
        
    if (tmd == 'y'):
        plotting_bar_data_yearly(icy_season, icy_average_season, years, months, month, yp, cities, "icy")
        plotting_bar_data_yearly(frosty_season, frosty_average_season, years, months, month, yp, cities, "frosty")
        plotting_bar_data_yearly(cold_season, cold_average_season, years, months, month, yp, cities, "cold")
        plotting_bar_data_yearly(warm_season, warm_average_season, years, months, month, yp, cities, "warm")
        plotting_bar_data_yearly(hot_season, hot_average_season, years, months, month, yp, cities, "hot")
        plotting_bar_data_night_yearly(night_season, years, months, month, yp, cities, 'night')
        
    print('\nStart script again for more insights!')
    
else:
    
    data_length = [month]
    precip_average_month, icy_average_month, frosty_average_month, cold_average_month, warm_average_month, hot_average_month = average_fetcher_monthly(month, months, cities_average)
    icy_month, frosty_month, cold_month, warm_month, hot_month, night_month, precip_month, max_snow_month, cum_snow_month, snow_days_month, hum_month, max_temp_month, min_temp_month = stats_ogimet_monthly_yearly(years, month, stations)
    
    if (years[0] > 2010):    
        precip_DHMZ_month = DHMZ_precip_fetcher_monthly_yearly(years, cities, month)
        plotting_bar_precip_yearly(precip_average_month, precip_DHMZ_month, years, months, month, yp, cities)
    
    else:
        plotting_bar_precip_yearly(precip_average_month, precip_month, years, months, month, yp, cities)

    plotting_bar_data_night_yearly(max_temp_month, years, months, month, yp, cities, "max_temp")
    plotting_bar_data_night_yearly(min_temp_month, years, months, month, yp, cities, "min_temp")
    plotting_bar_data_night_yearly(hum_month, years, months, month, yp, cities, 'hmd')    

    snd = str(input('Print snowy data(y/n)? '))
    tmd = str(input('Print day-type stats(y/n)? '))
    
    if (snd == 'y'):
        plotting_bar_data_snow_yearly(snow_days_month, years, months, month, yp, cities, "snwd")
        plotting_bar_data_snow_yearly(max_snow_month, years, months, month, yp, cities, "max")
        plotting_bar_data_snow_yearly(cum_snow_month, years, months, month, yp, cities, "cum")
        
    if (tmd == 'y'):
    
        plotting_bar_data_yearly(icy_month, icy_average_month, years, months, month, yp, cities, "icy")
        plotting_bar_data_yearly(frosty_month, frosty_average_month, years, months, month, yp, cities, "frosty")
        plotting_bar_data_yearly(cold_month, cold_average_month, years, months, month, yp, cities, "cold")
        plotting_bar_data_yearly(warm_month, warm_average_month, years, months, month, yp, cities, "warm")
        plotting_bar_data_yearly(hot_month, hot_average_month, years, months, month, yp, cities, "hot")
        plotting_bar_data_night_yearly(night_month, years, months, month, yp, cities, 'night')

    print('\nStart script again for more insights!')
    









