import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the training and test datasets
train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')

# Extract features and target variable from training dataset
X_train = train_data[['GrLivArea', 'BedroomAbvGr', 'HalfBath', 'FullBath']]
y_train = train_data['SalePrice']

# Extract same features from test dataset
X_test = test_data[['GrLivArea', 'BedroomAbvGr', 'HalfBath', 'FullBath']]

# Train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict house prices on test data
y_pred = model.predict(X_test)

# Round predicted prices to two decimal places
y_pred_rounded = [round(price, 2) for price in y_pred]

# Add predicted prices to test data
test_data['PredictedPrice'] = y_pred_rounded

# Save predictions to a CSV file
test_data.to_csv('predicted_prices.csv', columns=['Id', 'PredictedPrice'], index=False)

# Print coefficients and intercept
print("Model Coefficients:", model.coef_)
print("Model Intercept:", model.intercept_)
