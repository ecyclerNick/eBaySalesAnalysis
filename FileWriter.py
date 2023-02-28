import os
import pandas as pd
import glob
import shutil
from StatsCalculator import StatsCalculator


class FileWriter:
    def __init__(self, data):
        self.data = data

    def write_results(self):
        writer = pd.ExcelWriter('eBay_results.xlsx', engine='xlsxwriter')
        self.data['Top Items'].to_excel(writer, sheet_name='Top Items', index=False)
        self.data['Top Buyers'].to_excel(writer, sheet_name='Top Buyers', index=False)
        self.data['High Value'].to_excel(writer, sheet_name='High Value', index=False)
        self.data['Returns or Cancellations'].to_excel(writer, sheet_name='Returns or Cancellations', index=False)
        writer.save()
        print("Results written to eBay_results.xlsx")
        self.move_files()

    def move_files(self):
        unprocessed_path = os.path.join(os.getcwd(), 'eBay Analysis', 'Unprocessed Data')
        archive_path = os.path.join(os.getcwd(), 'eBay Analysis', 'Archived Data')
        csv_files = glob.glob(os.path.join(unprocessed_path, "*.csv"))
        for csv_file in csv_files:
            shutil.move(csv_file, os.path.join(archive_path, os.path.basename(csv_file)))
        print(f"Moved {len(csv_files)} CSV files from Unprocessed Data to Archived Data.")