import pandas as pd
import numpy as np 


df = pd.read_csv('data/diabetes.csv')


df['Glucose'] = df['Glucose'].replace(0, np.nan) # if there is a 0 that that will be replaced with the avarege 
df['Glucose'] = df['Glucose'].fillna(df['Glucose'].mean())

df['BloodPressure'] = df['BloodPressure'].replace(0, np.nan)
df['BloodPressure'] = df['BloodPressure'].fillna(df['BloodPressure'].mean())

df['SkinThickness'] = df['SkinThickness'].replace(0, np.nan)
df['SkinThickness'] = df['SkinThickness'].fillna(df['SkinThickness'].mean())

df['Insulin'] = df['Insulin'].replace(0, np.nan)
df['Insulin'] = df['Insulin'].fillna(df['Insulin'].mean())

df['BMI'] = df['BMI'].replace(0, np.nan)
df['BMI'] = df['BMI'].fillna(df['BMI'].mean())


x = df[['BMI', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'Pregnancies', 'DiabetesPedigreeFunction', 'Age']] #everything exapt the outcome
y = df['Outcome'] # outcome


print(df['Glucose'] == 0)
print(df['BloodPressure'] == 0)
print(df['SkinThickness'] == 0)
print(df['Insulin'] == 0)
print(df['BMI'] == 0)