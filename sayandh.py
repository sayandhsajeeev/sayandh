def generate_payroll(emp_id, total_days=30, worked_days=30, bonus=0, deduction=0):
    if emp_id not in employees:
        print("Employee not found")
        return

    emp = employees[emp_id]
    salary = calculate_salary(emp["base_salary"], total_days, worked_days)
    final_salary = apply_bonus_deduction(salary, bonus, deduction)

    print("\n--- Payroll Report ---")
    print("Employee ID:", emp_id)
    print("Name:", emp["name"])
    print("Base Salary:", emp["base_salary"])
    print("Final Salary:", final_salary)
