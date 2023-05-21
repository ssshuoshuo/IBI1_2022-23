def mortgage_affordability(value, salary):
    if value > 5 * salary:
        return "The house cannot be bought with the given salary."
    else:
        return "The house can be bought with the given salary."

# Example function calls
house_value = int(input("Enter the value of the house: "))
salary = int(input("Enter the annual salary: "))

result = mortgage_affordability(house_value, salary)
print(result)
#For example
#Enter the value of the house: 18000
#Enter the annual salary: 35000
#The house can be bought with the given salary.
