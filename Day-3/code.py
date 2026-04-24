import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = {
    "name": ["A", "B", "C", "D", "E", "F"],
    "age": [18, 20, None, 22, 19, None],
    "hours_studied": [2, 5, 3, None, 4, 6],
    "marks": [50, 80, 65, 90, None, 85],
    "city": ["Mumbai", "Delhi", "Mumbai", "Delhi", "Pune", "Mumbai"]
}

df = pd.DataFrame(data)
print(df["age"])
df['age'] = df["age"].fillna(df["age"].mean())
print(df["age"])
df['hours_studied'] = df["hours_studied"].fillna(df["hours_studied"].median())
print(df["hours_studied"])
print(df)
df= df.dropna(subset='marks')
print(df)

df['performance']= df["marks"]/df["hours_studied"]
print(df)
df['status']= pd.cut(
    df["marks"], bins = [0,70, 100],
    labels= ["fail", "pass"]
)
print(df)
print(df[(df['city']== 'Mumbai') & (df["status"]=="pass")])

print(df.groupby("city")["marks"].mean())
n= df.to_numpy() 
print(n)
x= n[:, :5]
y= n[:, 5]
print(x.shape)
print(y.shape)
# plt.scatter(df["hours_studied"], df["marks"])
# plt.xlabel("Hours Studied")
# plt.ylabel("Marks")
# plt.show()

# plt.hist(df["marks"])
# plt.show()

print(df.groupby("city")['marks'].median())

