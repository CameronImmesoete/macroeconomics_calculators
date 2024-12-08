# phillips_curve_calculator.py

import argparse


def calculate_phillips_relationship(inflation_intercept, inflation_slope, unemployment):
    # Simple linear Phillips curve: inflation = intercept - slope * unemployment
    return inflation_intercept - inflation_slope * unemployment


def main():
    print("Starting Phillips Curve Calculator...")
    parser = argparse.ArgumentParser(
        description="Calculate inflation given unemployment using a Phillips Curve."
    )
    parser.add_argument(
        "--inflation_intercept",
        type=float,
        default=5.0,
        help="Phillips curve inflation intercept",
    )
    parser.add_argument(
        "--inflation_slope", type=float, default=0.5, help="Phillips curve slope"
    )
    parser.add_argument(
        "--unemployment", type=float, default=6.0, help="Unemployment rate (%)"
    )

    args = parser.parse_args()
    inflation_rate = calculate_phillips_relationship(
        args.inflation_intercept, args.inflation_slope, args.unemployment
    )

    print("\nPhillips Curve Calculation Result:")
    print(f"Given Unemployment: {args.unemployment:.2f}%")
    print(f"Predicted Inflation: {inflation_rate:.2f}%")


if __name__ == "__main__":
    main()
