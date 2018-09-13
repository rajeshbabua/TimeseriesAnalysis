import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
d= pd.read_csv("fp.csv", index_col='Date')
#d= pd.read_csv("fp.csv", names= ['Date', 'price'],index_col='Date')
d1=d.head(15)
d1.plot()
d1.shift(-1)########shifts price value up
d1['prev_day']=d1['Open'].shift(1)##created a column 
d1['change in one day']= d1['Open']-d1['prev_day']

d1['return of 5 days']=d['Open']-d['Open'].shift(5)*100/d['Open'].shift(5)
#d1.index

########business day frequency
d1
#d1.index = pd.date_range(start='2017-09-13', periods=15, freq='B')
#d1.tshift(1)############shifting time 
