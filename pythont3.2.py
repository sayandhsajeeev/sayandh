n = int(input("enter the number of consumers:"))
total_amount = 0

for i in range(1,n + 1):
    units = int(input("\n enter units consumed by the consumer {i}:"))

    if units <= 100:
       bill = units * 2
    elif units <= 300:
       bill = units * 3
    else:
       bill = units * 5

    print(f"Electricty bill for consumer {i}: ${bill}")
    total_amount += bill

print("\ntotal amount collected:$", total_amount)