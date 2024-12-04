def is_monotonic_with_constraints(levels):
    """
    Check if levels are either strictly increasing or strictly decreasing
    with differences between 1 and 3 inclusive.

    The sequence can be of any length - we just need to verify that each adjacent
    pair follows our rules for safe operation.
    """
    if len(levels) < 2:  # Single-level sequences are considered safe
        return True

    # Calculate all differences between adjacent numbers
    differences = []
    for i in range(1, len(levels)):
        diff = levels[i] - levels[i - 1]
        differences.append(diff)

    # A sequence must be either all increasing or all decreasing
    all_increasing = all(diff > 0 for diff in differences)
    all_decreasing = all(diff < 0 for diff in differences)

    if not (all_increasing or all_decreasing):
        return False

    # Each difference must be between 1 and 3 inclusive
    return all(1 <= abs(diff) <= 3 for diff in differences)


def check_safety_with_dampener(levels):
    """
    Check if a report is safe, either directly or by removing one level using
    the Problem Dampener. Works with sequences of any length.

    The Problem Dampener can remove any single level to try to make an unsafe
    sequence safe.
    """
    # First check if the sequence is already safe without modification
    if is_monotonic_with_constraints(levels):
        return True, -1, levels

    # If not safe, try removing each level one at a time
    for i in range(len(levels)):
        # Create a new sequence without the current level
        modified_levels = levels[:i] + levels[i + 1 :]
        if is_monotonic_with_constraints(modified_levels):
            return True, i, modified_levels

    # If we couldn't make it safe even with the dampener
    return False, -1, levels


def process_reactor_file(filename):
    """
    Process reactor safety reports from a text file. Each line contains a sequence
    of numbers representing reactor levels. Sequences can be of any length.
    """
    try:
        print(f"\nAnalyzing reactor reports from: {filename}")
        print("=" * 70)

        with open(filename, "r") as file:
            # Read all non-empty lines
            reports = [line.strip() for line in file if line.strip()]

        safe_count = 0
        total_reports = len(reports)

        # Process each report
        for report_num, line in enumerate(reports, 1):
            # Convert line to list of integers
            levels = list(map(int, line.split()))

            # Check safety with Problem Dampener
            is_safe, removed_index, safe_sequence = check_safety_with_dampener(levels)

            # Print detailed results for this report
            if is_safe:
                safe_count += 1
                if removed_index == -1:
                    print(f"Report {report_num} ({len(levels)} levels): SAFE")
                    print(f"  Sequence: {levels}")
                    print("  Naturally safe - no dampening needed")
                else:
                    print(
                        f"Report {report_num} ({len(levels)} levels): SAFE with dampener"
                    )
                    print(f"  Original: {levels}")
                    print(
                        f"  Removed: {levels[removed_index]} at position {removed_index + 1}"
                    )
                    print(f"  Modified: {safe_sequence}")
            else:
                print(f"Report {report_num} ({len(levels)} levels): UNSAFE")
                print(f"  Sequence: {levels}")
                print("  Cannot be made safe even with dampener")

            print("-" * 70)

        # Print summary statistics
        print("\nFinal Analysis:")
        print(f"Total reports analyzed: {total_reports}")
        print(f"Safe reports (including dampened): {safe_count}")
        print(f"Unsafe reports: {total_reports - safe_count}")
        if total_reports > 0:
            print(f"Safety rate: {(safe_count/total_reports)*100:.1f}%")

    except FileNotFoundError:
        print(f"Error: Could not find file '{filename}'")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


# Main execution block
if __name__ == "__main__":
    filename = "input.txt"
    process_reactor_file(filename)
