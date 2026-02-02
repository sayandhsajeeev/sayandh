n = int(input("Enter number of vehicles: "))

total_fine = 0

for i in range(1, n + 1):
    speed = int(input(f"Enter speed of vehicle {i} (km/h): "))

    if speed <= 60:
        fine = 0
        print("No fine")
    elif speed <= 80:
        fine = 500
        print("Fine: ₹500")
    else:
        fine = 1000
        print("Fine: ₹1000")

    total_fine += fine

print("\nTotal fine collected: ₹", total_fine)
