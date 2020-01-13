######################
import pandas
data=pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data2=data*2
data2.to_csv("sampledata.txt",index=None)

######################
data1=pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data2=pandas.read_csv("http://pythonhow.com/data/sampledata_x_2.txt")
data=pandas.concat([data1,data2])
data.to_csv("mysample.txt",index=None)