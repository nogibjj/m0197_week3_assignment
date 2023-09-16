"""
    Visualize data using a polar scatter plot with Seaborn

    Parameters:
    - data: DataFrame containing the data.
    - x_col: Column name for the x-axis.
    - y_col: Column name for the y-axis.
    - title: Title of the plot.
    - x_label: Label for the x-axis.
    - y_label: Label for the y-axis.
    - color_by: Column name for categorical variable.
    """

import seaborn as sns
import matplotlib.pyplot as plt


def visualize_polar_data(data, x_col, y_col, title, x_label, y_label, color_by=None):

    fig, ax = plt.subplots()

    x = data[x_col]
    y = data[y_col]

    sns.scatterplot(x=x, y=y, hue=color_by, data=data, ax=ax)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)

    if color_by is not None:
        plt.legend(title=color_by)

    # assuming plots folder exists
    plot_name = f"plots/{title}.png"
    plt.savefig(plot_name)