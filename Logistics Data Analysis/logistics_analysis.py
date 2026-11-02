# Logistics Delivery Performance Analysis - reproducible starter script
# Dataset supplied with this package is SIMULATED for learning purposes.
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv("logistics_simulated_dataset.csv")
df["Shipment_Weight_kg"] = df["Shipment_Weight_kg"].fillna(df["Shipment_Weight_kg"].median())
df["Weather"] = df["Weather"].fillna(df["Weather"].mode()[0])
df["Shipping_Cost_USD"] = df["Shipping_Cost_USD"].fillna(df["Shipping_Cost_USD"].median())

# Cap extreme shipping-cost observations using the IQR rule.
q1, q3 = df["Shipping_Cost_USD"].quantile([0.25, 0.75])
iqr = q3 - q1
df["Shipping_Cost_USD"] = df["Shipping_Cost_USD"].clip(q1 - 1.5*iqr, q3 + 1.5*iqr)

features = ["Region","Shipping_Mode","Distance_km","Shipment_Weight_kg",
            "Order_Quantity","Weather","Traffic_Level","Scheduled_Delivery_Days"]
target = "Actual_Delivery_Days"
X, y = df[features], df[target]
categorical = ["Region","Shipping_Mode","Weather","Traffic_Level"]
numeric = [c for c in features if c not in categorical]

preprocess = ColumnTransformer([
    ("num", Pipeline([("imputer", SimpleImputer(strategy="median")),
                      ("scale", StandardScaler())]), numeric),
    ("cat", Pipeline([("imputer", SimpleImputer(strategy="most_frequent")),
                      ("onehot", OneHotEncoder(handle_unknown="ignore"))]), categorical)
])
pipeline = Pipeline([("preprocess", preprocess),
                     ("model", RandomForestRegressor(n_estimators=180, max_depth=12,
                         min_samples_leaf=3, random_state=42, n_jobs=-1))])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
print("MAE:", mean_absolute_error(y_test, y_pred))
print("RMSE:", mean_squared_error(y_test, y_pred)**0.5)
print("R2:", r2_score(y_test, y_pred))
