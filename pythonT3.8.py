n = int(input("Enter number of customers: "))

high_loan = 0
medium_loan = 0
not_eligible = 0

for i in range(1, n + 1):
    income = int(input(f"Enter annual income of customer {i} (₹): "))

    if income >= 500000:
        print("Loan Category: High Loan")
        high_loan += 1
    elif income >= 300000:
        print("Loan Category: Medium Loan")
        medium_loan += 1
    else:
        print("Loan Category: Not Eligible")
        not_eligible += 1

eligible = high_loan + medium_loan

print("\n--- Loan Eligibility Summary ---")
print("High Loan customers:", high_loan)
print("Medium Loan customers:", medium_loan)
print("Not Eligible customers:", not_eligible)
print("Total Eligible customers:", eligible)
