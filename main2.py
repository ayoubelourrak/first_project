from pandas import read_csv

data1=read_csv('data/hotspotUrbanMobility-1.csv')
print(data1.shape)

data2=read_csv('data/hotspotUrbanMobility-2.csv')
print(data2.shape)

data1 = data1.append(data2, ignore_index=True)
print(data1.shape)

data1.to_csv('data/completeDataset.csv',index=False)

data = read_csv('data/completeDataset.csv')
print(data.describe())

data = data.drop('h24', axis=1)
data = data.loc[data['Anomalous']<1]
print(data.describe())

data.to_csv('data/preprocessedDataset.csv', index=False)
