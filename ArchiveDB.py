import pandas as pd

# Load the data
tags_df = pd.read_csv('csvtags.csv')
df_not_opened = pd.read_csv('Subscribers Have Not Opened since Jan 2025.csv')
df_clicked = pd.read_csv('Subscribers Have Clicked Since Jan 2025.csv')

# Create dictionary of rules mapping the exact tag name to its "Yes" or "No" archive status
archive_rules = dict(zip(tags_df['Tag'].astype(str).str.strip(), tags_df['Okay to Archive?'].astype(str).str.strip()))

# Get a set of all LEIDs that clicked recently
active_leids = set(df_clicked['LEID'])


def check_if_should_archive(row):
    # 1. CROSS-REFERENCE CHECK: Did they click recently?
    if row['LEID'] in active_leids:
        return "No (Clicked Recently)"

    # 2. TAG CHECK: Look at their specific tags
    tags_string = row['TAGS']
    if pd.isna(tags_string):
        return "Yes"

    tags_list = [t.strip().strip('"') for t in str(tags_string).split('",')]

    for tag in tags_list:
        tag_clean = tag.strip('"')
        rule = archive_rules.get(tag_clean, "Unknown")

        if rule == 'No':
            return "No (Restricted Tag)"

    # If they didn't click recently AND none of their tags restrict archiving:
    return "Yes"


# Apply the logic to the Not Opened list (axis=1 to check the whole row)
df_not_opened['Okay to Archive'] = df_not_opened.apply(check_if_should_archive, axis=1)

# Save the final results to a new CSV file
df_not_opened.to_csv('CrossReferenced_Not_Opened_Subscribers.csv', index=False)

# Print out the final stats to verify the numbers
print(f"Total Not Opened Subscribers: {len(df_not_opened)}")
print(f"Safe to Archive: {(df_not_opened['Okay to Archive'] == 'Yes').sum()}")
print(f"Do Not Archive (Restricted Tag): {(df_not_opened['Okay to Archive'] == 'No (Restricted Tag)').sum()}")
print(f"Do Not Archive (Clicked Recently): {(df_not_opened['Okay to Archive'] == 'No (Clicked Recently)').sum()}")