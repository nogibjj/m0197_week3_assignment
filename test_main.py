"""
Testing the descriptive stats function

"""

from src.polar_script import descriptive_statistics
from io import StringIO
import sys

def test_stats():
    sys.stdout = StringIO()

    csv_file_path = "datasets/cereal.csv"
    selected_columns = ["calories"]

    mean, median, std = descriptive_statistics(csv_file_path,
                                                         selected_columns)
    # mean_str = str(mean)
    # median_str = str(median)
    # std_str = str(std)
    print(f"Mean: {mean}, Median: {median}, SD: {std}")

    printed_message = sys.stdout.getvalue().strip()
    sys.stdout = sys.__stdout__

    expected_output = 'Mean: 105.54054054054055, Median: 110.0, SD: 18.442200853112762'

    assert printed_message == expected_output

if __name__ == "__main__":
    test_stats()