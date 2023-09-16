"""
Testing the descriptive stats function

"""

from src.polar_script import descriptive_statistics
from io import StringIO
import sys

def test_stats():
    sys.stdout = StringIO()

    csv_file_path = "/datasets/cereal.csv"
    selected_columns = ["calories"]
    mean_str, median_str, std_str = descriptive_statistics(csv_file_path,
                                                         selected_columns)
    mean_str = str(mean_str)
    median_str = str(median_str)
    std_str = str(std_str)
    print(f"Mean: {mean_str}, Median: {median_str}, SD: {std_str}")

    printed_message = sys.stdout.getvalue().strip()

    sys.stdout = sys.__stdout__

    expected_output = 'Mean: 105.54054054054055, Median: 110.0, SD: 18.442200853112762'

    assert printed_message == expected_output


if __name__ == "__main__":
    test_stats()