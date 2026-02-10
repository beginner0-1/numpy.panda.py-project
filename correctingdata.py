import pandas as pd
import numpy as np

data = {
    "Name": ["Yuvraj", "Aman", "Kartik", "Abhey", None, "Rohit"],
    "age": [20, 21, None, 200, 19, -5],          # 200 and -5 are wrong
    "salary": [50000, None, 45000, "fifty", 48000, 52000],  # "fifty" wrong
    "city": ["Meerut", "Ghaziabad", "Meerut", None, "Delhi", "unknown"]
}

df = pd.DataFrame(data)
print(df)

#checking missing values 
print(df.isnull())
print(df.isnull().sum())

#filling missing age value with mean
df["age"]=df["age"].fillna(df["age"].mean())

#converting fifty into numberic value 
df["salary"]=pd.to_numeric(df["salary"],errors ="coerce")


#filling missing salary value with median
df["salary"]=df["salary"].fillna(df["salary"].median())


#fixing wrong age values
df.loc[df["age"]< 0,"age"]=np.nan
df.loc[df["age"]> 100,"age"]=np.nan

#filling nan age values with mean
df["age"]=df["age"].fillna(df["age"].mean())

#replacing unknown city value 
df["city"]=df["city"].replace("unknown",np.nan)

#filling the city with mode(most common city)
df["city"]=df["city"].fillna(df["city"].mode()[0])

#printing data
print(df)