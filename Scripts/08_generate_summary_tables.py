import pandas as pd

# Load Data
df = pd.read_excel('experimental_phase_data_clean.xlsx')

# Grouped Summary
summary = df.groupby(['Condition', 'Profile'])[['Immediate_Comprehension', 'Delayed_Retention', 'Cognitive_Strain']].agg(['mean', 'std']).round(2)

# Convert to Markdown for GitHub
print("--- Summary Table (Markdown Format) ---")
print(summary.to_markdown())

# Save to CSV
summary.to_csv('advanced_analysis/summary_statistics_table.csv')
