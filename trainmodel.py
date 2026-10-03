import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Column names
cols = [
    'age', 'workclass', 'fnlwgt', 'education', 'education_num',
    'marital_status', 'occupation', 'relationship', 'race',
    'sex', 'capital_gain', 'capital_loss', 'hours_per_week',
    'native_country', 'income'
]

# Load dataset
df = pd.read_csv(
    'data/adult.data',
    header=None,
    names=cols,
    skipinitialspace=True
)

print("Dataset Shape:", df.shape)

# Replace ? with NaN
df.replace('?', np.nan, inplace=True)

# Fill missing values
for col in df.columns:
    if df[col].dtype == object:
        df[col] = df[col].fillna(df[col].mode()[0])

# Encode ALL categorical columns
label_encoders = {}

categorical_cols = [
    'workclass',
    'education',
    'marital_status',
    'occupation',
    'relationship',
    'race',
    'sex',
    'native_country',
    'income'
]

for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str))
    label_encoders[col] = le

print("\nAfter Encoding:\n")
print(df.dtypes)

# Features and Target
X = df.drop('income', axis=1)
y = df['income']

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Random Forest Model
rf = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

rf.fit(X_train, y_train)

# Prediction
y_pred = rf.predict(X_test)

# Accuracy
acc = accuracy_score(y_test, y_pred)

print("\nRandom Forest Accuracy:", acc)

# Save model
joblib.dump(rf, "model.pkl")

print("\nModel Saved Successfully!")