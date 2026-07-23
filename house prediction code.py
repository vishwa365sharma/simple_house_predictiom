
# =====================================
# HOUSE PRICE PREDICTION
# Linear Regression (2 Features)
# =====================================

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from google.colab import files

# Load Dataset
Uploaded = files.upload()
df = pd.read_excel("house_price.xlsx")

print(df.head())

print(df.info())

print(df.describe())


# Features and Target
X = df[["sqft_living", "bedrooms"]]
y = df["price"]


# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Model Training
model = LinearRegression()

model.fit(X_train, y_train)


# Prediction
y_pred = model.predict(X_test)


# Evaluation
print("R2 Score :", r2_score(y_test, y_pred))

print("MAE :", mean_absolute_error(y_test, y_pred))

print("MSE :", mean_squared_error(y_test, y_pred))


# Sample Prediction
new_house = pd.DataFrame({
    "sqft_living":[2000],
    "bedrooms":[3]
})

prediction = model.predict(new_house)

print("Predicted Price :", prediction[0])


# Actual vs Predicted Plot
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted")
plt.show()
