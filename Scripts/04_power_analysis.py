import pandas as pd
from statsmodels.stats.power import TTestIndPower

# بارگذاری داده‌ها
df = pd.read_excel('experimental_phase_data_clean.xlsx')

# محاسبه اثر اندازه (Effect Size) فرض شده بر اساس نتایج قبلی
effect_size = 0.8  # Cohen's d
alpha = 0.05
power = 0.8

# محاسبه توان آماری برای نمونه N=63
analysis = TTestIndPower()
result = analysis.solve_power(effect_size=effect_size, nobs1=63, alpha=alpha, ratio=1.0)

print(f"Statistical Power for N=63 with effect size {effect_size}: {result:.4f}")
