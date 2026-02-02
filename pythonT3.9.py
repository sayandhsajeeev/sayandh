n = int(input("Enter number of users: "))

extra_charges = 0

for i in range(1, n + 1):
    usage = float(input(f"Enter data usage of user {i} (in GB): "))

    if usage <= 1:
        print("Usage Status: Normal")
    elif usage <= 2:
        print("Usage Status: Warning")
    else:
        print("Usage Status: Extra Charges")
        extra_charges += 1

print("\nNumber of users with extra charges:", extra_charges)
