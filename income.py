def calculate_income_tax(income):
    tax = 0

    if income <= 10000:
        tax = 0
    elif income <= 50000:
        tax = (income - 10000) * 0.1
    elif income <= 100000:
        tax = 4000 + (income - 50000) * 0.2
    else:
        tax = 14000 + (income - 100000) * 0.3

    return tax

income = float(input("Enter your annual income: $"))
tax_due = calculate_income_tax(income)
print(f"Your income tax due is: ${tax_due:.2f}")
