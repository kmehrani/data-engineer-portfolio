import pandas as pd

# Small sample dataset
data = {
    "Employee": ["Alice", "Bob", "Charlie", "Dana", "Eva"],
    "Department": ["Tech", "Finance", "Tech", "Tech", "HR"],
    "Salary": [70000, 68000, 72000, 69000, 65000]
}

df = pd.DataFrame(data)

#print info about dataFrame
#print(df.info())

#organizes min to max
#print(df.describe())

#gives mean of 'Salary'
#print(df["Salary"].mean())

#filters 'Salary' greater than 70000
#print(df[df["Salary"] > 70000])

#inserts column called 'Bonus' with 10% Salary Bonus
df.insert(3, 'Bonus', df["Salary"] * 0.10)
print(df)

#Logging Day: Today was easier than yesterday. Glad I got to touch on pandas again
#after a break
