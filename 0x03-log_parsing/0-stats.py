#!/usr/bin/python3
"""
stats module
"""
from sys import stdin

# Initialize a dictionary to store status codes and their counts
status_code_counts = {'200': 0, '301': 0, '400': 0, '401': 0,
                     '403': 0, '404': 0, '405': 0, '500': 0}

# Initialize a variable to store the total size of files
total_file_size = 0

def print_info():
    """
    print_info method print needed info
    Args:
        codes (dict): code status
        size (int): size of files
    """
    print("File size: {}".format(total_file_size))
    for code, count in sorted(status_code_counts.items()):
        if count > 0:
            print("{}: {}".format(code, count))

if __name__ == '__main__':
    try:
        # Read input from stdin line by line
        for line_number, line in enumerate(stdin, 1):
            try:
                # Split the line into tokens
                tokens = line.split()
                # Extract file size from the last token of the split
                # line and add it to total_file_size
                total_file_size += int(tokens[-1])
                # Check if the status code is in the dictionary
                # keys and increment its count if so
                if tokens[-2] in status_code_counts.keys():
                    status_code_counts[tokens[-2]] += 1
            except Exception:
                pass
            # Print statistics after every 10 lines
            if line_number % 10 == 0:
                print_info()
    except KeyboardInterrupt:
        # Handle KeyboardInterrupt by printing the
        # statistics and re-raising the exception
        print_info()
        raise
    # Print final statistics
    print_info()
