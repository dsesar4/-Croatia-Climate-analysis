import pandas as pd

def setting_env_many(year):
    
    if (year > 2009 and year < 2016):
        
        cities = ['Pazin', 'Rijeka', 'Senj', 'Parg', 'Ogulin', 'Zavižan', 'Gospić', \
                  'Mali Lošinj', 'Zadar', 'Šibenik', 'Split - Marjan', 'Hvar', 'Dubrovnik', \
                  'Karlovac', 'Zagreb - Maksimir', 'Zagreb - Grič', 'Varaždin', 'Križevci', 'Bjelovar', 'Sisak', 'Slavonski Brod', 'Osijek']
        
        cities_average = ['pazin', 'rijeka', 'senj', 'parg', 'ogulin', 'zavizan', 'gospic', \
                           'mali_losinj', 'zadar', 'sibenik', 'split_marjan', 'hvar', 'dubrovnik',
                           'karlovac', 'zagreb_maksimir', 'zagreb_gric', 'varazdin', 'krizevci', 'bjelovar', 'sisak', \
                           'slavonski_brod', 'osijek']
        
        stations = [14308, 14216, 14323, 14219, 14328, 14324, 14330, 14314, 14428, 14438, 14445,\
                    14447, 14472, 14232, 14240, 14236, 14246, 14248, 14253, 14244, 14370, 14284]

        
    else:
        
        cities = ['Pazin', 'Rijeka', 'Senj', 'Parg', 'Ogulin', 'Zavižan', 'Gospić', 'Knin', \
                  'Mali Lošinj', 'Zadar', 'Šibenik', 'Split - Marjan', 'Hvar', 'Dubrovnik', \
                  'Karlovac', 'Zagreb - Maksimir', 'Zagreb - Grič', 'Varaždin', 'Križevci', 'Bjelovar', 'Sisak', 'Slavonski Brod', 'Osijek']
        
        cities_average = ['pazin', 'rijeka', 'senj', 'parg', 'ogulin', 'zavizan', 'gospic', 'knin', \
                           'mali_losinj', 'zadar', 'sibenik', 'split_marjan', 'hvar', 'dubrovnik',
                           'karlovac', 'zagreb_maksimir', 'zagreb_gric', 'varazdin', 'krizevci', 'bjelovar', 'sisak', \
                           'slavonski_brod', 'osijek']
        
        stations = [14308, 14216, 14323, 14219, 14328, 14324, 14330, 14442, 14314, 14428, 14438, \
                    14445, 14447, 14472, 14232, 14240, 14236, 14246, 14248, 14253, 14244, 14370, 14284]
    
    months = ['siječanj','veljača','ožujak','travanj','svibanj','lipanj','srpanj',\
              'kolovoz','rujan','listopad','studeni','prosinac']
    
    return cities, cities_average, stations, months


def setting_env_one(ID):
    
    cities = ['Pazin', 'Rijeka', 'Senj', 'Parg', 'Ogulin', 'Zavižan', 'Gospić', 'Knin', \
              'Mali Lošinj', 'Zadar', 'Šibenik', 'Split - Marjan', 'Hvar', 'Dubrovnik', \
              'Karlovac', 'Zagreb - Maksimir', 'Zagreb - Grič', 'Varaždin', 'Križevci', 'Bjelovar', 'Sisak', 'Slavonski Brod', 'Osijek']
        
    cities_average = ['pazin', 'rijeka', 'senj', 'parg', 'ogulin', 'zavizan', 'gospic', 'knin', \
                      'mali_losinj', 'zadar', 'sibenik', 'split_marjan', 'hvar', 'dubrovnik',
                      'karlovac', 'zagreb_maksimir', 'zagreb_gric', 'varazdin', 'krizevci', 'bjelovar', 'sisak', \
                      'slavonski_brod', 'osijek']
        
    stations = [14308, 14216, 14323, 14219, 14328, 14324, 14330, 14442, 14314, 14428, 14438, \
                14445, 14447, 14472, 14232, 14240, 14236, 14246, 14248, 14253, 14244, 14370, 14284]
    
    months = ['siječanj','veljača','ožujak','travanj','svibanj','lipanj','srpanj',\
              'kolovoz','rujan','listopad','studeni','prosinac']
    
    pom = stations.index(ID)
    
    return [cities[pom]], [cities_average[pom]], months


def setting_months(season):
    
    if (season == 0):
        season_months = [1,2,12]
        yp = 'Zima'
    elif (season == 1):
        season_months = [3,4,5]
        yp = 'Proljeće'
    elif (season == 2):
        season_months = [6,7,8]
        yp = 'Ljeto'
    else:
        season_months = [9,10,11]
        yp = 'Jesen'
        
    return season_months, yp


def help_df():
    
    stations = [14308, 14216, 14323, 14219, 14328, 14324, 14330, 14314, 14428, 14438, 14445,\
                14447, 14472, 14232, 14240, 14236, 14246, 14248, 14253, 14244, 14370, 14284]

    cities = ['Pazin', 'Rijeka', 'Senj', 'Parg', 'Ogulin', 'Zavižan', 'Gospić', \
              'Mali Lošinj', 'Zadar', 'Šibenik', 'Split - Marjan', 'Hvar', 'Dubrovnik', \
              'Karlovac', 'Zagreb - Maksimir', 'Zagreb - Grič', 'Varaždin', 'Križevci', 'Bjelovar', 'Sisak', 'Slavonski Brod', 'Osijek']
   
    df_help = pd.DataFrame({'Station IDs': stations}, index = cities) 
    
    return df_help
    

