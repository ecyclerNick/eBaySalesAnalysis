from FileReader import FileReader
from DataProcessor import DataProcessing
from StatsCalculator import StatsCalculator
from FileWriter import FileWriter


def main():
    # create FileReader object and read in CSV files
    file_reader = FileReader()
    data = file_reader.get_data_frames()

    # create DataProcessing object and process data
    data_processor = DataProcessing(data)
    data_processor.process_data()

    # calculate stats on the data
    stats_calculator = StatsCalculator(data_processor.data)
    stats_calculator.calculate_top_items()
    stats_calculator.calculate_top_buyers()
    stats_calculator.calculate_high_value()
    stats_calculator.calculate_returns_cancellations()

    # write results to Excel file and move processed files to archive folder
    file_writer = FileWriter(stats_calculator.data)
    file_writer.write_results()


if __name__ == "__main__":
    main()
