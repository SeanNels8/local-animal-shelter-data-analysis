import pandas as pd

# 1. Load the cross-referenced file we just created
df = pd.read_csv('CrossReferenced_Not_Opened_Subscribers.csv')

# 2. Filter for the "Yes" (Okay to Archive)
# This creates a new dataframe containing ONLY the rows where the answer is exactly 'Yes'
df_yes = df[df['Okay to Archive'] == 'Yes']

# 3. Filter for the "No" (Do Not Archive)
# We use .str.startswith('No') because our previous code created two types of "No":
# "No (Restricted Tag)" and "No (Clicked Recently)". This catches both of them!
df_no = df[df['Okay to Archive'].str.startswith('No', na=False)]

# 4. Define the names for our new files
yes_filename = 'Safe_To_Archive_LEIDs.csv'
no_filename = 'Do_Not_Archive_LEIDs.csv'

# 5. Save the filtered dataframes to new CSV files, dropping the extra index numbers
df_yes.to_csv(yes_filename, index=False)
df_no.to_csv(no_filename, index=False)

# 6. Print out the final counts to verify
print(f"Total rows processed: {len(df)}")
print(f"Saved to {yes_filename}: {len(df_yes)} records")
print(f"Saved to {no_filename}: {len(df_no)} records")