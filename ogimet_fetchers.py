import pandas as pd
import datetime as dt

def stats_ogimet_monthly(year, month, stations):
    
    start_date = dt.datetime(year, month, 1)
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    num_of_days = days_in_month[month - 1]
    if (year % 4 == 0 and month == 2):
        num_of_days = 29
    date = start_date
    
    icy = []
    frosty = []
    cold = []
    warm = []
    hot = []
    night = []
    precip = []
    max_snow = []
    cum_snow = []
    snow_days = []
    hum = []
    max_temp = []
    min_temp = []
    
    for i in range(len(stations)):
        url = 'https://www.ogimet.com/cgi-bin/gsynres?lang=en&ind={station}&ndays'\
        '={num_of_days}&ano={year}&mes={month}&day={day}&hora=18&ord=REV&Send=Send'\
        .format(year = date.year, month = date.month, day = num_of_days, \
                num_of_days = num_of_days, station = stations[i])
        dfs = pd.read_html(url, match="Daily summary")
        df = dfs[1]
        
        df = df.apply(pd.to_numeric, errors='coerce')
        
        if ('SnowDep.(cm)' in df):
            df4 = df['SnowDep.(cm)'].dropna()
            max_snow.append(df4['SnowDep.(cm)'].values.max())
            cum_snow.append(df4['SnowDep.(cm)'].values.sum())
            snow_days.append(len(df4['SnowDep.(cm)']))
        else:
            max_snow.append(0)
            cum_snow.append(0)
            snow_days.append(0)
                    
        df1 = df['Temperature(C)']['Max'].dropna()
        df2 = df['Temperature(C)']['Min'].dropna()
        icy.append(df2[df2 <= -10.0].count())
        frosty.append(df1[df1 < 0.0].count())
        cold.append(df2[df2 < 0.0].count())
        warm.append(df1[df1 >= 25.0].count())
        hot.append(df1[df1 >= 30.0].count())
        night.append(df2[df2 >= 20.0].count())
        df['Prec.(mm)'] = df['Prec.(mm)'].fillna(0.0)
        precip.append(df['Prec.(mm)'].values.sum())
        df3 = df['Hr.Avg(%)'].dropna()
        hum.append(df3.values.mean())
        max_temp.append(df1.max())
        min_temp.append(df2.min())        
    
    for j in range (len(precip)):
        precip[j] = round(precip[j],1)
        
    return icy, frosty, cold, warm, hot, night, precip, max_snow, cum_snow, snow_days, hum, max_temp, min_temp


def stats_ogimet_seasonal(year, season_months, stations):
    
    icy = [0] * len(stations)
    frosty = [0] * len(stations)
    cold = [0] * len(stations)
    warm = [0] * len(stations)
    hot = [0] * len(stations)
    night = [0] * len(stations) 
    precip = [0.0] * len(stations)
    max_snow = [0] * len(stations)
    cum_snow = [0] * len(stations)  
    snow_days = [0] * len(stations)
    hum = [0] * len(stations)
    max_temp = [-10] * len(stations)
    min_temp = [30] * len(stations)
    
    for i in season_months:
        if (i == 1 or i == 2):
            year_querry = year + 1
        else:
            year_querry = year 
        start_date = dt.datetime(year_querry, i, 1)
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        num_of_days = days_in_month[i - 1]
        if (year_querry % 4 == 0 and i == 2):
            num_of_days = 29
        date = start_date
        
        for j in range(len(stations)):
            url = 'https://www.ogimet.com/cgi-bin/gsynres?lang=en&ind={station}&ndays'\
            '={num_of_days}&ano={year}&mes={month}&day={day}&hora=18&ord=REV&Send=Send'\
            .format(year = date.year, month = date.month, day = num_of_days, \
                    num_of_days = num_of_days, station = stations[j])
            dfs = pd.read_html(url, match="Daily summary")
            df = dfs[1]
            
            df = df.apply(pd.to_numeric, errors='coerce')
            
            if ('SnowDep.(cm)' in df):
                df4 = df['SnowDep.(cm)'].dropna()
                if (df4['SnowDep.(cm)'].values.max() > max_snow[j]):
                    max_snow[j] = (df4['SnowDep.(cm)'].values.max())
                cum_snow[j] = cum_snow[j] + df4['SnowDep.(cm)'].values.sum()
                snow_days[i] = snow_days[i] + len(df4['SnowDep.(cm)'])
                               
            df1 = df['Temperature(C)']['Max'].dropna()
            df2 = df['Temperature(C)']['Min'].dropna()
            icy[j] = icy[j] + df2[df2 <= -10.0].count()
            frosty[j] = frosty[j] + df1[df1 < 0.0].count()
            cold[j] = cold [j] + df2[df2 < 0.0].count()
            warm[j] = warm[j] + df1[df1 >= 25.0].count()
            hot[j] = hot[j] + df1[df1 >= 30.0].count()
            night[j] = night[j] + df2[df2 >= 20.0].count()
            df['Prec.(mm)'] = df['Prec.(mm)'].fillna(0.0)
            precip[j] = precip[j] + df['Prec.(mm)'].values.sum()
            df3 = df['Hr.Avg(%)'].dropna()
            hum[j] = hum[j] + df3.values.mean()
            if (df1.values.max() > max_temp[j]):
                max_temp[j] = (df1.values.max())
            if (df2.values.min() < min_temp[j]):
                min_temp[j] = (df2.values.min())
            
    hum[:] = [x / 3 for x in hum]    
    for k in range (len(precip)):
        precip[k] = round(precip[k],1)
    
    return icy, frosty, cold, warm, hot, night, precip, max_snow, cum_snow, snow_days, hum, max_temp, min_temp


