n = int(input("Enter number of students: "))

count_A = 0
count_B = 0
count_C = 0
count_F = 0

for i in range(1, n + 1):
    marks = int(input(f"Enter marks of student {i}: "))

    if marks >= 90:
        grade = "A"
        count_A += 1
    elif marks >= 75:
        grade = "B"
        count_B += 1
    elif marks >= 50:
        grade = "C"
        count_C += 1
    else:
        grade = "Fail"
        count_F += 1

    print(f"Student {i} Grade: {grade}")

print("\nGrade Summary:")
print("A Grade:", count_A)
print("B Grade:", count_B)
print("C Grade:", count_C)
print("Fail:", count_F)
