import pandas as pd

data = {'Name' : ['Sarim', 'John', 'Bob', 'Alice', 'Jim', 'Tim'],
'Age': [30, 43, 16, 21, 28, 27]
}

df = pd.DataFrame(data)

print(df.head())
print(df.columns)

