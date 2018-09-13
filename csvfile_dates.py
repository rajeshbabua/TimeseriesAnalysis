import pandas as pd
###############the next two lines are used to uplaod fiels to cvolab if youa re using colab environment ################
from google.colab import files
uploaded =files.upload()
#####################################################
######################the file fin.csv is a stock price data downlaoded from yahoo finance 
#################"https://in.finance.yahoo.com/quote/%5ENSEI/history?period1=1505290942&period2=1536826942&interval=1d&filter=history&frequency=1d"
o1 = pd.read_csv("fin.csv", parse_dates=["Date"],index_col="Date")
type(o1.index)
o1["2018-02"].Close.mean()
o1["2018-02"].Close.mean()
o1["2018-02-07":"2018-04-10"]
o1["2018-02-07":"2018-02-07"]
o1.Open.resample('M').mean()######avg price per month
o1.Open.resample('W').mean().plot('bar')
o1.Open.resample('D').mean().plot('bar')
o1.Close.plot()
len(o1)
##########################################################################
################when your csv file ahs no dates in time series analysis
#####################dealing with pd.date_range function
##############################
import pandas as pd
import numpy as np
o = pd.read_csv("fin_nodate.csv") 
len(o)

a= pd.date_range(start='9/16/2017', end='9/1/2018',freq='B')
a
o.set_index(a,inplace=True)
o['2017-10':'2018-02'].Close.mean()
##### rearrange dataframe to consider fridays prices even to sun,sat
o.asfreq('H',method='pad')#####hourly freq
############generate business days 
rn =pd.date_range(start='1/10/2017', periods=72, freq='W')
rn

ts= pd.Series(np.random.randint(1,10,len(rn)), index= rn)
ts
