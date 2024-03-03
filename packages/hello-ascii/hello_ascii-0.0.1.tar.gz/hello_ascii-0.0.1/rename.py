import os
import re
from datetime import datetime

# Renames folders like 'Home, 4 October 2022' to '[20221004]'


def remove_home_and_rename_folders(folder_path):

    for folder_name in os.listdir(folder_path):
        old_folder_path = os.path.join(folder_path, folder_name)
        if os.path.isdir(old_folder_path):
            try:
                # Remove 'Home,' from the folder name if it exists
                folder_name = folder_name.replace('Home,', '').strip()
                print(folder_name)
                # Extract day, month, and year from folder name
                match = re.match(r'(\d+) ([a-zA-Z]+) (\d+)', folder_name)
                if match:
                    day, month, year = match.groups()
                    month_number = datetime.strptime(month, "%B").month

                    # Remove characters before the first digit of the year
                    year = re.sub(r'^\D*', '', year)

                    # Format the folder name to [YYYYMMDD]
                    new_folder_nm = f"[{year}{month_number:02d}{int(day):02d}]"

                    # Rename the folder
                    new_folder_path = os.path.join(folder_path, new_folder_nm)
                    os.rename(old_folder_path, new_folder_path)
                    print(f"Renamed '{folder_name}' to '{new_folder_nm}'")
                else:
                    print(f"Failed to rename '{folder_name}' invalid format")
            except ValueError:
                print(f"Failed to rename '{folder_name}' due to invalid date")


if __name__ == "__main__":
    # Get the current working directory as the folder path
    folder_path = os.getcwd()
    remove_home_and_rename_folders(folder_path)
