import numpy as np
import pandas as pd
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
df = pd.read_csv('ncr_ride_bookings.csv')
##print(df.head())
##print(df.tail())
##print(df.info())
##print(df.describe())
##print(df.isnull().sum())
##print(df.duplicated().sum())
##print(df.dtypes)
##print(df.shape)
##print(df.columns)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Time'] = pd.to_datetime(df['Time'], format='%H:%M:%S', errors='coerce').dt.time
daily_stats = df.groupby('Date').agg({'Booking ID':'count', 'Booking Value':'sum'}).reset_index()
plt.figure(figsize=(12,5))
plt.plot(daily_stats['Date'], daily_stats['Booking ID'], label="Total Rides", color='darkblue')
plt.plot(daily_stats['Date'], daily_stats['Booking Value'], label="Total Revenue", color='darkgreen')
plt.title("Daily Rides & Revenue")
plt.xlabel("Date")
plt.ylabel("Count / Revenue")
plt.legend()
plt.grid(True)
##plt.show()

plt.figure(figsize=(7,5))
sns.countplot(x='Booking Status', data=df, palette='viridis')
plt.title("Booking Status Distribution")
plt.ylabel("Number of Rides")
plt.xticks(rotation=45)
##plt.show()

plt.figure(figsize=(7,5))
sns.countplot(x='Vehicle Type', data=df, order=df['Vehicle Type'].value_counts().index, palette='coolwarm')
plt.title("Vehicle Type Distribution")
plt.xticks(rotation=45)
##plt.show()

top_pickups = df['Pickup Location'].value_counts().head(10)
top_drops = df['Drop Location'].value_counts().head(10)

fig, axes = plt.subplots(1, 2, figsize=(14,5))
sns.barplot(x=top_pickups.values, y=top_pickups.index, ax=axes[0], palette='Blues_r')
axes[0].set_title("Top 10 Pickup Locations")
sns.barplot(x=top_drops.values, y=top_drops.index, ax=axes[1], palette='Greens_r')
axes[1].set_title("Top 10 Drop Locations")
plt.tight_layout()
##plt.show()

fig, axes = plt.subplots(1, 2, figsize=(14,5))
sns.countplot(y='Reason for cancelling by Customer', data=df, order=df['Reason for cancelling by Customer'].value_counts().index, ax=axes[0], palette='Reds')
axes[0].set_title("Customer Cancellation Reasons")
sns.countplot(y='Driver Cancellation Reason', data=df, order=df['Driver Cancellation Reason'].value_counts().index, ax=axes[1], palette='Oranges')
axes[1].set_title("Driver Cancellation Reasons")
plt.tight_layout()
##plt.show()

fig, axes = plt.subplots(1, 2, figsize=(12,5))
sns.histplot(df['Driver Ratings'], bins=10, kde=True, ax=axes[0], color='darkblue')
axes[0].set_title("Driver Ratings Distribution")
sns.histplot(df['Customer Rating'], bins=10, kde=True, ax=axes[1], color='darkgreen')
axes[1].set_title("Customer Ratings Distribution")
plt.tight_layout()
##plt.show()

num_cols = ['Avg VTAT', 'Avg CTAT', 'Booking Value', 'Ride Distance', 'Driver Ratings', 'Customer Rating']
plt.figure(figsize=(8,6))
sns.heatmap(df[num_cols].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
##plt.show()

df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Time'] = pd.to_datetime(df['Time'], format='%H:%M:%S', errors='coerce')

# Extract useful date & time features
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df['Hour'] = df['Time'].dt.hour
df['Minute'] = df['Time'].dt.minute

# Drop original date/time columns
df = df.drop(columns=['Date', 'Time'])

# Fill missing values
df = df.fillna("Unknown")

# Encode categorical variables
label_encoders = {}
for col in df.columns:
    if df[col].dtype == 'object' or isinstance(df[col].iloc[0], str):
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].astype(str))
        label_encoders[col] = le

# Define features & target
target_col = "Booking Status"
X = df.drop(target_col, axis=1)
y = df[target_col]

# Scale numeric features
scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

models = {
    "Logistic Regression": LogisticRegression(max_iter=500),
    "Decision Tree": DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier(),
    "Naive Bayes": GaussianNB(),
    "SVM": SVC(),
    "KNN": KNeighborsClassifier()
}

# Try importing XGBoost if available
try:
    from xgboost import XGBClassifier
    models["XGBoost"] = XGBClassifier(eval_metric='mlogloss')
except ImportError:
    print("XGBoost not installed, skipping...")

# Train & evaluate
accuracies = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds) * 100
    accuracies[name] = round(acc, 2)

# Show results
results_df = pd.DataFrame(list(accuracies.items()), columns=["Model", "Accuracy (%)"])
print(results_df)

plt.figure(figsize=(8,5))
sns.barplot(x="Accuracy (%)", y="Model", data=results_df, palette="viridis")
plt.title("Model Accuracies on Uber Booking Status Prediction")
plt.xlabel("Accuracy (%)")
plt.ylabel("Model")
plt.show()
