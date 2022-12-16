#Write a program that reads the base salary per day from the command line and
# calculate the salary of an employee per month. assume 30 days per month. Then
# output the total pay due

# Modify the above program to assume a random loss of pay days between 0 & 4
# and subtract the salary and print the following:
#  salary per day
#  number of days absent
#  amount lost
#  that month salary




salary=int(input("Enter base salary per day :"))
absent=int(input("Enter No.of days he absent  :"))

Emp_salary=salary*30
amountLost=absent*salary
takeHomeSalary=Emp_salary-amountLost
print("salary per day : ", salary ,'\n',
" No.of days he absent : ", absent, '\n',
" amount he lost : ", amountLost  ,'\n',
' total Salary : ', Emp_salary, '\n',
' final take home Salary : '   , takeHomeSalary )


