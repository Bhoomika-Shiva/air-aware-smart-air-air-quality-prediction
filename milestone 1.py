import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#Create sample data

data={"Date":["2024-01-01","2024-01-02","2024-01-03","2024-01-04","2024=01-05","2024-01-06"],"PM25":[120,150,None,80,70,65],"PM10":[200,240,220,None,150,140],"NO2":[40,55,50,45,None,30],"AQI":[180,220,200,130,110,100]}

df=pd.DataFrame(data)

print("ORIGINAL DATA")
print(df)

#Preprocessing

df["Date"]=pd.to_datetime(df["Date"],errors="coerce")

#Fill the missing values with mean
df["PM25"].fillna(df["PM25"].mean(),inplace=True)
df["PM10"].fillna(df["PM10"].mean(),inplace=True)
df["NO2"].fillna(df["NO2"].mean(),inplace=True)

print("\nAFTER CLEANING")
print(df)

#Feature engineering

df["Day"]=df["Date"].dt.day
df["Weekday"]=df["Date"].dt.day_name()
   
print("\nAFTER FEATURE ENGINEERING")
print(df)

#Basic EDA

print("\nSTATISTICAL SUMMARY")
print(df.describe())

#Visualization

plt.title("PM25 Trend")
plt.plot(df["Date"],df["PM25"])
plt.xlabel("Date")
plt.ylabel("PM25")
plt.xticks(rotation=45)
plt.show()

#Machine learning model(AQI prediction)

x=df[["PM25","PM10","NO2"]]
y=df["AQI"]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

model=LinearRegression()
model.fit(x_train,y_train)

#Predict new AQI
new_data=[[100,180,40]] #example pollution values
predicted_aqi=model.predict(new_data)

print("\nPredicted AQI:",predicted_aqi[0])