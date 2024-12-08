# exchange_rate_calculator.py

import argparse


def calculate_exchange_rate(amount, rate):
    # Simple conversion: exchanged_amount = amount * rate
    return amount * rate


def main():
    print("Starting Exchange Rate Calculator...")
    parser = argparse.ArgumentParser(description="Calculate converted currency amount.")
    parser.add_argument(
        "--amount", type=float, default=100.0, help="Amount in base currency"
    )
    parser.add_argument(
        "--rate",
        type=float,
        default=1.2,
        help="Exchange rate (target currency per base currency)",
    )

    args = parser.parse_args()
    converted = calculate_exchange_rate(args.amount, args.rate)

    print("\nExchange Rate Calculation Result:")
    print(f"Converted Amount: {converted:.2f} (in target currency)")


if __name__ == "__main__":
    main()
