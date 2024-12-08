# interest_rate_calculator.py

import argparse


def calculate_future_value(principal, rate, periods):
    # Compound interest: FV = P * (1 + r)^n
    return principal * ((1 + rate) ** periods)


def main():
    print("Starting Interest Rate Calculator...")
    parser = argparse.ArgumentParser(
        description="Calculate future value with compound interest."
    )
    parser.add_argument(
        "--principal", type=float, default=1000.0, help="Initial principal"
    )
    parser.add_argument(
        "--rate",
        type=float,
        default=0.05,
        help="Interest rate per period (decimal form)",
    )
    parser.add_argument(
        "--periods", type=int, default=10, help="Number of compounding periods"
    )

    args = parser.parse_args()
    fv = calculate_future_value(args.principal, args.rate, args.periods)

    print("\nInterest Rate Calculation Result:")
    print(f"Future Value after {args.periods} periods: ${fv:.2f}")


if __name__ == "__main__":
    main()
