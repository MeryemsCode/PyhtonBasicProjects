def salaryCal():

    salary = float(input("Please enter the current salary"))

    if salary < 0:
        return("invalid value")
    else:
        if 0 < salary <= 3000:
            salary = salary + salary * 0.4
        elif salary <= 5000:
            salary = salary + salary * 0.35
        elif salary <= 7000:
            salary = salary + salary * 0.3
        else:
            salary = salary + salary * 0.25

        return ("New salary:",salary)


new_salary = salaryCal()
print(new_salary)