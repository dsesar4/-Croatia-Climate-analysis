# (Croatia) Climate analysis

Motivation for this script is weather data visualization. There are vast amounts of weather and climate data available on Web, but it's usually just tables or synops (Ogimet). With this script you can easily visualize climate data, see bar charts with a lot of useful information and scale up weather data usage.

There are two main options for data analysis:

1. Country (14 stations) data
2. One station data

With both options you can choose:

1. Seasonal (ex. winter...) data analysis
2. Monthly (ex. january, july...) data analysis. 

The difference is that country data isn't available chronologically since it would be hard to visualize it for a lot of stations in more than one month/season. In this script there are 14 main stations available by default for Croatia in country data option. If one station data is chosen, you can insert how many years of that data you want to compare (1 - number of years available on Ogimet).

There are 13 bar charts available for instatnt visualization: 1. Precipitation, 2. Maximum temperature, 3. Minimum temperature, 4. Humidity, 5. Days with snow cover, 6. Maximum snow depth, 7. Cumulative snow cover, 8. Number of days with Tmin<-10°C, 9. Number of days with Tmax<0°C, 10. Number of days with Tmin<0°C, 11. Number of days with Tmax>25°C, 12. Number of days with Tmax>30°C, 13. Number of days with Tmin>20°C.

Script is started by running weather_analysis.py. Parameters for analysis are then manually inserted.
Init_analysis.py initializes data for analysis. Here we use Croatian 14 main weather stations.
Fethers.py get average data for each of the listed categories. That data is fetched from DHMZ official site and stored in lists.
Ogimet_fetchers.py does most of the job fetching data from Ogimet and putting it in pandas dataframes and lists.
Plotting_data.py plots your data on bar charts.

The more data or longer period, the more you wait for fetchers to get it. Usually it shouldn't take it more than 2 minutes, even for longer/bigger amounts of data analysed. 

It's possible to alter Init_analysis to get the data from other stations if you want, but after that you should also probably alter some other things, since some data is fetched with average data from DHMZ witch is later used from visualizations. But general way of fetching and visualizing Ogimet data is provided so you can build your own script if needed. 

Dont' overuse and abuse. Enjoy! :)




