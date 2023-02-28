import pandas as pd
from DataProcessor import DataProcessing


class StatsCalculator:
    def __init__(self, data):
        self.data = data

    def calculate_top_items(self):
        top_items = self.data.groupby('Item Title')['Quantity'].sum().reset_index().sort_values('Quantity', ascending=False)
        return top_items

    def calculate_top_buyers(self):
        top_buyers = self.data.groupby('Buyer Username').agg({'Quantity': 'sum', 'Item Title': ', '.join}).reset_index()
        top_buyers = top_buyers[top_buyers['Item Title'] != '']
        top_buyers = top_buyers.sort_values('Quantity', ascending=False)
        return top_buyers

    def calculate_high_value(self):
        high_value = self.data.groupby('Item Title')['Sold For'].max().reset_index().sort_values('Sold For', ascending=False)
        return high_value

    def calculate_returns_cancellations(self):
        return_df = pd.DataFrame(columns=["Buyer Username", "Return Rate"])
        repeat_buyers = self.data.groupby("Buyer Username").filter(lambda x: len(x) > 1)
        for buyer in repeat_buyers["Buyer Username"].unique():
            buyer_data = repeat_buyers[repeat_buyers["Buyer Username"] == buyer]
            total_purchased = buyer_data["Quantity"].sum()
            returns = buyer_data[buyer_data["Sale Date"].str.contains("RETURNED")]["Quantity"].sum()
            cancellations = buyer_data[buyer_data["Sale Date"].str.contains("CANCELLED")]["Quantity"].sum()
            total_sold = total_purchased - returns - cancellations
            return_rate = (returns + cancellations) / total_purchased
            return_df = return_df.append({"Buyer Username": buyer, "Return Rate": return_rate}, ignore_index=True)
        return return_df.sort_values("Return Rate", ascending=False)
