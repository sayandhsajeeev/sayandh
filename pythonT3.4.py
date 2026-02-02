n = int(input("Enter the number of coustmer:"))
discount_count = 0

for i in range(1,n + 1):
    bill = float(input(f"\n enter the bill amount by consumer {i}:"))

    if bill >= 5000:
        discount = bill * 0.20
        discount_count += 1
    elif bill >= 2000:
        discount = bill * 0.10
        discount_count += 1
    else:
         discount = 0
    final_amount = bill - discount 
    print(f"Final bil amount for coustmer {i}: ${final_amount}")

print("\nNumber of coustmer who recived discount:", discount_count)

