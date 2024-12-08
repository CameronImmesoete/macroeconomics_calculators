# bop_calculator.py

import argparse


def calculate_bop(current_account, capital_account, financial_account):
    # BoP should theoretically sum to zero (with statistical discrepancy).
    total_bop = current_account + capital_account + financial_account
    return total_bop


def main():
    print("Starting Balance of Payments (BoP) Calculator...")
    parser = argparse.ArgumentParser(
        description="Calculate the overall Balance of Payments."
    )
    parser.add_argument(
        "--current_account", type=float, default=50.0, help="Current account balance"
    )
    parser.add_argument(
        "--capital_account", type=float, default=10.0, help="Capital account balance"
    )
    parser.add_argument(
        "--financial_account",
        type=float,
        default=-60.0,
        help="Financial account balance",
    )

    args = parser.parse_args()
    bop_total = calculate_bop(
        args.current_account, args.capital_account, args.financial_account
    )

    print("\nBalance of Payments Calculation Result:")
    print(f"Current Account: {args.current_account:.2f}")
    print(f"Capital Account: {args.capital_account:.2f}")
    print(f"Financial Account: {args.financial_account:.2f}")
    print(f"Overall BoP: {bop_total:.2f} (Ideally close to 0)")


if __name__ == "__main__":
    main()
