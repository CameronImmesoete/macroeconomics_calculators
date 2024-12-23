# is_lm_calculator.py

import argparse
import matplotlib
import numpy as np


def calculate_equilibrium(is_intercept, is_slope, lm_intercept, lm_slope):
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


def apply_shift(intercept, slope, shift):
    return intercept + shift.get("intercept", 0), slope + shift.get("slope", 0)


def plot_is_lm(is_params, lm_params, shifts, equilibria):
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    Y_max = max([eq[0] for eq in equilibria.values() if eq[0] is not None] + [100])
    Y = np.linspace(0, Y_max * 1.5, 500)
    colors = ["blue", "green", "orange", "purple"]

    plt.figure(figsize=(8, 6))
    plt.plot(Y, is_params["intercept"] - is_params["slope"] * Y, label="IS", color=colors[0])
    plt.plot(Y, lm_params["intercept"] + lm_params["slope"] * Y, label="LM", color=colors[1])

    for idx, shift in enumerate(shifts, 2):
        is_shifted = (is_params["intercept"] + shift.get("is_shift_intercept", 0)) - (is_params["slope"] + shift.get("is_shift_slope", 0)) * Y
        lm_shifted = (lm_params["intercept"] + shift.get("lm_shift_intercept", 0)) + (lm_params["slope"] + shift.get("lm_shift_slope", 0)) * Y
        plt.plot(Y, is_shifted, label=f"IS Shift {idx-1}", linestyle="--", color=colors[idx])
        plt.plot(Y, lm_shifted, label=f"LM Shift {idx-1}", linestyle="--", color=colors[idx])

    for key, (Y_eq, r_eq) in equilibria.items():
        if Y_eq is not None:
            plt.plot(Y_eq, r_eq, "o", label=f"{key} Equilibrium")

    plt.title("IS-LM Model with Shifts")
    plt.xlabel("Output (Y)")
    plt.ylabel("Interest Rate (r)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("IS_LM_Shifts_Graph.png")
    print("IS_LM_Shifts_Graph chart saved as 'IS_LM_Shifts_Graph.png'")


def main():
    print("Starting IS-LM Model Calculator with Shifts...")
    parser = argparse.ArgumentParser(
        description="Find equilibrium interest rate and output in IS-LM model with curve shifts."
    )
    parser.add_argument(
        "--is_intercept", type=float, default=10.0, help="IS curve intercept"
    )
    parser.add_argument("--is_slope", type=float, default=0.5, help="IS curve slope")
    parser.add_argument(
        "--lm_intercept", type=float, default=2.0, help="LM curve intercept"
    )
    parser.add_argument("--lm_slope", type=float, default=0.2, help="LM curve slope")
    for i in range(1, 4):
        parser.add_argument(
            f"--shift{i}_type",
            choices=["IS", "LM"],
            help=f"Shift {i} type: IS or LM",
        )
        parser.add_argument(
            f"--shift{i}_direction",
            choices=["intercept", "slope"],
            help=f"Shift {i} direction: intercept or slope",
        )
        parser.add_argument(
            f"--shift{i}_value",
            type=float,
            help=f"Shift {i} value",
        )

    args = parser.parse_args()

    is_params = {"intercept": args.is_intercept, "slope": args.is_slope}
    lm_params = {"intercept": args.lm_intercept, "slope": args.lm_slope}

    shifts = []
    for i in range(1, 4):
        shift_type = getattr(args, f"shift{i}_type")
        direction = getattr(args, f"shift{i}_direction")
        value = getattr(args, f"shift{i}_value")
        if shift_type and direction and value is not None:
            shift = {}
            if shift_type == "IS":
                if direction == "intercept":
                    shift["is_shift_intercept"] = value
                else:
                    shift["is_shift_slope"] = value
            else:
                if direction == "intercept":
                    shift["lm_shift_intercept"] = value
                else:
                    shift["lm_shift_slope"] = value
            shifts.append(shift)

    equilibria = {"Base": calculate_equilibrium(is_params["intercept"], is_params["slope"], lm_params["intercept"], lm_params["slope"])}
    for idx, shift in enumerate(shifts, 1):
        new_is_intercept = is_params["intercept"] + shift.get("is_shift_intercept", 0)
        new_is_slope = is_params["slope"] + shift.get("is_shift_slope", 0)
        new_lm_intercept = lm_params["intercept"] + shift.get("lm_shift_intercept", 0)
        new_lm_slope = lm_params["slope"] + shift.get("lm_shift_slope", 0)
        Y_eq, r_eq = calculate_equilibrium(new_is_intercept, new_is_slope, new_lm_intercept, new_lm_slope)
        equilibria[f"Shift {idx}"] = (Y_eq, r_eq)

    for key, (Y_eq, r_eq) in equilibria.items():
        if Y_eq is None:
            print(f"{key} Equilibrium: Undefined")
        else:
            print(f"{key} Equilibrium: Y* = {Y_eq:.2f}, r* = {r_eq:.2f}")

    plot_is_lm(is_params, lm_params, shifts, equilibria)


if __name__ == "__main__":
    main()
