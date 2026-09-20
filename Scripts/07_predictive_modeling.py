import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Load and Prepare Data
df = pd.read_excel('experimental_phase_data_clean.xlsx')
X = pd.get_dummies(df[['Condition', 'Profile', 'Cognitive_Strain', 'Immediate_Comprehension']])
y = df['Delayed_Retention']

# Train simple model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Feature Importance
importance = pd.DataFrame({'Feature': X.columns, 'Importance': model.feature_importances_})
print("--- Feature Importance for Delayed Retention ---")
print(importance.sort_values(by='Importance', ascending=False))
