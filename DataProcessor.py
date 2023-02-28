import pandas as pd
from FileReader import FileReader


class DataProcessing:
    def __init__(self, data):
        self.data = data
        self.top_items = None
        self.top_buyers = None
        self.high_value = None
        self.returns_cancellations = None

    def process_data(self):
        self.clean_data()
        self.calculate_top_items()
        self.calculate_top_buyers()
        self.calculate_high_value()
        self.calculate_returns_cancellations()
    def clean_data(self):
        self.data = self.data[["Buyer Username", "Item Title", "Quantity", "Sold For", "Sale Date"]]
        self.data = self.data.dropna(subset=["Buyer Username", "Sale Date", "Item Title"])
        self.data["Sale Date"] = pd.to_datetime(self.data["Sale Date"])
        self.data["Total Sale"] = self.data["Quantity"] * self.data["Sold For"]

    def calculate_top_items(self):
        top_items = self.data.groupby("Item Title")["Quantity"].sum().reset_index()
        self.top_items = top_items.sort_values(by="Quantity", ascending=False)

    def calculate_top_buyers(self):
        top_buyers = self.data.groupby("Buyer Username").agg({"Quantity": "sum", "Item Title": lambda x: x.value_counts().index[0]})
        self.top_buyers = top_buyers.sort_values(by="Quantity", ascending=False)

    def calculate_high_value(self):
        high_value = self.data.groupby("Item Title")["Total Sale"].sum().reset_index()
        self.high_value = high_value.sort_values(by="Total Sale", ascending=False)

    def calculate_returns_cancellations(self):
        returns_cancellations = self.data.groupby("Buyer Username").agg({"Sale Date": "count", "Total Sale": "sum"})
        returns_cancellations = returns_cancellations.rename(columns={"Sale Date": "Orders", "Total Sale": "Sales"})
        returns_cancellations = returns_cancellations[returns_cancellations["Orders"] > 1]
        self.returns_cancellations = returns_cancellations.sort_values(by="Orders", ascending=False)

