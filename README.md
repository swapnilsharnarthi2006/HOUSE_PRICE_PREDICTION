# 🏠 House Price Prediction

A Machine Learning project that predicts house prices using the California Housing dataset.

This project demonstrates an end-to-end Machine Learning workflow, starting from data understanding and preprocessing to model training, evaluation, prediction, and deployment as a Flask web application.

---

## 📌 Project Overview

House prices depend on several factors such as income, house age, number of rooms, population, and geographical location.

In this project, different Machine Learning regression algorithms are trained and evaluated to predict house prices. The best-performing model is then saved and integrated into a web application.

The application allows users to enter house-related information and receive a predicted house price.

---

## 🎯 Objectives

- Understand and clean the dataset
- Perform Exploratory Data Analysis (EDA)
- Perform feature engineering
- Split the dataset into training and testing sets
- Apply feature scaling
- Train multiple regression models
- Evaluate model performance
- Compare different models
- Select the best-performing model
- Save the trained model
- Save the feature scaler
- Build a prediction pipeline
- Create a Flask web application
- Connect the Machine Learning model with a web interface

---

## 📊 Dataset

This project uses the **California Housing dataset**.

### Features

| Feature | Description |
|---|---|
| `MedInc` | Median income of households |
| `HouseAge` | Median age of houses |
| `AveRooms` | Average number of rooms |
| `AveBedrms` | Average number of bedrooms |
| `Population` | Population of the area |
| `AveOccup` | Average household occupancy |
| `Latitude` | Latitude of the location |
| `Longitude` | Longitude of the location |

### Target Variable

`MedHouseVal` — Median house value.

---

## 🧠 Machine Learning Workflow

```text
Dataset
   ↓
Data Understanding
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Feature Engineering
   ↓
Train/Test Split
   ↓
Feature Scaling
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Model Comparison
   ↓
Best Model Selection
   ↓
Model Saving
   ↓
Prediction
   ↓
Flask Web Application
```

---

# 📚 Project Notebooks

### 01 — Data Understanding

`notebooks/01_Data_Understanding.ipynb`

Activities include:
- Loading the dataset
- Checking dataset shape
- Viewing columns
- Checking data types
- Understanding the target variable
- Checking basic statistics
- Checking missing values
- Understanding the dataset structure

### 02 — Data Cleaning

`notebooks/02_Data_Cleaning.ipynb`

Activities include:
- Handling missing values
- Checking duplicate records
- Cleaning the dataset
- Preparing the cleaned dataset
- Saving the processed dataset

### 03 — Exploratory Data Analysis

`notebooks/03_EDA.ipynb`

Activities include:
- Distribution analysis
- Feature analysis
- Correlation analysis
- Visualization
- Understanding relationships between features and house prices

### 04 — Feature Engineering

`notebooks/04_Feature_Engineering.ipynb`

Activities include:
- Selecting useful features
- Preparing input features
- Separating features and target
- Train/test splitting
- Feature scaling

### 05 — Model Training

`notebooks/05_Model_training.ipynb`

Models include:
- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor

The models are evaluated using:
- MAE
- MSE
- RMSE
- R² Score

### 06 — Prediction

`notebooks/06_Prediction.ipynb`

This notebook demonstrates how the saved model and scaler can be used to make predictions on new data.

---

# 🤖 Machine Learning Models

## 1. Linear Regression

Provides a simple baseline model for predicting continuous values.

## 2. Decision Tree Regressor

Uses a tree-based structure to learn relationships between input features and the target variable.

## 3. Random Forest Regressor

Random Forest combines multiple decision trees to produce a stronger prediction model.

```python
RandomForestRegressor(
    n_estimators=100,
    random_state=42
)
```

Random Forest was selected as the best-performing model for this project.

## 4. Gradient Boosting Regressor

Builds models sequentially to improve prediction performance.

---

# 📈 Model Evaluation

The models were evaluated using four main metrics.

### MAE — Mean Absolute Error

Measures the average absolute difference between actual and predicted values.

Lower MAE is better.

### MSE — Mean Squared Error

Measures the average squared difference between actual and predicted values.

Lower MSE is better.

### RMSE — Root Mean Squared Error

The square root of MSE.

Lower RMSE is better.

### R² Score

Measures how well the model explains the variation in the target variable.

Higher R² is generally better.

---

# 🏆 Model Performance

The selected Random Forest model achieved:

| Metric | Score |
|---|---:|
| MAE | 0.3278 |
| MSE | 0.2559 |
| RMSE | 0.5059 |
| R² Score | 0.8047 |

### Best Model

**Random Forest Regressor**

### R² Score

**0.8047**

The model explains approximately **80.47% of the variation** in the target values on the evaluation data.

---

# 💾 Saved Machine Learning Artifacts

The trained model and scaler are saved in the `models` directory.

```text
models/
├── random_forest_model.pkl
└── Scaler.pkl
```

- `random_forest_model.pkl` — trained Random Forest regression model
- `Scaler.pkl` — feature scaler used during model training

