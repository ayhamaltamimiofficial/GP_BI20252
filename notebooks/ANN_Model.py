import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.metrics import r2_score, mean_absolute_error

# 1. Loading the dataset
# Ensure your file is named 'Ayham Altamimi Graduation Project.csv' 
try:
    df = pd.read_csv('/Ayham Altamimi Graduation Project.csv')
    print("Dataset loaded successfully.")
except Exception as e:
    print(f"Error loading data: {e}")

# 2. Data Preprocessing
# Selecting only numerical features (Removing 'Jordan', 'Year', etc.)
numeric_df = df.select_dtypes(include=[np.number])

# Handling Missing Values (NaN) using Mean Imputation
numeric_df = numeric_df.fillna(numeric_df.mean())

# Handling Infinite values
numeric_df = numeric_df.replace([np.inf, -np.inf], np.nan).dropna()

# Splitting Features (X) and Target (y - Unemployment Rate)
X = numeric_df.iloc[:, :-1].values
y = numeric_df.iloc[:, -1].values

# 3. Feature Scaling (Normalization to [0, 1])
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
y_scaled = scaler.fit_transform(y.reshape(-1, 1))

# 4. Train-Test Split (80% for training, 20% for testing)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_scaled, test_size=0.2, random_state=42)

# 5. Designing the Neural Network Architecture
model = Sequential([
    Dense(64, input_dim=X.shape[1], activation='relu'), # Hidden Layer 1
    Dense(32, activation='relu'),                      # Hidden Layer 2
    Dense(1, activation='linear')                      # Output Layer
])

# 6. Compiling the Model
model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# 7. Model Training
print("Training the Artificial Neural Network...")
history = model.fit(X_train, y_train, epochs=100, validation_split=0.1, verbose=0)

# 8. Evaluating Performance
predictions = model.predict(X_test)
accuracy_r2 = r2_score(y_test, predictions)
mae = mean_absolute_error(y_test, predictions)

print(f"\n--- Final Results ---")
print(f"R-Squared Accuracy: {accuracy_r2 * 100:.2f}%")
print(f"Mean Absolute Error: {mae:.4f}")

# 9. Visualizing Loss Convergence
plt.figure(figsize=(8, 5))
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('ANN Training Convergence')
plt.xlabel('Epochs')
plt.ylabel('Loss (MSE)')
plt.legend()
plt.grid(True)
plt.show()

print(f"\n⭐ Finally! Model Accuracy (R2): {accuracy_r2 * 100:.2f}%")
