# unemployment_rate_calculator.py

import argparse


def calculate_unemployment_rate(unemployed, labor_force):
    if labor_force == 0:
        return None
    return (unemployed / labor_force) * 100


def main():
    print("Starting Unemployment Rate Calculator...")
    parser = argparse.ArgumentParser(description="Calculate the Unemployment Rate.")
    parser.add_argument(
        "--unemployed",
        type=float,
        default=50.0,
        help="Number of unemployed individuals",
    )
    parser.add_argument(
        "--labor_force", type=float, default=1000.0, help="Total labor force"
    )

    args = parser.parse_args()
    rate = calculate_unemployment_rate(args.unemployed, args.labor_force)

    if rate is None:
        print("Error: Labor force cannot be zero.")
    else:
        print("\nUnemployment Rate Calculation Result:")
        print(f"Unemployment Rate: {rate:.2f}%")


if __name__ == "__main__":
    main()