> **Note:** The trained `.pkl` model is kept locally because the model file is larger than GitHub's standard 100 MB individual file limit.

---

# 🌐 Web Application

A Flask web application was created to make the trained Machine Learning model accessible through a web interface.

```text
app/
├── app.py
├── static/
│   └── style.css
└── templates/
    └── index.html
```

## 🔄 Web Application Workflow

```text
User
 ↓
HTML Form
 ↓
Flask Backend
 ↓
Receive User Input
 ↓
Create DataFrame
 ↓
Load Scaler
 ↓
Scale Input Features
 ↓
Load Random Forest Model
 ↓
Generate Prediction
 ↓
Display Predicted Price
```

## 🖥️ Web Application Features

Users can enter:
- Median Income
- House Age
- Average Rooms
- Average Bedrooms
- Population
- Average Occupancy
- Latitude
- Longitude

The application processes the input and returns the predicted house price.

---

# 📁 Project Structure

```text
HOUSE-PRICE-PREDICTION/
│
├── app/
│   ├── app.py
│   ├── static/
│   │   └── style.css
│   └── templates/
│       └── index.html
│
├── data/
│   ├── processed/
│   │   └── housing_clean.csv
│   └── raw/
│
├── models/
│   ├── random_forest_model.pkl
│   └── Scaler.pkl
│
├── notebooks/
│   ├── 01_Data_Understanding.ipynb
│   ├── 02_Data_Cleaning.ipynb
│   ├── 03_EDA.ipynb
│   ├── 04_Feature_Engineering.ipynb
│   ├── 05_Model_training.ipynb
│   └── 06_Prediction.ipynb
│
├── src/
├── tests/
├── .gitignore
├── requirements.txt
└── README.md
```

---

# 🛠️ Technologies Used

### Programming Language
- Python

### Machine Learning
- Scikit-learn

### Data Processing
- Pandas
- NumPy

### Data Visualization
- Matplotlib
- Seaborn

### Model Saving
- Joblib

### Web Development
- Flask
- HTML
- CSS

### Development Tools
- Jupyter Notebook
- VS Code

### Version Control
- Git
- GitHub

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/swapnilsharnarthi2006/HOUSE_PRICE_PREDICTION.git
```

## 2. Open the Project

```bash
cd HOUSE_PRICE_PREDICTION
```

## 3. Create a Virtual Environment

```bash
python -m venv .venv
```

## 4. Activate the Virtual Environment

### Windows PowerShell

```powershell
.venv\Scripts\activate
```

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🚀 Run the Application

From the project root directory:

```bash
python app/app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

# 🔐 Project Configuration

Sensitive configuration files should not be committed to GitHub.

The `.gitignore` file excludes files and directories such as:

```text
.venv/
__pycache__/
.ipynb_checkpoints/
.vscode/
.env
.DS_Store
```

---

# 📌 Git & GitHub

Git is used for version control and GitHub is used to host the project source code.

The repository contains:
- Machine Learning notebooks
- Processed dataset
- Flask application
- HTML frontend
- CSS styling
- Requirements
- Project documentation

Large trained model files are excluded from the GitHub repository because of GitHub's individual file-size limitation.

---

# 🔮 Future Improvements

- Hyperparameter tuning
- Cross-validation
- Improved feature engineering
- More extensive model comparison
- Better input validation
- Improved UI/UX
- Interactive data visualizations
- Automated testing
- Model versioning
- Cloud deployment
- API development
- Docker containerization

---

# 🎓 Learning Outcomes

Through this project, the following concepts were practiced:

- Data preprocessing
- Data cleaning
- Exploratory Data Analysis
- Feature engineering
- Train/test splitting
- Feature scaling
- Regression algorithms
- Model evaluation
- Model comparison
- Random Forest
- Model serialization
- Prediction pipelines
- Flask
- HTML/CSS
- Git
- GitHub
- Project structuring

---

# 📊 End-to-End Architecture

```text
                 ┌──────────────────┐
                 │     Dataset      │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Data Processing  │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │       EDA        │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Feature Engineer │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Model Training   │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Random Forest    │
                 └────────┬─────────┘
                          │
                          ▼
              ┌─────────────────────────┐
              │ Saved Model + Scaler    │
              └────────────┬────────────┘
                           │
                           ▼
                 ┌──────────────────┐
                 │ Flask Backend    │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ HTML + CSS UI    │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ House Prediction │
                 └──────────────────┘
```

---

# ✅ Project Status

**Completed ✅**

The project successfully implements an end-to-end Machine Learning workflow:

```text
Data
 ↓
Preprocessing
 ↓
EDA
 ↓
Feature Engineering
 ↓
Model Training
 ↓
Evaluation
 ↓
Model Selection
 ↓
Prediction
 ↓
Flask Web Application
```

---

# 👨‍💻 Author

## Swapnil Sharnarthi

**CSE — Data Science**

Interested in:
- Artificial Intelligence
- Machine Learning
- Data Science
- Building AI-powered applications

---

⭐ If you find this project useful, consider giving the repository a star!
