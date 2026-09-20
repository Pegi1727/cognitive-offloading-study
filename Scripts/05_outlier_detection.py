import pandas as pd
import numpy as np

# Load Data
df = pd.read_excel('experimental_phase_data_clean.xlsx')
metrics = ['Immediate_Comprehension', 'Cognitive_Strain', 'Delayed_Retention']

print("--- Outlier Detection (Z-Score > 3) ---")
for col in metrics:
    z_scores = (df[col] - df[col].mean()) / df[col].std()
    outliers = df[np.abs(z_scores) > 3]
    print(f"{col}: Found {len(outliers)} outliers.")

if len(outliers) == 0:
    print("Conclusion: Dataset is clean; no extreme outliers detected.")
