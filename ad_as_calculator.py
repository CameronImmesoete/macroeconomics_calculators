# ad_as_calculator.py

import argparse
import numpy as np


def calculate_equilibrium(ad_intercept, ad_slope, as_intercept, as_slope):
    # Solve for equilibrium: ad: P = ad_intercept - ad_slope*Y, as: P = as_intercept + as_slope*Y
    # at equilibrium: ad_intercept - ad_slope*Y = as_intercept + as_slope*Y
    # => ad_intercept - as_intercept = ad_slope*Y + as_slope*Y
    # => Y = (ad_intercept - as_intercept)/(ad_slope + as_slope)
    denominator = ad_slope + as_slope
    if denominator == 0:
        return None, None
    Y_eq = (ad_intercept - as_intercept) / denominator
    P_eq = ad_intercept - ad_slope * Y_eq
    return Y_eq, P_eq


def plot_ad_as(ad_intercept, ad_slope, as_intercept, as_slope, Y_eq, P_eq):
    import matplotlib

    matplotlib.use("Agg")  # Set backend to save plots as PNG
    import matplotlib.pyplot as plt

    Y = np.linspace(0, Y_eq * 2, 500)
    AD = ad_intercept - ad_slope * Y
    AS = as_intercept + as_slope * Y

    plt.figure(figsize=(8, 6))
    plt.plot(Y, AD, label="Aggregate Demand (AD)")
    plt.plot(Y, AS, label="Aggregate Supply (AS)")
    plt.plot([Y_eq], [P_eq], "ro", label="Equilibrium Point")
    plt.title("AD-AS Model")
    plt.xlabel("Output (Y)")
    plt.ylabel("Price Level (P)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("AS_AD_GDP.png")
    print("AS_AD_GDP chart saved as 'AS_AD_GDP.png'")


def main():
    print("Starting AD-AS Model Calculator...")
    parser = argparse.ArgumentParser(
        description="Calculate equilibrium output and price level in AD-AS model."
    )
    parser.add_argument(
        "--ad_intercept", type=float, default=100.0, help="AD curve intercept"
    )
    parser.add_argument("--ad_slope", type=float, default=0.5, help="AD curve slope")
    parser.add_argument(
        "--as_intercept", type=float, default=20.0, help="AS curve intercept"
    )
    parser.add_argument("--as_slope", type=float, default=0.3, help="AS curve slope")

    args = parser.parse_args()
    Y_eq, P_eq = calculate_equilibrium(
        args.ad_intercept, args.ad_slope, args.as_intercept, args.as_slope
    )

    if Y_eq is None:
        print("Error: Slope sum cannot be zero, cannot find equilibrium.")
    else:
        print("\nAD-AS Model Equilibrium Result:")
        print(f"Equilibrium Output (Y*): {Y_eq:.2f}")
        print(f"Equilibrium Price Level (P*): {P_eq:.2f}")
        plot_ad_as(
            args.ad_intercept,
            args.ad_slope,
            args.as_intercept,
            args.as_slope,
            Y_eq,
            P_eq,
        )


if __name__ == "__main__":
    main()
