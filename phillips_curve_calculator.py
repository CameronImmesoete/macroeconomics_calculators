# phillips_curve_calculator.py

import argparse
import matplotlib
import numpy as np


def calculate_phillips_relationship(inflation_intercept, inflation_slope, unemployment):
    # Simple linear Phillips curve: inflation = intercept - slope * unemployment
    return inflation_intercept - inflation_slope * unemployment


def apply_shift(intercept, slope, shift):
    if shift["type"] == "intercept":
        intercept += shift["value"]
    elif shift["type"] == "slope":
        slope += shift["value"]
    return intercept, slope


def plot_phillips_curve(
    base_params, shifts, current_unemployment, inflation_rate, equilibria
):
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    unemployment = np.linspace(0, current_unemployment * 2, 500)
    inflation_base = calculate_phillips_relationship(
        base_params["intercept"], base_params["slope"], unemployment
    )

    plt.figure(figsize=(8, 6))
    plt.plot(unemployment, inflation_base, label="Phillips Curve", color="blue")

    colors = ["green", "orange", "purple"]

    for idx, shift in enumerate(shifts):
        shifted_intercept, shifted_slope = apply_shift(
            base_params["intercept"], base_params["slope"], shift
        )
        inflation_shifted = calculate_phillips_relationship(
            shifted_intercept, shifted_slope, unemployment
        )
        plt.plot(
            unemployment,
            inflation_shifted,
            label=f"Shift {idx + 1}",
            linestyle="--",
            color=colors[idx % len(colors)],
        )

    plt.plot(
        [current_unemployment],
        [inflation_rate],
        "ro",
        label="Current Point",
    )

    for key, (unemp_eq, infl_eq) in equilibria.items():
        if unemp_eq is not None and infl_eq is not None:
            plt.plot(unemp_eq, infl_eq, "o", label=f"{key} Equilibrium")

    plt.title("Phillips Curve with Shifts")
    plt.xlabel("Unemployment Rate (%)")
    plt.ylabel("Inflation Rate (%)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("Phillips_Curve_Shifts.png")
    print("Phillips_Curve_Shifts chart saved as 'Phillips_Curve_Shifts.png'")


def main():
    print("Starting Phillips Curve Calculator with Shifts...")
    parser = argparse.ArgumentParser(
        description="Calculate inflation given unemployment using a Phillips Curve with possible shifts."
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
    for i in range(1, 4):
        parser.add_argument(
            f"--shift{i}_type",
            choices=["intercept", "slope"],
            help=f"Shift {i} type: intercept or slope",
        )
        parser.add_argument(
            f"--shift{i}_value",
            type=float,
            help=f"Shift {i} value",
        )

    args = parser.parse_args()
    base_params = {"intercept": args.inflation_intercept, "slope": args.inflation_slope}

    shifts = []
    for i in range(1, 4):
        shift_type = getattr(args, f"shift{i}_type")
        shift_value = getattr(args, f"shift{i}_value")
        if shift_type and shift_value is not None:
            shift = {"type": shift_type, "value": shift_value}
            shifts.append(shift)

    inflation_rate = calculate_phillips_relationship(
        base_params["intercept"], base_params["slope"], args.unemployment
    )

    equilibria = {"Base": (args.unemployment, inflation_rate)}
    for idx, shift in enumerate(shifts, 1):
        shifted_intercept, shifted_slope = apply_shift(
            base_params["intercept"], base_params["slope"], shift
        )
        infl_shifted = calculate_phillips_relationship(
            shifted_intercept, shifted_slope, args.unemployment
        )
        equilibria[f"Shift {idx}"] = (args.unemployment, infl_shifted)

    print("\nPhillips Curve Calculation Result:")
    print(f"Given Unemployment: {args.unemployment:.2f}%")
    print(f"Predicted Inflation: {inflation_rate:.2f}%")
    for key, (unemp, infl) in equilibria.items():
        print(f"{key} Equilibrium: Unemployment = {unemp:.2f}%, Inflation = {infl:.2f}%")

    plot_phillips_curve(
        base_params, shifts, args.unemployment, inflation_rate, equilibria
    )


if __name__ == "__main__":
    main()
