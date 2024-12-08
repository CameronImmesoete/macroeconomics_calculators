# gdp_calculator.py

import argparse


def calculate_gdp(consumption, investment, government, net_exports):
    # Simple expenditure approach: GDP = C + I + G + NX
    return consumption + investment + government + net_exports


def main():
    print("Starting GDP Calculator...")
    parser = argparse.ArgumentParser(
        description="Calculate GDP (Expenditure Approach)."
    )
    parser.add_argument(
        "--consumption", type=float, default=1000.0, help="Consumption (C)"
    )
    parser.add_argument(
        "--investment", type=float, default=500.0, help="Investment (I)"
    )
    parser.add_argument(
        "--government", type=float, default=300.0, help="Government Spending (G)"
    )
    parser.add_argument(
        "--net_exports",
        type=float,
        default=50.0,
        help="Net Exports (NX) = Exports - Imports",
    )

    args = parser.parse_args()
    gdp = calculate_gdp(
        args.consumption, args.investment, args.government, args.net_exports
    )

    print("\nGDP Calculation Result:")
    print(f"GDP: ${gdp:.2f}")


if __name__ == "__main__":
    main()
