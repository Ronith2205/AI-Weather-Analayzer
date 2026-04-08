import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import pickle

# Load dataset
data = pd.read_csv("seattle-weather.csv")

# Features (use correct names from dataset)
X = data[['precipitation', 'temp_max', 'temp_min', 'wind']]

# Labels
y = data['weather']

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Weather model trained successfully!")