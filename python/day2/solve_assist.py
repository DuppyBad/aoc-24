def is_monotonic_with_constraints(levels):
    """
    Check if levels are either strictly increasing or strictly decreasing
    with differences between 1 and 3 inclusive.

    Args:
        levels (list): List of integers representing reactor levels

    Returns:
        bool: True if the levels follow safety rules, False otherwise
    """
    # First, determine if sequence should be increasing or decreasing
    # by checking first two numbers
    if len(levels) < 2:
        return True

    differences = []
    for i in range(1, len(levels)):
        diff = levels[i] - levels[i - 1]
        differences.append(diff)

    # Check if all differences are positive (increasing) or negative (decreasing)
    all_increasing = all(diff > 0 for diff in differences)
    all_decreasing = all(diff < 0 for diff in differences)

    # If neither all increasing nor all decreasing, report is unsafe
    if not (all_increasing or all_decreasing):
        return False

    # Check if all differences are between 1 and 3 inclusive
    return all(1 <= abs(diff) <= 3 for diff in differences)


def analyze_reactor_safety_from_file(filename):
    """
    Read reactor safety reports from a file and analyze them.

    Args:
        filename (str): Path to the text file containing the reports

    Returns:
        tuple: (number of safe reports, total number of reports)

    Raises:
        FileNotFoundError: If the specified file doesn't exist
        ValueError: If the file contains invalid data format
    """
    try:
        with open(filename, "r") as file:
            # Read all lines and remove any empty lines
            reports = [line.strip() for line in file if line.strip()]

        safe_count = 0
        total_reports = len(reports)

        # Process each report
        print("\nAnalyzing reactor safety reports...")
        print("-" * 50)

        for i, report in enumerate(reports, 1):
            try:
                # Convert the line of numbers into a list of integers
                levels = list(map(int, report.split()))

                # Check if the report is safe
                is_safe = is_monotonic_with_constraints(levels)
                status = "Safe" if is_safe else "Unsafe"

                if is_safe:
                    safe_count += 1

                print(f"Report {i} ({levels}): {status}")

            except ValueError as e:
                print(f"Error in Report {i}: Invalid number format")
                continue

        print("-" * 50)
        print(f"\nAnalysis Summary:")
        print(f"Total reports processed: {total_reports}")
        print(f"Number of safe reports: {safe_count}")
        print(f"Number of unsafe reports: {total_reports - safe_count}")

        return safe_count, total_reports

    except FileNotFoundError:
        print(f"Error: Could not find file '{filename}'")
        return 0, 0
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        return 0, 0


# Example usage
if __name__ == "__main__":
    # You can change this to the path of your text file
    filename = "input.txt"

    print(f"Reading reactor safety reports from '{filename}'...")
    safe_count, total_reports = analyze_reactor_safety_from_file(filename)

    if total_reports > 0:
        percentage_safe = (safe_count / total_reports) * 100
        print(f"\nSafety Rate: {percentage_safe:.1f}%")
