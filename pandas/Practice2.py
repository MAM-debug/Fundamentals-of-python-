import pandas as pd

data = {
    'NAME': ['Abdullah', 'Azfar', 'Shaham', 'Ghulam Qadir'],
    'AGE': [20, 19, 21, 20],
    'GPA': [3.5, 3.8, 3.2, 3.6]
}
df = pd.DataFrame(data)
print(df)
print("\n" + "="*60 + "\n")

print("Names in the DataFrame:")
print(df['NAME'])
print("\n" + "="*60 + "\n")

print("ITERATING THROUGH NAMES:")
for name in df['NAME']:
    print(name)
print("(above will print names one by one by removing the indexes)")
print("\n" + "="*60 + "\n")

print("Filtering DataFrame based on condition like gpas and age:")
filter_df = df[df['GPA'] > 3.5]
print(filter_df)
print("\n" + "="*60 + "\n")

print("Sorting DF in descending order based on GPA:")
sorted_df = df.sort_values(by='GPA', ascending=False)
print(sorted_df)
print("\n" + "="*60 + "\n")

print("Adding new column to DF:")
df['GRADES'] = ['A', 'A+', 'B+', 'A']
print(df)
print("\n" + "="*60 + "\n")

print("DROPPING COLUMNS:")
df_no_name = df.drop('AGE', axis=1)  # axis=1 means column
print("Without AGE column:")
print(df_no_name)
print("\n" + "="*60 + "\n")

print("Descriptive statistics of the DataFrame:")
print(df.describe())
print("\nJust GPA statistics:")
print(df['GPA'].describe())
print("\n" + "="*60 + "\n")

print("Accessing specific row by index:")
print(df.iloc[2])  # Accessing the third row (index 2)
print("\n" + "="*60 + "\n")

print("Printing multiple rows together:")
print(df.iloc[1:3])
print("\n" + "="*60 + "\n")

print("Printing row by loc:")
print(df.loc[1])  # This prints entire row 1
print("\n" + "="*60 + "\n")

# ✅ CORRECT WAYS TO SELECT COLUMNS:
print("Selecting specific columns for one row:")
print(df.loc[1, ['NAME', 'GPA']])  # Row 1, only NAME and GPA
print()

print("Selecting specific columns for all rows:")
print(df.loc[:, ['NAME', 'GPA']])  # All rows, only NAME and GPA
print()

print("Simpler way (all rows, specific columns):")
print(df[['NAME', 'GPA']])  # Most common way!

