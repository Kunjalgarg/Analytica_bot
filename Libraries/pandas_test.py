import pandas as pd

data1 = {
  "name": ["Sally", "Mary", "John"],
  "age": [50, 40, 30]
}

data2 = {
  "name": ["Sally", "Peter", "Micky"],
  "age": [77, 44, 22]
}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print(df1.merge(df2,how='right'),'\n\n')

print(df1.filter(items=["names"]),'\n\n')

s = pd.Series(['Kunjal','Krishna'], name='Family')
print('Series = \n',s, '\n')

file = pd.read_csv('data.csv')
##print(file.to_string(),'\n\n')

##print('first 6 rows = \n',file.head(6),'\n\n')

##print('last 3 rows = \n',file.tail(3),'\n\n')

##print('info = \n',file.info(),'\n\n')

new_file1 = file.dropna()     #if file.dropna(inplace=True) is used then org DF is changed
##print('new file =\n',new_file1.to_string(),'\n\n')

new_file2 = file.fillna(130, inplace=True)
##print(file.duplicated())

file.drop_duplicates(inplace=True)
##print('after removing \n',file.duplicated())

print(file.corr())
