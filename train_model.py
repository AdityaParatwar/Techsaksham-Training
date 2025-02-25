import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
import pickle

# Load dataset
df_train = pd.read_csv("D:\edunet\DiseasePredictionUI\disease-predictioncd\Training.csv")

# Extract features and labels
X = df_train.drop(columns=["prognosis"])
y = df_train["prognosis"]

# Encode disease labels
le = LabelEncoder()
y = le.fit_transform(y)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = SVC(kernel='linear', probability=True)
model.fit(X_train, y_train)

# Save model and label encoder
with open("./disease_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("./label_encoder.pkl", "wb") as f:
    pickle.dump(le, f)

print("Model training completed!")
