import os

import pandas as pd

current_path = os.path.abspath(os.getcwd())
csv_logic_path = "csv_logic"


def get_skins_combo() -> dict:
    filename = os.path.join(current_path, csv_logic_path, 'skins.csv')
    # Use pandas to read the CSV file
    df = pd.read_csv(filename, skiprows=lambda x: x == 1)

    data_dict = {}

    for index, row in df.iterrows():
        key = row.iloc[0]

        # Convert the selected columns to a comma-separated string
        value = ', '.join(row.iloc[15:19].astype(str).tolist())  # Convert to string to ensure join works

        # Format the string as required
        data_dict[key] = f",,,,,,,,,,,,,,{value},"

    return data_dict


def prepare_skin_confs_line(chosen_skin, brawler_name):
    filename = os.path.join(current_path, csv_logic_path, 'skin_confs.csv')
    df = pd.read_csv(filename)
    base_line = df[df['Name'] == chosen_skin].iloc[0]  # Replace 'FirstColumnName' with the actual column name
    new_line = base_line.copy()
    new_line['Name'] = brawler_name + "Default"  # Adjust column name as needed
    new_line['Character'] = brawler_name  # Adjust column name as needed
    columns_to_clear = ['MainAttackProjectile', 'SecondaryProjectile', 'UltiProjectile', 'AutoAttackProjectile',
                        'ProjectileForShockyStarPower', 'IncendiaryStarPowerAreaEffect']
    for col in columns_to_clear:
        new_line[col] = ''  # Set to empty
    return new_line


prepare_skin_confs_line(list(get_skins_combo().keys())[5], "Angel")
# data_dict = get_skins_combo()
#
# # Now data_dict contains the desired association
# for k, v in data_dict.items():
#     print(k, v)
