import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import roc_auc_score
from xgboost import XGBClassifier

# 1. Load dataset
df = pd.read_csv("winequality.csv")  # adjust filename if needed

X = df.drop("quality", axis=1)
y = df["quality"]

# 2. Train-test split
xtrain, xtest, ytrain, ytest = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Scaling
scaler = MinMaxScaler()
xtrain = scaler.fit_transform(xtrain)
xtest = scaler.transform(xtest)

# 4. Train model
model = XGBClassifier(
    n_estimators=100,
    max_depth=5,
    learning_rate=0.1,
    random_state=42
)
model.fit(xtrain, ytrain)

# 5. Evaluation
train_auc = roc_auc_score(ytrain, model.predict(xtrain))
test_auc = roc_auc_score(ytest, model.predict(xtest))

print("Training ROC-AUC:", train_auc)
print("Validation ROC-AUC:", test_auc)

# 6. Save model & scaler
joblib.dump(model, "wine_model.pkl")
joblib.dump(scaler, "scaler.pkl")

print("Model and scaler saved successfully.")
