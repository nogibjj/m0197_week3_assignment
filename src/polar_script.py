"""
Polar function to display descriptive statistics for any file and specified or
 non specified columns

"""


import polars as pl


def descriptive_statistics(csv_file_path, selected_columns=None):
    try:
        df = pl.read_csv(csv_file_path)

        if selected_columns is None:
            numeric_columns = df.select(pl.col(pl.NUMERIC_DTYPES))
        else:
            numeric_columns = df[selected_columns]
        for col in numeric_columns.columns:
            series = numeric_columns[col]

            mean = series.mean()
            median = series.median()
            std = series.std()


    except FileNotFoundError:
        print("The file was not found.")
    return mean,median,std

#
# if __name__ == "__main__":
#     csv_file_path = "datasets/cereal.csv"
#     selected_columns = ["calories"]

#     mean_str, median_str, std_str = descriptive_statistics(csv_file_path, selected_columns)
#     mean_str = str(mean_str)
#     median_str = str(median_str)
#     std_str = str(std_str)

#     print(f"Mean: {mean_str}, Median: {median_str}, SD: {std_str}")

# prints Mean: 105.54054054054055, Median: 110.0, SD: 18.442200853112762