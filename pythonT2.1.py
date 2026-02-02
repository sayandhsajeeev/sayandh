n = int(input("Enter the nuumber of days:"))

a,b = 1,1


print("Number of leaves each days:")

if n >= 1:
    print("day 1:", a)
if n >= 2:
    print("day 2:", b)

for i in range (3, n + 1):
    c = a + b
    print(f"day {i}:", c)
    a, b = b, c
    