import pandas as pd
data={'Name':['Tom','nick','krish','jack'],'Age':[20,21,19,18]}
df=pd.DataFrame(data) 
print('Original DataFrame:')
print(df)
df['Score'] = 0
print('\nDataFrame after adding new column "Score":')
print(df)
df.loc[0,'Score']=95
df.loc[1,'Score']=85
df.loc[2,'Score']=75
df.loc[3,'Score']=65
print('\nDataFrame after updating "Score" values:')
print(df)