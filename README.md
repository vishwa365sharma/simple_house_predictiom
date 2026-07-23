# simple_house_predictiom
# 🏠 House Price Prediction

A Machine Learning based House Price Prediction project that predicts house prices using house area and number of bedrooms.

This project uses **Linear Regression** algorithm and is deployed using a customised **Streamlit web application**.

---

## 🚀 Project Features

- Predict house prices using Machine Learning
- Simple and interactive user interface
- Customised Streamlit design
- Real-time prediction
- Beginner-friendly ML project

---

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- Streamlit
- Pickle
- Matplotlib

---

## 📂 Project Structure

House_Price_Prediction/
│ ├── app.py                  # Streamlit application ├── model_training.py       # Model training script ├── house_model.pkl         # Trained Machine Learning model ├── house_price.csv         # Dataset ├── requirements.txt        # Required libraries └── README.md               # Project documentation


---

## 📊 Machine Learning Workflow

The complete workflow followed in this project:

1. Data Collection
2. Data Understanding
3. Data Cleaning
4. Feature Selection
5. Train-Test Split
6. Model Training
7. Model Evaluation
8. Model Deployment

---

## 📌 Features Used

| Feature | Description |
|---------|-------------|
| Area | Total house area in square feet |
| Bedrooms | Number of bedrooms |

### Target Variable

- Price

---

## 🤖 Machine Learning Model

### Linear Regression

Linear Regression is used to learn the relationship between input features and house prices.

The model predicts the estimated price based on:

- Area of house
- Number of bedrooms

---

## 📈 Model Evaluation

The model is evaluated using:

- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)

---

## ⚙️ Installation

Clone the repository:

git clone your-repository-link


Install required libraries:

pip install -r requirements.txt


▶️ Run Application
Run the Streamlit application:
streamlit run app.py


🖥️ How To Use

Open the Streamlit application
Enter house area
Enter number of bedrooms
Click on Predict Price
Get estimated house price


📦 Model Deployment

The trained model is saved using Pickle:
house_model.pkl
The Streamlit application loads this model and performs predictions.


🔮 Future Improvements

Add more features like:
Location
Bathrooms
Parking
Property type
Use advanced models:
Random Forest
XGBoost
Gradient Boosting
Improve prediction accuracy


👨‍💻 Author

Vishwa Sharma
