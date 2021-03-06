import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy import nan
df = pd.read_csv("C:\\Excel_speech_data\\Sample.csv")
df.replace(nan,int (0),inplace = True)
train  =df[["AGE","experience"]]
plot = sns.barplot(x = "AGE",y = "experience",data=train)
plt.grid()
plt.show()
import pylab as pl
#fetching the data from the location
df = pd.read_csv("C:\\Excel_speech_data\\Sample.csv")
# df = pd.DataFrame(np.array([ENGINESIZE, CYLINDERS, FUEL CONSUMPTION]).T,
#                   columns=["ENGINESIZE", "CYLINDERS", "FUEL CONSUMPTION"])
# df.replace(nan,str(0),inplace=True)
print(df.describe())
df.fillna(value=float(0), inplace=True)
cdf = df[['AGE','Occupation','language','experience']]
#cdf['CYLINDERS'] = cdf['CYLINDERS'].map(lambda x : float(x))
# cdf.replace(nan,str(0),inplace=True)
cdf.head(9)
print(df)
print(cdf)
ax = sns.scatterplot(x="AGE", y="language", data=cdf, color = "black")
#ax.set(yticks = [0,50,100,150,200,250,300,350,400,450])
#a4_dims = (15.7, 13.27)
#fig, ax = pyplot.subplots(figsize=a4_dims)
#ax.set(
#yticks = [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,
#320,330,340,350,360,370,380,390,400,410,420,430,440,450])
plt.tight_layout()
#sns.plt.show()
#plt.yscale('log')
sns.set_context("talk")
#y = np.linspace(0,14,100)
print(ax)
vx = sns.scatterplot(x="language", y="experience", data = cdf,color = "red")
#vx.set(
#yticks = [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,
#320,330,340,350,360,370,380,390,400,410,420,430,440,450])
#xticks = [0,1,2,3,4,5,6])
#xticks = [0.0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6,2.8,3.0,3.2,3.4,3.6,3.8,4.0,4.2,4.4,4.6,4.8,5.0,
#          5.2,5.4,5.6,5.8,6.0])
#plt.xscale('log')
#sns.set_context("talk")
#y = np.linspace(0,14,100)
plt.tight_layout()
print(vx)
viz = cdf[['AGE','Occupation','language','experience']]
viz.hist()
plt.show()
msk = np.random.rand(len(cdf)) < 0.8
train = cdf[msk]
test = cdf[~msk]
nw = sns.scatterplot(x = "AGE", y = "experience",data = train, color = "yellow")
print(nw)


from sklearn import linear_model
regr = linear_model.LinearRegression()
cdf['AGE'] = cdf['AGE'].map(lambda x : float(x))
# cdf.replace(nan,int(0),inplace=True)
# train_x = np.asanyarray(train['ENGINESIZE'])
# train_y = np.asanyarray(train['CO2EMISSIONS '])
cdf['experience'] = cdf['experience'].map(lambda x : float(x))
regr.fit(X = train[['AGE', 'experience']],y = train['AGE'])
print('Coefficients:',regr.coef_)
print('Intercept:',regr.intercept_)

predicted_y = regr.predict(X=test[['AGE', 'experience']])
mse = np.average(a = (test['experience'] - predicted_y)**2)
print(mse)
scat = plt.scatter((test['experience'] - predicted_y)**2,test['experience'],color = "blue")
plt.xlabel("MSE")
plt.ylabel("language")
plt.legend(fontsize='small')
plt.grid()
plt.show()
# plot(mse,test['CO2EMISSIONS '])

print("Hi")
