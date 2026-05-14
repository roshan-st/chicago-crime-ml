import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split 
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
df=pd.read_csv('C:\\Users\\thoma\\Downloads\\cca\\data\\new.csv')
#print(df.columns)
#print(df.dtypes)

# I am dropping Unamed, ID because they are not useful for the model
df.drop(["Unnamed: 0","ID","Case Number","FBI Code","Updated On","Description","X Coordinate","Y Coordinate","Community Area","Ward","Beat","Year","Location","IUCR","Block"
         ],axis=1,inplace=True)
#print(df.columns)
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
#print(df.Date.dtypes)
#print((str(df["Date"][1]))[11:])
#print(df["Date"][1])
'''df["HOUR"]=df["Date"].dt.hour
plt.figure(figsize=(10,6))
sns.countplot(x="HOUR",hue="Arrest",data=df)
plt.show()'''
df["YEAR"]=df["Date"].dt.year
df["MONTH"]=df["Date"].dt.month
df["HOUR"]=df["Date"].dt.hour

df.drop(["Date"],axis=1,inplace=True)
df["Primary Type"]=df["Primary Type"].replace({"THEFT":0,"ROBBERY":1,"WEAPONS VIOLATION":2,"SEX OFFENSE":3,})
df=df.astype({"Primary Type":'int64'})
print(df.dtypes)




'''
#Num of Non Arrests vs Arrests
plt.figure(figsize=(10,6))
sns.countplot(x="Arrest",data=df)
plt.show()


#Crime rate by hour
plt.figure(figsize=(10,6))
sns.countplot(x="HOUR",data=df)
plt.show()

#Crime rate by monnth
plt.figure(figsize=(10,6))
sns.countplot(x="MONTH",data=df)
plt.show()

#Which crimes result more in an arrest
d=pd.crosstab(df["Primary Type"],df["Arrest"])
#print(d.head())
plt.figure(figsize=(10,6))
sns.heatmap(data=d,annot=True)
plt.show()

plt.figure(figsize=(10,6))
sns.countplot(x="District",hue="Arrest",data=df)
plt.show()


'''

top_10_locations = df["Location Description"].value_counts().head(10).index
#print(top_10_locations)

# Trying to see if there is a relationship between location and arrest rate
'''filtered_location_df = df[df["Location Description"].isin(top_10_locations)]
print(filtered_location_df)
print(filtered_location_df["Location Description"].value_counts())
print(filtered_location_df)
plt.figure(figsize=(10,6))
sns.countplot(x="Location Description",hue="Arrest",data=filtered_location_df)
plt.xticks(rotation=90)
plt.show()'''
topl = df["Location Description"].value_counts().index
topl=list(topl)
#print(len(topl))
dict1={}
for i in range(len(topl)):
    dict1[topl[i]]=i
#print(dict1)
df["Location Description"]=df["Location Description"].replace(dict1)
df=df.astype({"Location Description":'int64'})
#print(df["Location Description"].dtypes)
predict_list=["Primary Type","Location Description","District","YEAR","MONTH","HOUR","Domestic","Latitude","Longitude"]








