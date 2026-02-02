n = int(input("Enter number of employees: "))

total_bonus = 0

for i in range(1, n + 1):
    salary = float(input(f"Enter salary of employee {i}: "))
    years = int(input(f"Enter years of service of employee {i}: "))

    if years >= 10:
        bonus = salary * 0.20
    elif years >= 5:
        bonus = salary * 0.10
    else:
        bonus = salary * 0.05

    total_bonus += bonus

    print(f"Employee {i} Bonus: {bonus:.2f}")

print("\nTotal Bonus Paid:", total_bonus)
