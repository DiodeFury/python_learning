try:
    age = int(input("age: "))
    print (age)
    income = 2000
    risk = income/age
except ValueError:
    print('Invalid value')
except ZeroDivisionError:
    print('ege cannot be 0')

    
