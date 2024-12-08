# is_lm_calculator.py

import argparse


def calculate_is_lm_equilibrium(is_intercept, is_slope, lm_intercept, lm_slope):
    # IS: r = is_intercept - is_slope*Y
    # LM: r = lm_intercept + lm_slope*Y
    # Equate: is_intercept - is_slope*Y = lm_intercept + lm_slope*Y
    # => is_intercept - lm_intercept = is_slope*Y + lm_slope*Y
    # => Y = (is_intercept - lm_intercept)/(is_slope + lm_slope)
    denominator = is_slope + lm_slope
    if denominator == 0:
        return None, None
    Y_eq = (is_intercept - lm_intercept) / denominator
    r_eq = is_intercept - is_slope * Y_eq
    return Y_eq, r_eq


def main():
    print("Starting IS-LM Model Calculator...")
    parser = argparse.ArgumentParser(
        description="Find equilibrium interest rate and output in IS-LM model."
    )
    parser.add_argument(
        "--is_intercept", type=float, default=10.0, help="IS curve intercept"
    )
    parser.add_argument("--is_slope", type=float, default=0.5, help="IS curve slope")
    parser.add_argument(
        "--lm_intercept", type=float, default=2.0, help="LM curve intercept"
    )
    parser.add_argument("--lm_slope", type=float, default=0.2, help="LM curve slope")

    args = parser.parse_args()
    Y_eq, r_eq = calculate_is_lm_equilibrium(
        args.is_intercept, args.is_slope, args.lm_intercept, args.lm_slope
    )

    if Y_eq is None:
        print("Error: Sum of slopes cannot be zero.")
    else:
        print("\nIS-LM Model Equilibrium Result:")
        print(f"Equilibrium Output (Y*): {Y_eq:.2f}")
        print(f"Equilibrium Interest Rate (r*): {r_eq:.2f}")


if __name__ == "__main__":
    main()
