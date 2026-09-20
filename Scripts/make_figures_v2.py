import pandas as pd, numpy as np, os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('/mnt/data/experimental_phase_data_clean.xlsx')
sns.set_theme(style="whitegrid")
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 11

color_ai = '#1E90FF'    # brighter blue
color_ctrl = '#FF6F3C'  # brighter coral
group_order = ['Habitual', 'Active']

def stats(col):
    s = df.groupby(['Group', 'Condition'])[col].agg(['mean', 'sem']).reset_index()
    s['Group'] = pd.Categorical(s['Group'], categories=group_order, ordered=True)
    return s.sort_values('Group')

def line_plot(col, title, ylabel, note, fname):
    st = stats(col)
    plt.figure(figsize=(6.5, 4.5), dpi=300)
    for cond, color, marker in [('AI-Access', color_ai, 'o'), ('Control', color_ctrl, 's')]:
        sub = st[st['Condition'] == cond]
        plt.errorbar(sub['Group'].astype(str), sub['mean'], yerr=sub['sem'], label=cond,
                     color=color, marker=marker, markersize=9, linewidth=2.8,
                     capsize=6, capthick=1.6)
    plt.title(title, fontsize=13, fontweight='bold', pad=12)
    plt.xlabel('AI Reliance Profile', fontsize=11, fontweight='bold', labelpad=8)
    plt.ylabel(ylabel, fontsize=11, fontweight='bold', labelpad=8)
    plt.legend(title='Condition', frameon=True, facecolor='white', framealpha=0.9)
    plt.annotate(note, xy=(0.03, 0.06), xycoords='axes fraction',
                 bbox=dict(boxstyle="round,pad=0.4", fc="#EAF2FB", ec="#9CC3E5", lw=1))
    plt.tight_layout()
    plt.savefig(fname, dpi=300)
    plt.close()

def bar_plot(col, title, ylabel, note, fname, ylim=None):
    st = stats(col)
    fig, ax = plt.subplots(figsize=(6.5, 4.5), dpi=300)
    x = np.arange(2); width = 0.35
    ai = st[st['Condition'] == 'AI-Access'].set_index('Group').loc[group_order]
    ct = st[st['Condition'] == 'Control'].set_index('Group').loc[group_order]
    ax.bar(x - width/2, ai['mean'], width, yerr=ai['sem'], label='AI-Access',
           color=color_ai, capsize=5, edgecolor='black', linewidth=0.8)
    ax.bar(x + width/2, ct['mean'], width, yerr=ct['sem'], label='Control',
           color=color_ctrl, capsize=5, edgecolor='black', linewidth=0.8)
    ax.set_title(title, fontsize=13, fontweight='bold', pad=12)
    ax.set_xlabel('AI Reliance Profile', fontsize=11, fontweight='bold', labelpad=8)
    ax.set_ylabel(ylabel, fontsize=11, fontweight='bold', labelpad=8)
    ax.set_xticks(x)
    ax.set_xticklabels(group_order, fontweight='bold')
    ax.legend(title='Condition', frameon=True, facecolor='white', framealpha=0.9)
    if ylim:
        ax.set_ylim(*ylim)
    ax.annotate(note, xy=(0.03, 0.88), xycoords='axes fraction',
                bbox=dict(boxstyle="round,pad=0.4", fc="#FFF1EA", ec="#F0B9A0", lw=1))
    plt.tight_layout()
    plt.savefig(fname, dpi=300)
    plt.close()

line_plot('Comp_Score', 'Figure 2. Immediate Comprehension Score', 'Comprehension Score',
          r'Interaction: $F(1, 59) = 12.84,\ p = .001,\ \eta^2 = .18$',
          '/mnt/data/Figure_2_Immediate_Comprehension_v2.png')

bar_plot('Switch_Det', 'Figure 3. Conceptual Reversal Detection', 'Probability of Successful Detection',
         r'$OR = 0.28,\ 95\%\ \mathrm{CI}\ [.15,\ .52],\ p < .001$',
         '/mnt/data/Figure_3_Conceptual_Reversal_Detection_v2.png', ylim=(0, 1.1))

bar_plot('Strain', 'Figure 4. Perceived Cognitive Strain', 'Cognitive Strain Score',
         r'Main Effect of AI Access: $F(1, 59) = 15.32,\ p < .001,\ \eta^2 = .21$',
         '/mnt/data/Figure_4_Cognitive_Strain_v2.png')

line_plot('Retent_Score', 'Figure 5. Delayed Structural Retention Score', 'Retention Score',
          r'Interaction: $F(1, 59) = 11.76,\ p = .001,\ \eta^2 = .16$',
          '/mnt/data/Figure_5_Delayed_Structural_Retention_v2.png')

for col in ['Comp_Score', 'Switch_Det', 'Strain', 'Retent_Score']:
    print(col)
    print(stats(col).round(3).to_string())

from PIL import Image
for f in sorted(os.listdir('/mnt/data')):
    if f.endswith('_v2.png'):
        p = '/mnt/data/' + f
        im = Image.open(p)
        print(f, os.path.getsize(p), 'bytes, size:', im.size, 'dpi:', im.info.get('dpi'))
