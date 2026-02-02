n = int(input("Enter number of students: "))

full_fee = 0
seventyfive_fee = 0
half_fee = 0

for i in range(1, n + 1):
    attendance = float(input(f"Enter attendance percentage of student {i}: "))

    if attendance >= 90:
        print("Mess Fee: Full Fee")
        full_fee += 1
    elif attendance >= 75:
        print("Mess Fee: 75% Fee")
        seventyfive_fee += 1
    else:
        print("Mess Fee: 50% Fee")
        half_fee += 1

print("\n--- Mess Fee Summary ---")
print("Full Fee students:", full_fee)
print("75% Fee students:", seventyfive_fee)
print("50% Fee students:")