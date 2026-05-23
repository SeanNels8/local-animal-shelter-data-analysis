import pandas as pd

# 1. Load both CSV files
df_clicked = pd.read_csv('Subscribers Have Clicked Since Jan 2025.csv')
df_not_opened = pd.read_csv('Subscribers Have Not Opened since Jan 2025.csv')

# 2. Extract the LEIDs and turn them into "Sets"
leids_clicked = set(df_clicked['LEID'])
leids_not_opened = set(df_not_opened['LEID'])

# 3. Find the exact overlap using the .intersection() command
overlap = leids_clicked.intersection(leids_not_opened)

# 4. Print out the final numbers
print(f"Total in Clicked: {len(leids_clicked)}")
print(f"Total in Not Opened: {len(leids_not_opened)}")
print(f"Number of overlapping LEIDs: {len(overlap)}")

# 5. Print LEID numbers that appear on both lists
if len(overlap) > 0:
    print(f"Overlapping LEIDs: {overlap}")