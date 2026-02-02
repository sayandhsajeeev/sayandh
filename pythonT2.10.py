def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

num = int(input("Enter a number: "))

total = 0
temp = num

while temp > 0:
    digit = temp % 10
    total += factorial(digit)
    temp //= 10

if total == num:
    print("Gate opens! Iron-sealed number")
else:
    print("Gate remains closed")
