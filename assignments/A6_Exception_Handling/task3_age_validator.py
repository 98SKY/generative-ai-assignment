# task3_age_validator.py

def check_age(age):
    if age < 1 or age > 120:
        raise ValueError("Age must be between 1 and 120")
    return True


try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
    print("Age is valid.")

except ValueError as e:
    print("Error:", e)
