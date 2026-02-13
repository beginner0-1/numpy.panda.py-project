import pandas as pd 
import matplotlib.pyplot as plt 

data ={
    "name": ["Yuvraj", "Aman", "Kartik", "Abhey", None, "Rohit"],
    "age": [21, 22, None, 80, 20, -5],          # 200 and -5 are wrong
    "salary": [50000, None, 45000, "fifty", 48000, 52000]
}

df =pd.DataFrame(data)
print(df)

# we will remove the row where name is missing 

df =df.dropna(subset=["name"])

#conveting salary into numeric value 

df["salary"]=pd.to_numeric(df["salary"],errors="coerce")

#fixing the missing salry with mean 

df["salary"]=df["salary"].fillna(df["salary"].mean())

#fixing age column

df["age"]=pd.to_numeric(df["age"], errors="coerce")

# removing unrealastic ages 

df=df[(df["age"] > 18 ) & (df["age"]<120)]

print("\nprinting the cleared data\n")

print(df)

plt.figure()

plt.bar(df["name"],df["salary"],color="red")

plt.title("salary comparison")
plt.xlabel("Name")
plt.ylabel("Salary")

plt.show()
