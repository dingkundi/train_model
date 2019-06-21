import pandas as pd


data = pd.read_excel("data3-31.xlsx")

data["K"] = data['E']+data["F"]
data1 = data[["H","A","B","C","E","F","DATE","TIME","K"]]
index = data1[(data1.K==0)].index.tolist()
data2 = data1.drop(index)
data2['A'] = data2['A'].map(lambda x:float(x)*100)
data3 = data2.ix[data2['A']>=80]
data4 = data3.ix[data3['A']<=20000]
index = data4[(data4.H==9)].index.tolist()
data4.loc[index,'H'] = 0
data4.loc[:,"H"] = data4.loc[:,'H'].fillna(0)
data4.loc[index,'N'] = 1
data4 = data4[['H','A','B','C','E','F','N','DATE','TIME']]
data4.loc[:,'G'] = 0

date = 1190329
train_data = data4.loc[data4['DATE']<=date]
test_data = data4.loc[data4['DATE']>date]

train_data.to_csv('../database/train.csv',index=None)
test_data.to_csv('../database/test.csv',index=None)


























































































