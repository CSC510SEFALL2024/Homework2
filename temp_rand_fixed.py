"""
This module contains a function that generates a random array by
invoking the `shuf` command to shuffle and generate random numbers.
"""

import subprocess


def random_array(arr):
    """
    Generates an array with random integers using the shuf command.

    Args:
        arr (list): A list to be filled with random integers.

    Returns:
        list: The input list filled with random integers between 1 and 20.
    """
    for i, _ in enumerate(arr):  # Using enumerate instead of range(len(arr))
        shuffled_num = subprocess.run(
            # Added check=True
            ["shuf", "-i1-20", "-n1"], capture_output=True, check=True
        )
        arr[i] = int(shuffled_num.stdout)  # Convert bytes output to integer
    return arr


# Example call to the function for testing
if __name__ == "__main__":
    print(random_array([None] * 5))  # Example usage to generate a random array
