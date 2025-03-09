import pandas as pd

def process_sales_data(input_file, output_file):
    df = pd.read_csv(input_file)
    avg_price_per_foot = df['price_per_foot'].mean()
    filtered_df = df[df['price_per_foot'] < avg_price_per_foot]
    filtered_df.to_csv(output_file, index=False)

if __name__ == "__main__":
    process_sales_data("../data/sales-data.csv", "data/output_sales_data.csv")