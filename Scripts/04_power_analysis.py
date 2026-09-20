import pandas as pd
from statsmodels.stats.power import TTestIndPower

# 1. Load Data
df = pd.read_excel('experimental_phase_data_clean.xlsx')

# 2. Parameters (based on your results)
# We use Cohen's d for effect size (e.g., 0.8 is large)
effect_size = 0.8 
alpha = 0.05
sample_size = len(df)

# 3. Calculate Power
analysis = TTestIndPower()
power = analysis.solve_power(effect_size=effect_size, nobs1=sample_size/2, alpha=alpha, ratio=1.0)

print(f"--- Power Analysis Report ---")
print(f"Sample Size (N): {sample_size}")
print(f"Assumed Effect Size (Cohen's d): {effect_size}")
print(f"Calculated Statistical Power: {power:.4f}")
print("Interpretation: Power > 0.80 suggests sufficient sample size for the detected effect.")
