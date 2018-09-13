##########timestamp
############ period
#########timespan 
import pandas as pd
import numpy as np
s = pd.read_csv('fin.csv')
s1= pd.Period('2018')
s1.start_time
s1.end_time
pd.Period('2017-08')
d= pd.Period('2017-02-28','D')
d+1
qs= pd.Period('2017-02-12 00:00','H')
qs+pd.offsets.Hour(8)

a= pd.Period('2017Q1')
c=a+1
c.start_time
#################fiscal data for wallmart THAT STARTS FROM FEB
a= pd.Period('2017Q1', freq='Q-JAN')
a.start_time

a.asfreq('M', how='end')################convert freq
q2=pd.Period('2018Q2', freq='Q-JAN')
q2

i = pd.period_range('2011','2017', freq='Q-JAN')
i[0].start_time

