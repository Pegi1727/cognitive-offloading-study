import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Data
df = pd.read_excel('experimental_phase_data_clean.xlsx')
cols = ['Immediate_Comprehension', 'Cognitive_Strain', 'Delayed_Retention', 'Reversal_Detection']
corr_matrix = df[cols].corr()

# Plotting
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='RdYlGn', fmt=".2f")
plt.title('Inter-Variable Correlation Heatmap')
plt.savefig('Figures/correlation_matrix.png')
print("Correlation matrix saved to Figures/folder.")
