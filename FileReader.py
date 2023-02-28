import pandas as pd
import os
import glob
from datetime import datetime, timedelta

class FileReader:
    def __init__(self):
        print("FileReader instance created")
        self.unprocessed_path = os.path.join(os.path.expanduser("~"), "Desktop", "eBay Analysis", "Unprocessed Data")
        self.archived_path = os.path.join(os.path.expanduser("~"), "Desktop", "eBay Analysis", "Archived Data")
        self.current_date = datetime.now()
        self.six_months_ago = (self.current_date - timedelta(days=180)).date()

    def get_data_frames(self):
        data = []
        for path in [self.unprocessed_path, self.archived_path]:
            csv_files = glob.glob(os.path.join(path, "*.csv"))
            for csv_file in csv_files:
                file_date = datetime.strptime(csv_file.split("_")[1], "%Y-%m-%d").date()
                if file_date >= self.six_months_ago:
                    print(f"Processing {csv_file}...")
                    data.append(pd.read_csv(csv_file, usecols=["Buyer Username", "Item Title", "Quantity", "Sold For", "Sale Date"]))
        return data

