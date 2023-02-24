import os
import glob
import pandas as pd
from datetime import datetime, timedelta


class FileReader:
    def __init__(self, folders):
        self.folders = folders
        self.data = None

    def read_csv_files(self):
        all_files = []
        six_months_ago = datetime.now() - timedelta(days=180)
        for folder in self.folders:
            folder_path = os.path.join(os.path.expanduser('~'), 'Desktop', folder)
            csv_files = glob.glob(os.path.join(folder_path, "*.csv"))
            for csv_file in csv_files:
                created_time = datetime.fromtimestamp(os.path.getctime(csv_file))
                if created_time >= six_months_ago:
                    all_files.append(csv_file)
        if not all_files:
            print("No CSV files found in the specified folders.")
            return
        print(f"Found {len(all_files)} CSV files in the specified folders.")
        usecols = ["Buyer Username", "Item Title", "Quantity", "Sold For", "Sale Date"]
        self.data = pd.concat([pd.read_csv(file, usecols=usecols) for file in all_files], ignore_index=True)
        if self.data.empty:
            print("No data found in the specified CSV files.")
