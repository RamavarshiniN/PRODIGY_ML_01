# House Price Prediction using Linear Regression

This project involves predicting house prices based on their square footage, number of bedrooms, and bathrooms using a Linear Regression model.

## 📌 Project Overview

We use a linear regression model to predict the sale prices of houses. The model is trained on a dataset with the following features:

- **GrLivArea**: Above ground living area (in sq. ft)
- **BedroomAbvGr**: Number of bedrooms above ground
- **HalfBath**: Number of half bathrooms
- **FullBath**: Number of full bathrooms

## 📁 Dataset

- `train.csv`: Training dataset containing features and target variable (`SalePrice`)
- `test.csv`: Test dataset containing features only
- `predicted_prices.csv`: Output file containing test data with predicted house prices

## ⚙️ Dependencies

- Python 3.x
- pandas
- scikit-learn

## 🚀 Execution Steps

1. Place `train.csv` and `test.csv` in the working directory.
2. Run the script:
```bash
python ml01.py
