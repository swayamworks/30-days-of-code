
# Your tasks:
# Fill missing values (correct method, not random)
# Bin age into groups
# Encode city properly
# Create a column: rich (income > 45000)
# Filter: only adults who are rich


import pandas as pd

df = pd.DataFrame({
    "age": [15, 25, None, 70],
    "income": [20000, 50000, 40000, None],
    "city": ["Mumbai", "Delhi", "Mumbai", "Chennai"]
})

# Fill missing values
df["age"] = df["age"].fillna(df["age"].mean())
df["income"] = df["income"].fillna(df["income"].mean())

# Binning
df["age_groups"] = pd.cut(
    df["age"],
    bins=[0,18,60,100],
    labels=["kid","adult","senior"],
    right=False
)

# Encoding
df = pd.get_dummies(df, columns=["city"])

# Feature creation
df["rich"] = df["income"] > 45000

# Filtering
result = df[(df["age_groups"] == "adult") & (df["rich"])]

print(result)