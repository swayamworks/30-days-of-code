import pandas as pd
data = {
    "name": ["A", "B", "C", "D"],
    "age": [18, 20, None, 22],
    "marks": [80, 90, 85, None]
}
df= pd.DataFrame(data)
df["performance"]= df["marks"] *1.2
#print(df[df["performance"] > 100])
#print(df.shape, df.info(), df.dtypes, df.columns )
print(df.describe())
print(df.describe(include="all"))
a=df.isnull().sum()
print(a)
print(df.drop_duplicates(inplace=True))
df["age_group"] = pd.cut(
    df["age"],
    bins=[0, 18, 60, 100],
    labels=["child", "adult", "senior"]
)
df["gender"]= ["male", "female", "male", "female"]
#encoding
print(pd.get_dummies(df, columns= ["gender"]))

# print(df["age_group"])
# df["gender"]= df['gender'].map({
#     "male": 0,
#     "female":1
# })
print(df["gender"])