num = int(input("Enter a number: "))

digits = str(num)
count = len(digits)

total = 0

for d in digits:
    total += int(d) ** count
    
    if total > num:
        print("Vault rejects the number ")
        break
else:
    if total == num:
        print("Vault opens! Rare number found")
    else:
        print("Vault rejects the number")
