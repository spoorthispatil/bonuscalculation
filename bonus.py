import sys
if len(sys.argv) == 2:
    script_name = sys.argv[0]
    salary = float(sys.argv[1])
    print("User provided salary:")
else:
    script_name = sys.argv[0]
    salary = 50000.0  # default salary
    print("No input given - using default salary:")
bonus = salary * 0.10
total_salary = salary + bonus
print("Script Name:", script_name)
print("Basic Salary:", salary)
print("Bonus Amount (10%):", bonus)
print("Total Salary (with Bonus):", total_salary)
