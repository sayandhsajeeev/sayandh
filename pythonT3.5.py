n = int(input("Enter number of students: "))

distinction = 0
pass_count = 0
fail = 0

for i in range(1, n + 1):
    marks = int(input(f"Enter marks of student {i}: "))

    if marks >= 75:
        print("Result: Distinction")
        distinction += 1
    elif marks >= 50:
        print("Result: Pass")
        pass_count += 1
    else:
        print("Result: Fail")
        fail += 1

print("\n--- Result Summary ---")
print("Distinction:", distinction)
print("Pass:", pass_count)
print("Fail:", fail)
