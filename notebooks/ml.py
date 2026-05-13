import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split 
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import RandomForestClassifier
df=pd.read_csv('C:\\Users\\thoma\\Downloads\\cca\\data\\new.csv')
#print(df.columns)
#print(df.dtypes)

# I am dropping Unamed, ID because they are not useful for the model
df.drop(["Unnamed: 0","ID"],axis=1,inplace=True)
#print(df.columns)
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
#print(df.Date.dtypes)
#print((str(df["Date"][1]))[11:])
#print(df["Date"][1])
df["HOUR"]=df["Date"].dt.year
plt.figure(figsize=(10,6))
sns.lineplot(x="HOUR",y="Arrest",data=df)
plt.show()
df["MONTH"]=df["Date"].dt.month


