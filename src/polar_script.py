"""
Polar function to display descriptive statistics for any file and specified or
 non specified columns

"""

import polars as pl

import markdown


def descriptive_statistics_1(csv_file_path, selected_columns=None):
    try:
        df = pl.read_csv(csv_file_path)

        if selected_columns is None:
            numeric_columns = df.select(pl.col(pl.NUMERIC_DTYPES))
        else:
            numeric_columns = df[selected_columns]

        # Initialize variables outside the loop
        mean = None
        median = None
        std = None

        for col in numeric_columns.columns:
            series = numeric_columns[col]

            # Calculate mean, median, and std for each column
            col_mean = series.mean()
            col_median = series.median()
            col_std = series.std()

            # Accumulate results
            if mean is None:
                mean = col_mean
                median = col_median
                std = col_std
            else:
                mean += col_mean
                median += col_median
                std += col_std

        # Calculate the final mean, median, and std
        num_columns = len(numeric_columns.columns)
        mean /= num_columns
        median /= num_columns
        std /= num_columns

    except FileNotFoundError:
        print("The file was not found.")
        return None, None, None

    return mean, median, std

def get_descriptive_stats(csv_file_path):
   
   df = pl.read_csv(csv_file_path)
   #numeric_columns = df.select(pl.col_is_numeric())
   descriptive_stats = df.describe()
   
   return descriptive_stats

def descriptive_stats_to_markdown_table(descriptive_stats):
   
   pandas_df = descriptive_stats.to_pandas()
   markdown_table = pandas_df.to_markdown()
   
   return markdown_table


if __name__ == "__main__":
    csv_file_path = "datasets/cereal.csv"
    selected_columns = ["calories"]

#     mean_str, median_str, std_str = descriptive_statistics(csv_file_path,
#  selected_columns)
#     mean_str = str(mean_str)
#     median_str = str(median_str)
#     std_str = str(std_str)
    descriptive_stats = get_descriptive_stats(csv_file_path)
    markdown_table = descriptive_stats_to_markdown_table(descriptive_stats)
    with open("descriptive_stats.md", "w") as f:
        f.write(markdown_table)

