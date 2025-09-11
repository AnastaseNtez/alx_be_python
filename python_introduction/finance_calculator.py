#This script will calculate the user’s monthly savings based on inputted monthly income and expenses
monthly_income = int(input("Enter your monthly income: "))
total_monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - total_monthly_expenses
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)
print("your monthly savings are $"+str(monthly_savings)+".")
print("Projected savings after one year, with interest, is: $"+str(int(projected_savings))+".")