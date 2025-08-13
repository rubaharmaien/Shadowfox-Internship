# 🚗 Car Selling Price Prediction

This project predicts the **selling price of cars** using machine learning techniques.  
It involves **data preprocessing, exploratory data analysis (EDA)**, and **model building** with regression algorithms.

## 📌 Project Overview
Car price prediction is a crucial use case in the automobile industry.  
By analyzing historical data, this project aims to build a regression model that can accurately predict a car's selling price based on its features such as:

- Year of manufacture  
- Present price  
- Kms driven  
- Fuel type  
- Seller type  
- Transmission type  
- Owner count  

## 📂 Dataset
The dataset used (`car.csv`) contains car details with multiple features and the target variable **Selling Price**.

### Example Columns:
- `Car_Name`  
- `Year`  
- `Present_Price`  
- `Kms_Driven`  
- `Fuel_Type`  
- `Seller_Type`  
- `Transmission`  
- `Owner`  
- `Selling_Price` (Target)

## 🛠️ Technologies Used
- **Python**  
- **NumPy, Pandas** – Data manipulation  
- **Matplotlib, Seaborn** – Data visualization  
- **Scikit-learn** – Model training & evaluation  

## ⚙️ Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/Car-Selling-Price-Prediction.git
   cd Car-Selling-Price-Prediction
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage
Run the Jupyter Notebook to train and test the model:
```bash
jupyter notebook Car_Selling-PricePrediction.ipynb
```

## 📊 Project Workflow
1. **Import Libraries**  
2. **Load Dataset**  
3. **Data Preprocessing** (handling missing values, encoding categorical variables)  
4. **Exploratory Data Analysis (EDA)**  
5. **Model Training** (Linear Regression)  
6. **Model Evaluation** (MAE, MSE, R² score)  

## 📈 Results
The **Linear Regression model** achieved:
- **MAE:** (2.0349434490336122)  
- **MSE:** (9.225663641224129)  
- **RMSE Score:**( 3.0373777574124903) 
- **R² Score:** (0.5995038184033071)  

## 📜 License
This project is licensed under the MIT License.
