import pandas as pd

# Creating the dataset based on the provided table
data = [
    [1, 19, 18, 37, 'B', 'C', 'Habitual'],
    [2, 18, 17, 35, 'B', 'C', 'Habitual'],
    [3, 20, 19, 39, 'B', 'C', 'Habitual'],
    [4, 17, 16, 33, 'B', 'C', 'Habitual'],
    [5, 19, 15, 34, 'B', 'C', 'Habitual'],
    [6, 18, 18, 36, 'B', 'C', 'Habitual'],
    [7, 16, 17, 33, 'B', 'C', 'Habitual'],
    [8, 15, 16, 31, 'B', 'C', 'Habitual'],
    [9, 19, 19, 38, 'B', 'C', 'Habitual'],
    [10, 18, 16, 34, 'B', 'C', 'Habitual'],
    [11, 17, 15, 32, 'B', 'C', 'Habitual'],
    [12, 16, 14, 30, 'B', 'C', 'Habitual'],
    [13, 18, 18, 36, 'B', 'C', 'Habitual'],
    [14, 19, 17, 36, 'B', 'C', 'Habitual'],
    [15, 17, 17, 34, 'B', 'C', 'Habitual'],
    [16, 15, 15, 30, 'B', 'C', 'Habitual'],
    [17, 16, 16, 32, 'B', 'C', 'Habitual'],
    [18, 18, 19, 37, 'B', 'C', 'Habitual'],
    [19, 20, 18, 38, 'B', 'C', 'Habitual'],
    [20, 17, 16, 33, 'B', 'C', 'Habitual'],
    [21, 19, 17, 36, 'B', 'C', 'Habitual'],
    [22, 18, 15, 33, 'B', 'C', 'Habitual'],
    [23, 16, 18, 34, 'B', 'C', 'Habitual'],
    [24, 17, 17, 34, 'B', 'C', 'Habitual'],
    [25, 15, 14, 29, 'B', 'C', 'Habitual'],
    [26, 19, 19, 38, 'B', 'C', 'Habitual'],
    [27, 18, 16, 34, 'B', 'C', 'Habitual'],
    [28, 17, 18, 35, 'B', 'C', 'Habitual'],
    [29, 16, 15, 31, 'B', 'C', 'Habitual'],
    [30, 19, 17, 36, 'B', 'C', 'Habitual'],
    [31, 18, 17, 35, 'B', 'C', 'Habitual'],
    [32, 17, 16, 33, 'B', 'C', 'Habitual'],
    [33, 16, 16, 32, 'B', 'C', 'Habitual'],
    [34, 19, 18, 37, 'B', 'C', 'Habitual'],
    [35, 18, 19, 37, 'B', 'C', 'Habitual'],
    [36, 17, 15, 32, 'B', 'C', 'Habitual'],
    [37, 16, 15, 31, 'B', 'C', 'Habitual'],
    [38, 18, 17, 35, 'B', 'C', 'Habitual'],
    [39, 19, 16, 35, 'B', 'C', 'Habitual'],
    [40, 17, 18, 35, 'B', 'C', 'Habitual'],
    [41, 16, 14, 30, 'B', 'C', 'Habitual'],
    [42, 18, 16, 34, 'B', 'C', 'Habitual'],
    [43, 19, 19, 38, 'B', 'C', 'Habitual'],
    [44, 17, 17, 34, 'B', 'C', 'Habitual'],
    [45, 16, 17, 33, 'B', 'C', 'Habitual'],
    [46, 18, 16, 34, 'B', 'C', 'Habitual'],
    [47, 19, 18, 37, 'B', 'C', 'Habitual'],
    [48, 17, 15, 32, 'B', 'C', 'Habitual'],
    [49, 16, 16, 32, 'B', 'C', 'Habitual'],
    [50, 18, 17, 35, 'B', 'C', 'Habitual'],
    [51, 19, 16, 35, 'B', 'C', 'Habitual'],
    [52, 17, 14, 31, 'B', 'C', 'Habitual'],
    [53, 16, 15, 31, 'B', 'C', 'Habitual'],
    [54, 18, 18, 36, 'B', 'C', 'Habitual'],
    [55, 12, 11, 23, 'C', 'B', 'Moderate'],
    [56, 13, 12, 25, 'C', 'C', 'Moderate'],
    [57, 11, 10, 21, 'C', 'B', 'Moderate'],
    [58, 12, 13, 25, 'C', 'C', 'Moderate'],
    [59, 11, 9, 20, 'C', 'B', 'Moderate'],
    [60, 13, 11, 24, 'C', 'C', 'Moderate'],
    [61, 12, 12, 24, 'C', 'B', 'Moderate'],
    [62, 11, 11, 22, 'C', 'C', 'Moderate'],
    [63, 13, 12, 25, 'C', 'B', 'Moderate'],
    [64, 12, 10, 22, 'C', 'C', 'Moderate'],
    [65, 11, 9, 20, 'C', 'B', 'Moderate'],
    [66, 13, 13, 26, 'C', 'C', 'Moderate'],
    [67, 12, 11, 23, 'C', 'B', 'Moderate'],
    [68, 11, 11, 22, 'C', 'C', 'Moderate'],
    [69, 13, 12, 25, 'C', 'B', 'Moderate'],
    [70, 12, 10, 22, 'C', 'C', 'Moderate'],
    [71, 11, 9, 20, 'C', 'B', 'Moderate'],
    [72, 12, 12, 24, 'C', 'C', 'Moderate'],
    [73, 7, 6, 13, 'A', 'A', 'Active'],
    [74, 8, 7, 15, 'A', 'A', 'Active'],
    [75, 6, 5, 11, 'A', 'B', 'Active'],
    [76, 7, 6, 13, 'A', 'A', 'Active'],
    [77, 8, 8, 16, 'A', 'A', 'Active'],
    [78, 6, 6, 12, 'A', 'B', 'Active'],
    [79, 7, 5, 12, 'A', 'A', 'Active'],
    [80, 8, 7, 15, 'A', 'A', 'Active'],
    [81, 7, 6, 13, 'A', 'B', 'Active'],
    [82, 18, 10, 28, 'A', 'C', 'Inconsistent'],
    [83, 15, 12, 27, 'B', 'A', 'Inconsistent'],
    [84, 12, 14, 26, 'C', 'C', 'Moderate-Mix'],
    [85, 19, 8, 27, 'A', 'C', 'Inconsistent'],
    [86, 10, 17, 27, 'B', 'A', 'Inconsistent'],
    [87, 14, 13, 27, 'C', 'B', 'Moderate-Mix'],
    [88, 13, 12, 25, 'C', 'C', 'Moderate-Mix'],
    [89, 16, 12, 28, 'B', 'A', 'Inconsistent'],
    [90, 11, 15, 26, 'A', 'C', 'Inconsistent'],
]

columns = ['ID', 'P2', 'P4', 'Total', 'Orient', 'SJI', 'Group_Note']
df = pd.DataFrame(data, columns=columns)

# Save to CSV
file_path = '/mnt/data/screening_data.csv'
df.to_csv(file_path, index=False)

# Also save raw data to Excel
xlsx_path = '/mnt/data/screening_data.xlsx'
df.to_excel(xlsx_path, index=False, sheet_name='RawData')

# Verification
assert len(df) == 90, 'row count'
assert (df['ID'] == range(1, 91)).all(), 'IDs sequential'
assert (df['P2'] + df['P4'] == df['Total']).all(), 'Total check'
print('rows:', len(df))
print('Total check P2+P4==Total:', (df['P2'] + df['P4'] == df['Total']).all())
print('Group counts:', df['Group_Note'].value_counts().to_dict())
print('Orient counts:', df['Orient'].value_counts().to_dict())
print('SJI counts:', df['SJI'].value_counts().to_dict())
print('CSV:', file_path)
print('XLSX:', xlsx_path)
