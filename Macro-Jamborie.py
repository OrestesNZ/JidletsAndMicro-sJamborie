#New file push, 
#new files
#git add Macro-Jamborie.py
#git commit -m "Initial commit of Macro-Jamborie.py"
#git push origin main

#update file
# save file
# git add Macro-Jamborie.py 
# git commit -m "Updated logic in Macro-Jamborie.py"
# git push origin main

# Define companies 'Vitals' 
# Tech Start up called Macro-Jamborie

# Financial Vitals
# Financial Vitals
total_assets = 600000  # Cash, equipment, etc.
total_liabilities = 200000  # Loans, bills to pay
annual_cash_flow = 75000  # Money left over at the end of the year
shares_outstanding = 10000  # Total number of stock "slices"

# equity value (Book value)
equity_value = total_assets - total_liabilities

# to get market value, we often use a multiple of cash flow, say 10x for a tech startup (industry based)
# earnings based value = annual_cash_flow * 10
# total coompany value = equity value + earnings based value
total_company_value = equity_value + (annual_cash_flow * 10)
#print(f"Total Company Value: ${total_company_value}")

# whole pizzq, now we want to find what slice is worth 
# divide total value by shares outstanding
total_sharesoutstanding = 90000
value_per_share = total_company_value / total_sharesoutstanding
#print(f"Value Per Share: ${value_per_share}")

# risk (margin of safety)
risk_margin = 0.2  # 20% margin of safety
adjusted_value_per_share = value_per_share * (1 - risk_margin)
#print(f"Adjusted Value Per Share (with margin of safety): ${adjusted_value_per_share}")

# "what if" machine - sensitivity analysis
# if cash flow multiple changes from 10x to 5x 
def calculate_intrinstic_value(cash_flow, assets, liabilities, shares, multiple=10, margin=0.2):
    # Calculate Equity (Book Value)
    equity_value = assets - liabilities
    # Calculate Total Value (Equity + Multiplier effect)
    total_company_value = equity_value + (cash_flow * multiple)
    # Calculate Per Share
    price_per_share = total_company_value / shares
    # Apply Margin of Safety
    safe_price = price_per_share * (1 - margin)
    return safe_price

intrinsic_value = calculate_intrinstic_value(annual_cash_flow, total_assets, total_liabilities, shares_outstanding, multiple=5, margin=0.4)
#print(f"Intrinsic Value Per Share with 5x multiple and 40% margin of safety: ${intrinsic_value}")

#compare to real stock price
"""
market_price = 50 
if intrinsic_value > market_price:
    print("The stock is undervalued. Consider buying.")
else:
    print("The stock is overvalued. Consider waiting or selling.")

#calculate a 10% buffer
upper_bound = intrinsic_value * 1.1
lower_bound = intrinsic_value * 0.9

if market_price < lower_bound:
    print("🟢 The stock is significantly undervalued. Strong buy signal.")
elif lower_bound <= market_price <= upper_bound: # chained comparison. Market price is between lower and upper bound = True
    print("🟡The stock price is fairly valued.") 
else:
    print("🔴 The stock is overvalued. Consider selling.")
"""
# Terminal value 
# used to determine the value of a company for an extended period, ie 5 years. 
# instrinsic value is based on current cash flow, for one year. 
# value = next year's cash flow / (discount rate - growth rate)

discount_rate = 0.18  # 10% discount rate
growth_rate = 0.05 # 3% growth rate

terminal_value = (annual_cash_flow * (1 + growth_rate)) / (discount_rate - growth_rate)
#print(f"Terminal Value: ${terminal_value}")

def professional_valuation(cash_flow, assets, liabilities, shares, growth, discount, margin=0.2):
    # 1. Equity
    equity = assets - liabilities
    
    # 2. Terminal Value (Perpetuity)
    # We'll use a standard 3% long-term growth for this part
    terminal_val = (cash_flow * (1 + growth)) / (discount - 0.03)
    
    # 3. Final Calculation
    intrinsic_value = (equity + terminal_val) / shares

    # Apply the safety buffer here
    safe_price = intrinsic_value * (1 - margin)
    return safe_price

# Let's run it!
my_value = professional_valuation(75000, 500000, 200000, 10000, 0.15, 0.12)

stocks_to_check = [
    {"name": "CloudNine", "cf": 80000, "assets": 400000, "liab": 100000, "shares": 5000, "price": 270},
    {"name": "DataDash", "cf": 50000, "assets": 200000, "liab": 50000, "shares": 10000, "price": 45},
    {"name": "CyberSec", "cf": 120000, "assets": 800000, "liab": 300000, "shares": 15000, "price": 130}
]

for stock in stocks_to_check:
    # 1. Calculate the raw Intrinsic Value
    value = professional_valuation(stock["cf"], stock["assets"], stock["liab"], stock["shares"], 0.15, 0.12)
    
    # 2. Apply a 20% Margin of Safety to get our "Target Buy Price"
    safe_buy_price = value * 0.80

for stock in stocks_to_check:
    # 1. Print the header for the specific stock the loop is currently touching
    print(f"--- Statistics for {stock['name']} ---")
    
    # 2. Loop through the items of JUST this stock
    for key, value in stock.items():
        print(f"{key}: {value}")
    
    # 3. Add a blank line to separate this stock from the next one
    print()
    # 3. Compare to the actual current Market Price
    # Which comparison should we use here to find a 'Good Deal'?
    if stock["price"] < safe_buy_price:
        print(f"🟢 {stock['name']}: BUY! Price is below our safe entry point.")
        print()
    else:
        print(f"🔴 {stock['name']}: WAIT. Price is too high.")
        print()

# Key Terms:

# Growth Rate
# Definition: The expected percentage increase in a company’s cash flow over a specific period.

# Discount Rate
# Definition: The required rate of return an investor needs to justify the risk of the investment, accounting for the Time Value of Money. Hurdle rate company needs to meet
# to justify your risk, vs bonds for example. 

# Margin of Safety
# Definition: The difference between a stock's Intrinsic Value and its Market Price. It acts as a "buffer" to protect the investor from errors in their estimate
# Doesn't change company value, but changes your willingness to buy.