def stats_ogimet_monthly_yearly(years, month, stations):
    
    icy = [] 
    frosty = [] 
    cold = [] 
    warm = [] 
    hot = [] 
    night = [] 
    precip = []
    max_snow = []
    cum_snow = []
    snow_days = []
    hum = []
    max_temp = []
    min_temp = []
    
    for i in range (0, len(years)):
        year_querry = years[i] 
        start_date = dt.datetime(year_querry, month, 1)
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        num_of_days = days_in_month[month - 1]
        if (year_querry % 4 == 0 and month == 2):
            num_of_days = 29
        date = start_date    

        url = 'https://www.ogimet.com/cgi-bin/gsynres?lang=en&ind={station}&ndays'\
        '={num_of_days}&ano={year}&mes={month}&day={day}&hora=18&ord=REV&Send=Send'\
        .format(year = date.year, month = date.month, day = num_of_days, \
                num_of_days = num_of_days, station = stations[0])
        dfs = pd.read_html(url, match="Daily summary")
        df = dfs[1]
        
        df = df.apply(pd.to_numeric, errors='coerce')
                
        if ('SnowDep.(cm)' in df):
            df4 = df['SnowDep.(cm)'].dropna()
            max_snow.append(df4.values.max())
            cum_snow.append(df4.values.sum())
            snow_days.append(len(df4['SnowDep.(cm)']))
            
        else:
            max_snow.append(0)
            cum_snow.append(0)
            snow_days.append(0)

        df1 = df['Temperature(C)']['Max'].dropna()
        df2 = df['Temperature(C)']['Min'].dropna()
        icy.append(df2[df2 <= -10.0].count())
        frosty.append(df1[df1 < 0.0].count())
        cold.append(df2[df2 < 0.0].count())
        warm.append(df1[df1 >= 25.0].count())
        hot.append(df1[df1 >= 30.0].count())
        night.append(df2[df2 >= 20.0].count())
        df['Prec.(mm)'] = df['Prec.(mm)'].fillna(0.0)
        precip.append(df['Prec.(mm)'].values.sum())
        df3 = df['Hr.Avg(%)'].dropna()
        hum.append(df3.values.mean())
        max_temp.append(df1.max())
        min_temp.append(df2.min())
        
    for j in range (len(precip)):
        precip[j] = round(precip[j],1)
    
    return icy, frosty, cold, warm, hot, night, precip, max_snow, cum_snow, snow_days, hum, max_temp, min_temp


def stats_ogimet_seasonal_yearly(years, season_months, stations):
    
    icy = [0] * len(years)
    frosty = [0] * len(years)
    cold = [0] * len(years)
    warm = [0] * len(years)
    hot = [0] * len(years)
    night = [0] * len(years)
    precip = [0.0] * len(years)
    max_snow = [0] * len(years)
    cum_snow = [0] * len(years)   
    snow_days = [0] * len(years)
    hum = [0] * len(years)
    max_temp = [-10] * len(years)
    min_temp = [30] * len(years)
    
    for i in range (0, len(years)):
        for j in season_months:
            if (j == 1 or j == 2):
                year_querry = years[i] + 1
            else:
                year_querry = years[i] 
            start_date = dt.datetime(year_querry, j, 1)
            days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            num_of_days = days_in_month[j - 1]
            if (year_querry % 4 == 0 and j == 2):
                num_of_days = 29
            date = start_date            
            
            url = 'https://www.ogimet.com/cgi-bin/gsynres?lang=en&ind={station}&ndays'\
            '={num_of_days}&ano={year}&mes={month}&day={day}&hora=18&ord=REV&Send=Send'\
            .format(year = date.year, month = date.month, day = num_of_days, \
                    num_of_days = num_of_days, station = stations[0])
            dfs = pd.read_html(url, match="Daily summary")
            df = dfs[1]
            
            df = df.apply(pd.to_numeric, errors='coerce')
                        
            if ('SnowDep.(cm)' in df):
                df4 = df['SnowDep.(cm)'].dropna()
                if (df4['SnowDep.(cm)'].values.max() > max_snow[i]):
                    max_snow[i] = (df4['SnowDep.(cm)'].values.max())
                cum_snow[i] = cum_snow[i] + df4['SnowDep.(cm)'].values.sum()
                snow_days[i] = snow_days[i] + len(df4['SnowDep.(cm)'])
                           
            df1 = df['Temperature(C)']['Max'].dropna()
            df2 = df['Temperature(C)']['Min'].dropna()
            icy[i] = icy[i] + df2[df2 <= -10.0].count()
            frosty[i] = frosty[i] + df1[df1 < 0.0].count()
            cold[i] = cold [i] + df2[df2 < 0.0].count()
            warm[i] = warm[i] + df1[df1 >= 25.0].count()
            hot[i] = hot[i] + df1[df1 >= 30.0].count()
            night[i] = night[i] + df2[df2 >= 20.0].count()
            df['Prec.(mm)'] = df['Prec.(mm)'].fillna(0.0)
            precip[i] = precip[i] + df['Prec.(mm)'].values.sum()
            df3 = df['Hr.Avg(%)'].dropna()
            hum[i] = hum[i] + df3.values.mean()
            if (df1.max() > max_temp[i]):
                max_temp[i] = (df1.max())
            if (df2.min() < min_temp[i]):
                min_temp[i] = (df2.min())

    for k in range (len(precip)):
        precip[k] = round(precip[k],1)
    hum[:] = [x / 3 for x in hum]
        
    return icy, frosty, cold, warm, hot, night, precip, max_snow, cum_snow, snow_days, hum, max_temp, min_temp

