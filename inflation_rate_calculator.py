# inflation_rate_calculator.py

import argparse


def calculate_inflation_rate(index_current, index_previous):
    if index_previous == 0:
        return None
    return ((index_current - index_previous) / index_previous) * 100


def main():
    print("Starting Inflation Rate Calculator...")
    parser = argparse.ArgumentParser(
        description="Calculate Inflation Rate based on price indices."
    )
    parser.add_argument(
        "--index_current",
        type=float,
        default=120.0,
        help="Current period price index (e.g., CPI)",
    )
    parser.add_argument(
        "--index_previous",
        type=float,
        default=100.0,
        help="Previous period price index (e.g., CPI)",
    )

    args = parser.parse_args()
    inflation_rate = calculate_inflation_rate(args.index_current, args.index_previous)

    if inflation_rate is None:
        print("Error: Previous period index cannot be zero.")
    else:
        print("\nInflation Rate Calculation Result:")
        print(f"Inflation Rate: {inflation_rate:.2f}%")


if __name__ == "__main__":
    main()
