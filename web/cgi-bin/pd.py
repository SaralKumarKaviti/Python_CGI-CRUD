import pandas as pd
d=pd.read_csv('C:\\Users\\hp\\Downloads\\1.csv')
for data in d:
    #if(float(data['Cost per event, mio. USD'])>float(10)):
    print(data)
