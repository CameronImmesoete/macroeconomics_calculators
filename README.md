# Macroeconomic Calculators

This repository contains a collection of macroeconomic calculators implemented in Python. These tools are designed to assist students, economists, and researchers in performing essential calculations related to macroeconomic concepts such as GDP, inflation rate, unemployment rate, and various economic models.

## **Give it a try!**

Try these out on my website: https://immesoete.cam/tools/macroeconomics/

## **Calculators Included**

1. **GDP Calculator** (`gdp_calculator.py`)
    - Calculates Gross Domestic Product (GDP) using the expenditure approach.
    - **Inputs:**
      - Consumption (C)
      - Investment (I)
      - Government Spending (G)
      - Net Exports (NX)
    - **Outputs:**
      - GDP

2. **Inflation Rate Calculator** (`inflation_rate_calculator.py`)
    - Calculates the inflation rate based on price indices.
    - **Inputs:**
      - Current period price index
      - Previous period price index
    - **Outputs:**
      - Inflation Rate (%)

3. **Unemployment Rate Calculator** (`unemployment_rate_calculator.py`)
    - Calculates the unemployment rate.
    - **Inputs:**
      - Number of unemployed individuals
      - Total labor force
    - **Outputs:**
      - Unemployment Rate (%)

4. **Fiscal Multiplier Calculator** (`fiscal_multiplier_calculator.py`)
    - Calculates the spending and tax multipliers based on the Marginal Propensity to Consume (MPC).
    - **Inputs:**
      - Marginal Propensity to Consume (MPC)
    - **Outputs:**
      - Spending Multiplier
      - Tax Multiplier

5. **Exchange Rate Calculator** (`exchange_rate_calculator.py`)
    - Converts currency amounts based on exchange rates.
    - **Inputs:**
      - Amount in base currency
      - Exchange rate (target currency per base currency)
    - **Outputs:**
      - Converted amount in target currency

6. **Interest Rate Calculator** (`interest_rate_calculator.py`)
    - Calculates future value with compound interest.
    - **Inputs:**
      - Principal amount
      - Interest rate per period
      - Number of compounding periods
    - **Outputs:**
      - Future Value

7. **Balance of Payments Calculator** (`bop_calculator.py`)
    - Calculates the total Balance of Payments (BoP).
    - **Inputs:**
      - Current account balance
      - Capital account balance
      - Financial account balance
    - **Outputs:**
      - Overall BoP (ideally close to zero)

8. **Phillips Curve Calculator** (`phillips_curve_calculator.py`)
    - Calculates inflation given unemployment using the Phillips Curve.
    - **Inputs:**
      - Inflation intercept
      - Inflation slope
      - Unemployment rate (%)
    - **Outputs:**
      - Predicted inflation rate (%)

9. **IS-LM Model Calculator** (`is_lm_calculator.py`)
    - Finds equilibrium interest rate and output in the IS-LM model.
    - **Inputs:**
      - IS curve intercept
      - IS curve slope
      - LM curve intercept
      - LM curve slope
    - **Outputs:**
      - Equilibrium output (Y)
      - Equilibrium interest rate (r)

10. **AD-AS Model Calculator** (`ad_as_calculator.py`)
     - Calculates equilibrium output and price level in the AD-AS model.
     - **Inputs:**
       - Aggregate Demand (AD) curve intercept
       - AD curve slope
       - Aggregate Supply (AS) curve intercept
       - AS curve slope
     - **Outputs:**
       - Equilibrium output (Y)
       - Equilibrium price level (P)

## **Getting Started**

### **Prerequisites**

- Python 3.x
- Required Python package:
  - `argparse` (usually included with Python)

### **Usage**

To use any of the calculators, run the corresponding Python script from the command line with optional arguments. For example, to use the GDP calculator:

```bash
python gdp_calculator.py --consumption 1500 --investment 600 --government 400 --net_exports 100
```

If no arguments are provided, default values will be used. Use the `-h` flag with any script to see all available options:

```bash
python gdp_calculator.py -h
```

### **License**

This project is licensed under the MIT License. See the `LICENSE` file for more details.

### **Contact**

For any questions or feedback, please contact Cam.
