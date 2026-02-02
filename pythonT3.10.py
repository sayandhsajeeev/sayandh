n = int(input("Enter number of students: "))

base_amount = 1000

concession_50 = 0
concession_25 = 0
no_concession = 0

for i in range(1, n + 1):
    age = int(input(f"Enter age of student {i}: "))

    if age < 18:
        payable = base_amount * 0.50
        print("50% c:")
