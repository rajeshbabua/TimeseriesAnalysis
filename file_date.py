import pandas as pd
###############the next two lines are used to uplaod fiels to cvolab if youa re using colab environment ################
from google.colab import files
uploaded =files.upload()
#####################################################
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
