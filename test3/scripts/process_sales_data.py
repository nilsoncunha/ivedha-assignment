import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
path = BASE_DIR / 'data'

def process_sales_data(input_file, output_file):
    # read csv file
    df = pd.read_csv(input_file)

    # exclude beds, baths and sq__ft with 0
    df2 = df[(df.beds != 0) | (df.baths != 0)].copy()
    df2 = df[df.sq__ft != 0].copy()

    # create new columns
    df2['price_per_sqft'] = df2['price'] / df2['sq__ft']
    df2['avg_price_per_sqft'] = df2['price_per_sqft'].mean()

    # Filter price to df_final
    df_final = df2[df2['price_per_sqft'] < df2['avg_price_per_sqft']]

    # Write new csv file
    df_final.to_csv(output_file, index=False)

if __name__ == "__main__":
    process_sales_data(f"{path}/sales_data.csv", f"{path}/output_sales_data.csv")