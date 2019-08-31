import pandas as pd
import matplotlib.pyplot as plt
from pylab import rcParams


def plotting_bar_precip(precip_average, precip_DHMZ, cities, months, month, year, yp):
    
    precipitation_per_city = pd.DataFrame({'Prosječne oborine (mm)': precip_average,\
                                           'Oborine (mm)': precip_DHMZ}, index = cities)
    
    rcParams['figure.figsize'] = 18, 10
    precipitation_per_city.plot.bar(width=0.5, fontsize=10, rot=70)
    for i, val in enumerate(precipitation_per_city['Oborine (mm)'].values):
        plt.text(i, val, float(val), horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':14},weight='bold')
    if (max(precip_average) > max(precip_DHMZ)):
        plt.ylim(0, max(precip_average) + max(precip_average)//10)
    else:
        plt.ylim(0, max(precip_DHMZ) + max(precip_DHMZ)//10)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=18)
    plt.legend(fontsize=12)
    if (month != None):
        plt.title(months[month-1].capitalize() + ' ' + str(year) +'.', fontsize = 25)
    elif (yp == 'Zima'):
        plt.title(yp + ' ' + str(year) + '.' + '/' + str(year + 1) + '.', fontsize = 25)
    else:
        plt.title(yp + ' ' + str(year) + '.', fontsize = 25)
    plt.grid(lw=0.5)
    
def plotting_bar_data(data, data_average, cities, months, month, year, yp, name):
    
    dict_types = {"icy":["Ledeni dani","(Tmin<-10°C)"],"frosty":["Studeni dani","(Tmax<0°C)"],"cold":["Hladni dani","(Tmin<0°)"],\
                  "warm":["Topli dani","(Tmax>25°C)"],"hot":["Vrući dani","(Tmax>30°C)"]}
    
    data_per_city = pd.DataFrame({dict_types[name][0] + '  prosjek': data_average, \
                                 dict_types[name][0] + ' ' + dict_types[name][1]: data}, index = cities)
    
    rcParams['figure.figsize'] = 18, 10
    data_per_city.plot.bar(width=0.5,fontsize=10,rot=70)
    for i, val in enumerate(data_per_city[dict_types[name][0] + ' ' + dict_types[name][1]].values):
        plt.text(i, val, int(val), horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':14},weight = 'bold')
    
    if (max(data) > max(data_average)):
        plt.ylim(0, max(data) + 4)
    else:
        plt.ylim(0, max(data_average) + 4)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=18)
    plt.legend(fontsize=12)
    if (month != None):
        plt.title(months[month-1].capitalize() + ' ' + str(year) + '.', fontsize = 25)
    elif (yp == 'Zima'):
        plt.title(yp + ' ' + str(year) + '.' + '/' + str(year + 1) + '.', fontsize = 25)
    else:
        plt.title(yp + ' ' + str(year) + '.', fontsize = 25)
    plt.grid(lw=0.5)
    
def plotting_bar_data_night(data, cities, months, month, year, yp, name_type):
    
    data_types = {"night":["Tople noći (Tmin>20°C)"],"hmd":["Srednja vlažnost zraka (%)"],\
                  "max_temp":["Maksimalna temperatura (°C)"],"min_temp":["Minimalna temperatura (°C)"]}    
    data_per_city = pd.DataFrame({data_types[name_type][0]: data}, index = cities)
    
    rcParams['figure.figsize'] = 18, 10
    if (name_type == 'hmd'):
        data_per_city.plot.bar(width = 0.35,color='teal',fontsize=10,rot =70)
        plt.ylim(0, max(data) + max(data)//10)
        for i, val in enumerate(data_per_city[data_types[name_type][0]].values):
            plt.text(i, val, int(val), horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':14},weight = 'bold')
    elif (name_type == 'night'):
        data_per_city.plot.bar(width = 0.35,color='firebrick',fontsize=10,rot =70)
        plt.ylim(0, max(data) + 5)
        for i, val in enumerate(data_per_city[data_types[name_type][0]].values):
            plt.text(i, val, int(val), horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':14},weight = 'bold')
    elif(name_type == 'max_temp'):
        data_per_city.plot.bar(width = 0.35,color='orangered',fontsize=10,rot =70)
        plt.ylim(0, max(data) + 4)
        for i, val in enumerate(data_per_city[data_types[name_type][0]].values):
            plt.text(i, val, float(val), horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':14},weight = 'bold')
    else:
        data_per_city.plot.bar(width = 0.35,color='dodgerblue',fontsize=10,rot =70)
        plt.ylim(min(data) - 4, max(data) + 4)
        if ((yp != 'Ljeto' and yp != '') or month == 1 or month == 2 or month == 3 or month == 11 or month == 12):
            for i, val in enumerate(data_per_city[data_types[name_type][0]].values):
                plt.text(i, val, float(val), horizontalalignment='center', verticalalignment='top', fontdict={'fontweight':500, 'size':14},weight = 'bold')
        else:
            for i, val in enumerate(data_per_city[data_types[name_type][0]].values):
                plt.text(i, val, float(val), horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':14},weight = 'bold')

    plt.xticks(fontsize=16)
    plt.yticks(fontsize=18)
    plt.legend(fontsize=12)
    if (month != None):
        plt.title(months[month-1].capitalize() + ' ' + str(year) + '.', fontsize = 25)
    elif (yp == 'Zima'):
        plt.title(yp + ' ' + str(year) + '.' + '/' + str(year + 1) + '.', fontsize = 25)
    else:
        plt.title(yp + ' ' + str(year) + '.', fontsize = 25)
    plt.grid(lw=0.5)
    
def plotting_bar_data_snow(data, cities, months, month, year, yp, name):
    
    snow_types =  {"max":["Maksimalna visina snijega (cm)"],"cum":["Cm-dani"],\
                   "snwd":["Broj dana sa snijegom na tlu"]}
    data_per_city = pd.DataFrame({snow_types[name][0]:data}, index = cities)
    
    rcParams['figure.figsize'] = 18, 10
    data_per_city.plot.bar(width = 0.35,color='royalblue',fontsize=10,rot =70)
    for i, val in enumerate(data_per_city[snow_types[name][0]].values):
        plt.text(i, val, int(val), horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':14},weight = 'bold')

    if (name == 'cum'):
        plt.ylim(0, max(data) + max(data)//10 + 5)
    elif (name == 'max'):
        plt.ylim(0, max(data) + max(data)//15 + 5)
    else:
        plt.ylim(0, max(data) + 5)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=18)
    plt.legend(fontsize=12)
    if (month != None):
        plt.title(months[month-1].capitalize() + ' ' + str(year) + '.', fontsize = 25)
    elif (yp == 'Zima'):
        plt.title(yp + ' ' + str(year) + '.' + '/' + str(year + 1) + '.', fontsize = 25)
    else:
        plt.title(yp + ' ' + str(year) + '.', fontsize = 25)
    plt.grid(lw=0.5)
    
    
def plotting_bar_precip_yearly(precip_average, precip, years, months, month, yp, cities):
    
    for i in range(0, len(years)):
        if (yp != 'Zima'):
            years[i] = str(years[i]) + '.'
        else:
            years[i] = str(years[i]) + '.' + '/' + str(years[i]+ 1) + '.'
        
    precipitation_per_city = pd.DataFrame({'Oborine (mm)': precip}, index = years)
    if (len(precip) <= 5):
        par = 8
    elif (len(precip) > 5 and len(precip) <= 10):
        par = 12
    else:
        par = 18
    rcParams['figure.figsize'] = par, 10
    fig, ax = plt.subplots()
    precipitation_per_city.plot(kind = "bar", ax = ax, width = 0.5,color = 'dodgerblue',rot = 40)
    for i, val in enumerate(precipitation_per_city['Oborine (mm)'].values):
        plt.text(i, val, float(val), horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':14},weight='bold')
    
    if (max(precip_average) > max(precip)):
        plt.ylim(0, max(precip_average) + max(precip_average)//10)
    else:
        plt.ylim(0, max(precip) + max(precip)//10)
    plt.xticks(fontsize = 16)
    plt.yticks(fontsize = 20)
    plt.legend(fontsize=12)
    plt.axhline(precip_average, color = 'tomato')
    if (month != None):
        plt.title(cities[0] + ': ' + months[month-1], fontsize = 25)
    else:
        plt.title(cities[0] + ': ' + yp, fontsize = 25)
    plt.grid(lw=0.5)
    
def plotting_bar_data_yearly(data, data_average, years, months, month, yp, cities, name):
        
    dict_types = {"icy":["Ledeni dani","(Tmin<-10°C)"],"frosty":["Studeni dani","(Tmax<0°C)"],"cold":["Hladni dani","(Tmin<0°C)"],
                  "warm":["Topli dani","(Tmax>25°C)"],"hot":["Vrući dani","(Tmax>30°C)"]}
    
    data_per_city = pd.DataFrame({dict_types[name][0] + ' ' + dict_types[name][1]: data}, index = years)
    
    if (len(data) <= 5):
        par = 8
    elif (len(data) > 5 and len(data) <= 10):
        par = 12
    else:
        par = 18
    rcParams['figure.figsize'] = par, 10
    fig, ax = plt.subplots()
    if (name == 'icy' or name == 'frosty' or name == 'cold'):
        data_per_city.plot(kind = "bar", ax = ax, width = 0.5, color = 'royalblue', rot = 40)
        plt.axhline(data_average, color = 'tomato')
    else:
        data_per_city.plot(kind = "bar", ax = ax, width = 0.5, color = 'firebrick', rot = 40)
        plt.axhline(data_average, color = 'dodgerblue')
    for i, val in enumerate(data_per_city[dict_types[name][0] + ' ' + dict_types[name][1]].values):
        plt.text(i, val, int(val), horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':14},weight='bold')

    plt.ylim(0, max(data) + 4)
    plt.xticks(fontsize = 16)
    plt.yticks(fontsize = 20)
    plt.legend(fontsize=12)
    if (month != None):
        plt.title(cities[0] + ': ' + months[month-1], fontsize = 25)
    else:
        plt.title(cities[0] + ': ' + yp, fontsize = 25)
    plt.grid(lw=0.5)
    
def plotting_bar_data_night_yearly(data, years, months, month, yp, cities, name_type):
    
    data_types = {"night":["Tople noći (Tmin>20°C)"],"hmd":["Srednja vlažnost zraka (%)"],\
                  "max_temp":["Maksimalna temperatura (°C)"],"min_temp":["Minimalna temperatura (°C)"]} 
    data_per_city = pd.DataFrame({data_types[name_type][0]:data}, index = years)
    
    if (len(data) <= 5):
        par = 8
    elif (len(data) > 5 and len(data) <= 10):
        par = 12
    else:
        par = 18
    rcParams['figure.figsize'] = par, 10
    if (name_type == 'hmd'):
        data_per_city.plot.bar(width = 0.35,color='teal',fontsize=10,rot =40)
        plt.ylim(0, max(data) + max(data)//10)
        for i, val in enumerate(data_per_city[data_types[name_type][0]].values):
            plt.text(i, val, int(val), horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':14},weight = 'bold')
    elif (name_type == 'night'):
        data_per_city.plot.bar(width = 0.35,color='firebrick',fontsize=10,rot =40)
        plt.ylim(0, max(data) + 5)
        for i, val in enumerate(data_per_city[data_types[name_type][0]].values):
            plt.text(i, val, int(val), horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':14},weight='bold')
    elif(name_type == 'max_temp'):
        data_per_city.plot.bar(width = 0.35,color='orangered',fontsize=10,rot =40)
        plt.ylim(0, max(data) + 4)
        for i, val in enumerate(data_per_city[data_types[name_type][0]].values):
            plt.text(i, val, float(val), horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':14},weight='bold')
    else:
        data_per_city.plot.bar(width = 0.35,color='dodgerblue',fontsize=10,rot =40)
        plt.ylim(min(data) - 4, max(data) + 4)
        if ((yp != 'Ljeto' and yp != '') or month == 1 or month == 2 or month == 3 or month == 11 or month == 12):
            for i, val in enumerate(data_per_city[data_types[name_type][0]].values):
                plt.text(i, val, float(val), horizontalalignment='center', verticalalignment='top', fontdict={'fontweight':500, 'size':14},weight = 'bold')
        else:
            for i, val in enumerate(data_per_city[data_types[name_type][0]].values):
                plt.text(i, val, float(val), horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':14},weight = 'bold')

    plt.xticks(fontsize = 16)
    plt.yticks(fontsize = 20)
    plt.legend(fontsize=12)
    if (month != None):
        plt.title(cities[0] + ': ' + months[month-1], fontsize = 25)
    else:
        plt.title(cities[0] + ': ' + yp, fontsize = 25)
    plt.grid(lw=0.5)
    
def plotting_bar_data_snow_yearly(data, years, months, month, yp, cities, name):
    
    snow_types =  {"max":["Maksimalna visina snijega (cm)"],"cum":["Cm-dani"],\
                   "snwd":["Broj dana sa snijegom na tlu"]}
    data_per_city = pd.DataFrame({snow_types[name][0]: data}, index = years)
    
    if (len(data) <= 5):
        par = 8
    elif (len(data) > 5 and len(data) <= 10):
        par = 12
    else:
        par = 18
    rcParams['figure.figsize'] = par, 10
    data_per_city.plot.bar(width = 0.35,color = 'royalblue',fontsize=10,rot =40)
    for i, val in enumerate(data_per_city[snow_types[name][0]].values):
        plt.text(i, val, int(val), horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight':500, 'size':14},weight='bold')

    if (name == 'cum'):
        plt.ylim(0, max(data) + max(data)//10 + 5)
    elif (name == 'max'):
        plt.ylim(0, max(data) + max(data)//15 + 5)
    else:
        plt.ylim(0, max(data) + 5)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=20)
    plt.legend(fontsize=12)
    if (month != None):
        plt.title(cities[0] + ': ' + months[month-1], fontsize = 25)
    else:
        plt.title(cities[0] + ': ' + yp, fontsize = 25)
    plt.grid(lw=0.5)
    

