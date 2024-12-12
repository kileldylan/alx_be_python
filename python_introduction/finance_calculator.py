# User Input for Financial Details
monthly_income = float(input("Enter your monthly income: "))  # Using float to allow for decimal input
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate Monthly Savings
monthly_savings = monthly_income - monthly_expenses

# Project Annual Savings with Interest (5%)
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Output Results
print("Your monthly savings are: ", monthly_savings)
print("Projected savings after one year, with interest, is: ", projected_savings)
