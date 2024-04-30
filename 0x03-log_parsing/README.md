## Readme of 0x03-log_parsing
---

The task involves creating a Python script that reads log entries from standard input (`stdin`), processes them, and computes statistics based on the log data. The input log entries follow a specific format, containing an IP address, date, HTTP request, status code, and file size. The script calculates the total file size and the count of each status code encountered in the log entries.

The script reads input line by line, splitting each line into tokens and extracting relevant information such as file size and status code. It maintains counts of status codes using a dictionary and updates the total file size accordingly. After processing every 10 lines, or when interrupted by a Ctrl+C signal, the script prints the current statistics including the total file size and the count of each status code in ascending order.

To handle keyboard interruptions gracefully, the script catches the `KeyboardInterrupt` exception, prints the current statistics, and re-raises the exception to exit cleanly.

Overall, the script effectively parses log data, computes metrics, and handles interruptions, providing useful insights into the log entries processed.
