# fiscal_multiplier_calculator.py

import argparse


def calculate_spending_multiplier(mpc):
    # Spending multiplier = 1/(1 - MPC)
    if (1 - mpc) == 0:
        return None
    return 1 / (1 - mpc)


def calculate_tax_multiplier(mpc):
    # Tax multiplier = -MPC/(1 - MPC)
    if (1 - mpc) == 0:
        return None
    return -mpc / (1 - mpc)


def main():
    print("Starting Fiscal Multiplier Calculator...")
    parser = argparse.ArgumentParser(
        description="Calculate Spending and Tax Multipliers."
    )
    parser.add_argument(
        "--mpc",
        type=float,
        default=0.8,
        help="Marginal Propensity to Consume (0 < MPC < 1)",
    )

    args = parser.parse_args()
    spending_mult = calculate_spending_multiplier(args.mpc)
    tax_mult = calculate_tax_multiplier(args.mpc)

    if spending_mult is None or tax_mult is None:
        print("Error: MPC cannot be 1.")
    else:
        print("\nFiscal Multipliers Calculation Result:")
        print(f"Spending Multiplier: {spending_mult:.2f}")
        print(f"Tax Multiplier: {tax_mult:.2f}")


if __name__ == "__main__":
    main()
