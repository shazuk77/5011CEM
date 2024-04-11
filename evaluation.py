from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

# Making predictions on the training and testing sets
y_train_pred = model.predict(x_train)
y_test_pred = model.predict(x_test)

# Calculating Mean Absolute Error (MAE)
train_mae = mean_absolute_error(y_train, y_train_pred)
test_mae = mean_absolute_error(y_test, y_test_pred)

# Calculating Mean Squared Error (MSE) and Root Mean Squared Error (RMSE)
train_mse = mean_squared_error(y_train, y_train_pred)
test_mse = mean_squared_error(y_test, y_test_pred)
train_rmse = np.sqrt(train_mse)
test_rmse = np.sqrt(test_mse)

print("Training Mean Absolute Error:", train_mae)
print("Testing Mean Absolute Error:", test_mae)
print("\nTraining Mean Squared Error:", train_mse)
print("Testing Mean Squared Error:", test_mse)
print("\nTraining Root Mean Squared Error:", train_rmse)
print("Testing Root Mean Squared Error:", test_rmse)
