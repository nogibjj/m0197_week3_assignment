"""
Visualise the dataset from the visualizer script functions 

"""


from src.visualizer import visualize_polar_data

import polars as pl

# Read the dataset using the Polar library
data = pl.read_csv("datasets/cereal.csv")

# Visualize the data using a polar scatter plot
visualize_polar_data(data, x_col="rating",
                y_col="calories",
                title="calories and ratings",
                x_label="Item Ratings",
                y_label="Calories")

visualize_polar_data(data, x_col="rating",
                y_col="calories",
                title=" Calories and ratings by mfr",
                x_label="Item Ratings",
                y_label="Calories",
                color_by="mfr"
                )
visualize_polar_data(data, x_col="rating",
                y_col="carbo",
                title="carbohydrates and ratings of the Product",
                x_label="Item Ratings",
                y_label="Item Carbohydrates")

visualize_polar_data(data, x_col="rating",
                y_col="carbo",
                title="carbohydrates and ratings of the Product by mfr",
                x_label="Item Ratings",
                y_label="Item Carbohydrates",
                color_by = "mfr")
visualize_polar_data(data, x_col="rating",
                y_col="sodium",
                title="Sodium and ratings of the Product",
                x_label="Item Ratings",
                y_label="Item Sodium")

