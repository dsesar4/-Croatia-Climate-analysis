import pandas as pd

def average_fetcher_monthly(month, months, cities_average):
    
    precip_average = []
    icy_average = []
    frosty_average = []
    cold_average = []
    warm_average = []
    hot_average = [] 
    
    for i in range (0, len(cities_average)):
        url = "https://meteo.hr/klima.php?section=klima_podaci&param=k1&Grad={city}".format(city=cities_average[i])
        dfs1 = pd.read_html(url)
        df1 = dfs1[0]
        df1 = df1.apply(pd.to_numeric, errors='coerce')
        precip_average.append(df1[months[month-1]].iloc[9])
        icy_average.append(df1[months[month-1]].iloc[18])
        frosty_average.append(df1[months[month-1]].iloc[19])
        cold_average.append(df1[months[month-1]].iloc[20])
        warm_average.append(df1[months[month-1]].iloc[21])
        hot_average.append(df1[months[month-1]].iloc[22])
        
    return precip_average, icy_average, frosty_average, cold_average, warm_average, hot_average


def average_fetcher_season(season_months, months, cities_average):
    
    precip_average = []
    icy_average = []
    frosty_average = []
    cold_average = []
    warm_average = []
    hot_average = [] 
    
    for j in range (0, len(cities_average)):
    
        i = season_months
            
        url = "https://meteo.hr/klima.php?section=klima_podaci&param=k1&Grad={city}".format(city=cities_average[j])
        dfs1 = pd.read_html(url)
        df1 = dfs1[0]
        df1 = df1.apply(pd.to_numeric, errors='coerce')
        
        precip_average.append(df1[months[i[0]-1]].iloc[9] + df1[months[i[1]-1]].iloc[9] + df1[months[i[2]-1]].iloc[9])
        icy_average.append(df1[months[i[0]-1]].iloc[18] + df1[months[i[1]-1]].iloc[18] + df1[months[i[2]-1]].iloc[18])
        frosty_average.append(df1[months[i[0]-1]].iloc[19] + df1[months[i[1]-1]].iloc[19] + df1[months[i[2]-1]].iloc[19])
        cold_average.append(df1[months[i[0]-1]].iloc[20] + df1[months[i[1]-1]].iloc[20] + df1[months[i[2]-1]].iloc[20])
        warm_average.append(df1[months[i[0]-1]].iloc[21] + df1[months[i[1]-1]].iloc[21] + df1[months[i[2]-1]].iloc[21])
        hot_average.append(df1[months[i[0]-1]].iloc[22] + df1[months[i[1]-1]].iloc[22] + df1[months[i[2]-1]].iloc[22])
        
    return precip_average, icy_average, frosty_average, cold_average, warm_average, hot_average


def DHMZ_precip_fetcher_monthly(year, cities, month):

    df_array = []
    url = "https://meteo.hr/klima.php?section=klima_podaci&param=k2_1&Godina={Year}".format(Year=year)
    dfs = pd.read_html(url)
    df = dfs[0]
    df.set_index('Postaja', inplace=True)
    df = df.replace("**", "0.0")
    df = df.replace("Selo", "0.0")
    df.iloc[:] = df.iloc[:].astype('float64')
    df.iloc[:] = df.iloc[:]/10
    
    for m in cities:
        df_array.append(pd.DataFrame(df.loc[m])) 
        
    precip_DHMZ = []
    
    for l in range(len(cities)):
        precip_DHMZ.append(df.loc[cities[l]][month - 1])
        
    for k in range (len(precip_DHMZ)):
        precip_DHMZ[k] = round(precip_DHMZ[k],1)
                          
    return precip_DHMZ

def DHMZ_precip_fetcher_monthly_yearly(years, cities, month):
    
    precip_DHMZ = []
    
    for i in range(0, len(years)):
        url = "https://meteo.hr/klima.php?section=klima_podaci&param=k2_1&Godina={Year}".format(Year=years[i])
        dfs = pd.read_html(url)
        df = dfs[0]
        df.set_index('Postaja', inplace=True)
        df = df.replace("**", "0.0")
        df = df.replace("Selo", "0.0")
        df.iloc[:] = df.iloc[:].astype('float64')
        df.iloc[:] = df.iloc[:]/10
        
        precip_DHMZ.append(df.loc[cities[0]][month - 1])
        
    for k in range (len(precip_DHMZ)):
        precip_DHMZ[k] = round(precip_DHMZ[k],1)
                          
    return precip_DHMZ

