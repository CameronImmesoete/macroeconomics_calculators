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


def apply_shift(intercept, slope, shift):
    return intercept + shift.get("intercept", 0), slope + shift.get("slope", 0)


def plot_ad_as(ad_params, as_params, shifts, equilibria):
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    Y_max = max([eq[0] for eq in equilibria.values()] + [100])
    Y = np.linspace(0, Y_max * 1.5, 500)
    colors = ["blue", "green", "orange", "purple"]

    plt.figure(figsize=(10, 8))
    plt.plot(Y, ad_params["intercept"] - ad_params["slope"] * Y, label="AD", color=colors[0])
    plt.plot(Y, as_params["intercept"] + as_params["slope"] * Y, label="AS", color=colors[1])

    for idx, shift in enumerate(shifts, 2):
        ad_shifted = ad_params["intercept"] - ad_params["slope"] * Y + shift.get("ad_shift", 0)
        as_shifted = as_params["intercept"] + as_params["slope"] * Y + shift.get("as_shift", 0)
        plt.plot(Y, ad_shifted, label=f"AD Shift {idx-1}", linestyle="--", color=colors[idx])
        plt.plot(Y, as_shifted, label=f"AS Shift {idx-1}", linestyle="--", color=colors[idx])

    for key, (Y_eq, P_eq) in equilibria.items():
        plt.plot(Y_eq, P_eq, "o", label=f"{key} Equilibrium")

    plt.title("AD-AS Model with Shifts")
    plt.xlabel("Output (Y)")
    plt.ylabel("Price Level (P)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("AS_AD_GDP_Shifts.png")
    print("AS_AD_GDP_Shifts chart saved as 'AS_AD_GDP_Shifts.png'")


def main():
    print("Starting AD-AS Model Calculator with Shifts...")
    parser = argparse.ArgumentParser(
        description="Calculate equilibrium output and price level in AD-AS model with curve shifts."
    )
    parser.add_argument(
        "--ad_intercept", type=float, default=100.0, help="AD curve intercept"
    )
    parser.add_argument("--ad_slope", type=float, default=0.5, help="AD curve slope")
    parser.add_argument(
        "--as_intercept", type=float, default=20.0, help="AS curve intercept"
    )
    parser.add_argument("--as_slope", type=float, default=0.3, help="AS curve slope")
    for i in range(1, 4):
        parser.add_argument(
            f"--shift{i}_type",
            choices=["AD", "AS"],
            help=f"Shift {i} type: AD or AS",
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

    ad_params = {"intercept": args.ad_intercept, "slope": args.ad_slope}
    as_params = {"intercept": args.as_intercept, "slope": args.as_slope}

    shifts = []
    for i in range(1, 4):
        shift_type = getattr(args, f"shift{i}_type")
        direction = getattr(args, f"shift{i}_direction")
        value = getattr(args, f"shift{i}_value")
        if shift_type and direction and value is not None:
            shift = {}
            if shift_type == "AD":
                if direction == "intercept":
                    shift["ad_shift"] = value
                else:
                    shift["ad_shift_slope"] = value
            else:
                if direction == "intercept":
                    shift["as_shift"] = value
                else:
                    shift["as_shift_slope"] = value
            shifts.append(shift)

    equilibria = {"Base": calculate_equilibrium(ad_params["intercept"], ad_params["slope"], as_params["intercept"], as_params["slope"])}
    for idx, shift in enumerate(shifts, 1):
        new_ad = ad_params["intercept"] + shift.get("ad_shift", 0)
        new_as = as_params["intercept"] + shift.get("as_shift", 0)
        Y_eq, P_eq = calculate_equilibrium(new_ad, ad_params["slope"], new_as, as_params["slope"])
        equilibria[f"Shift {idx}"] = (Y_eq, P_eq)

    for key, (Y_eq, P_eq) in equilibria.items():
        if Y_eq is None:
            print(f"{key} Equilibrium: Undefined")
        else:
            print(f"{key} Equilibrium: Y* = {Y_eq:.2f}, P* = {P_eq:.2f}")

    plot_ad_as(ad_params, as_params, shifts, equilibria)


if __name__ == "__main__":
    main()
