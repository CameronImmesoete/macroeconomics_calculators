# phillips_curve_calculator.py

import argparse
import matplotlib
import numpy as np


def calculate_phillips_relationship(inflation_intercept, inflation_slope, unemployment):
    # Simple linear Phillips curve: inflation = intercept - slope * unemployment
    return inflation_intercept - inflation_slope * unemployment


def plot_phillips_curve(
    inflation_intercept, inflation_slope, current_unemployment, inflation_rate
):
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    unemployment = np.linspace(0, current_unemployment * 2, 500)
    inflation = inflation_intercept - inflation_slope * unemployment

    plt.figure(figsize=(8, 6))
    plt.plot(unemployment, inflation, label="Phillips Curve")
    plt.plot([current_unemployment], [inflation_rate], "ro", label="Current Point")
    plt.title("Phillips Curve")
    plt.xlabel("Unemployment Rate (%)")
    plt.ylabel("Inflation Rate (%)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("Phillips_Curve.png")
    print("Phillips_Curve chart saved as 'Phillips_Curve.png'")


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

    plot_phillips_curve(
        args.inflation_intercept,
        args.inflation_slope,
        args.unemployment,
        inflation_rate,
    )


if __name__ == "__main__":
    main()