def DHMZ_precip_fetcher_season(year, cities, season_months):

    df_array = []
    precip_DHMZ = []
    
    if (season_months[0] != 1):
        url = "https://meteo.hr/klima.php?section=klima_podaci&param=k2_1&Godina={Year}".format(Year=year)
        dfs = pd.read_html(url)
        df = dfs[0]
        df.set_index('Postaja', inplace=True)
        df = df.replace("**", "0.0")
        df = df.replace("Selo", "0.0")
        df.iloc[:] = df.iloc[:].astype('float64')
        df.iloc[:] = df.iloc[:]/10
            
        for m in cities:
            df_array.append(pd.DataFrame(df.loc[m])) 
        
        for l in range(len(cities)):
            precip_DHMZ.append(df.loc[cities[l]][season_months[0] - 1] + df.loc[cities[l]][season_months[0]] + df.loc[cities[l]][season_months[0] + 1])
                  
    else:
        url = "https://meteo.hr/klima.php?section=klima_podaci&param=k2_1&Godina={Year}".format(Year=year+1)
        dfs = pd.read_html(url)
        df = dfs[0]
        df.set_index('Postaja', inplace=True)
        df = df.replace("**", "0.0")
        df = df.replace("Selo", "0.0")
        df.iloc[:] = df.iloc[:].astype('float64')
        df.iloc[:] = df.iloc[:]/10
    
        for m in cities:
            df_array.append(pd.DataFrame(df.loc[m]))         
    
        for l in range(len(cities)):
            precip_DHMZ.append(df.loc[cities[l]][season_months[0] - 1] + df.loc[cities[l]][season_months[0]])
        
        url = "https://meteo.hr/klima.php?section=klima_podaci&param=k2_1&Godina={Year}".format(Year=year)
        dfs = pd.read_html(url)
        df = dfs[0]
        df.set_index('Postaja', inplace=True)
        df = df.replace("**", "0.0")
        df = df.replace("Selo", "0.0")
        df.iloc[:] = df.iloc[:].astype('float64')
        df.iloc[:] = df.iloc[:]/10       
    
        for l in range(len(cities)):
            precip_DHMZ[l] = precip_DHMZ[l] + df.loc[cities[l]][season_months[2] - 1]
            
    for k in range (len(precip_DHMZ)):
        precip_DHMZ[k] = round(precip_DHMZ[k],1)
    
    return precip_DHMZ


def DHMZ_precip_fetcher_season_yearly(years, cities, season_months):
    
    precip_DHMZ = []
    
    if (season_months[0] != 1):
        for i in range(0, len(years)):
            url = "https://meteo.hr/klima.php?section=klima_podaci&param=k2_1&Godina={Year}".format(Year=years[i])
            dfs = pd.read_html(url)
            df = dfs[0]
            df.set_index('Postaja', inplace=True)
            df = df.replace("**", "0.0")
            df = df.replace("Selo", "0.0")
            df.iloc[:] = df.iloc[:].astype('float64')
            df.iloc[:] = df.iloc[:]/10
            
            precip_DHMZ.append(df.loc[cities[0]][season_months[0] - 1] + df.loc[cities[0]][season_months[0]] + df.loc[cities[0]][season_months[0] + 1])
    else:
        for i in range(0, len(years)):
            url = "https://meteo.hr/klima.php?section=klima_podaci&param=k2_1&Godina={Year}".format(Year=years[i] + 1)
            dfs = pd.read_html(url)
            df = dfs[0]
            df.set_index('Postaja', inplace=True)
            df = df.replace("**", "0.0")
            df = df.replace("Selo", "0.0")
            df.iloc[:] = df.iloc[:].astype('float64')
            df.iloc[:] = df.iloc[:]/10
            
            precip_DHMZ.append(df.loc[cities[0]][season_months[0] - 1] + df.loc[cities[0]][season_months[0]])

            url = "https://meteo.hr/klima.php?section=klima_podaci&param=k2_1&Godina={Year}".format(Year=years[i])
            dfs = pd.read_html(url)
            df = dfs[0]
            df.set_index('Postaja', inplace=True)
            df = df.replace("**", "0.0")
            df = df.replace("Selo", "0.0")
            df.iloc[:] = df.iloc[:].astype('float64')
            df.iloc[:] = df.iloc[:]/10       
            
            precip_DHMZ[i] = precip_DHMZ[i] + df.loc[cities[0]][season_months[2] - 1]
            
    for k in range (len(precip_DHMZ)):
        precip_DHMZ[k] = round(precip_DHMZ[k],1)
    
    return precip_DHMZ


        
    
                 
        
    




