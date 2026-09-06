from functools import wraps


# Decorator to check if the employee is logged in
def login_required(function):
    @wraps(function)
    def wrapper(logged_in, *args, **kwargs):
        if logged_in:
            return function(logged_in, *args, **kwargs)
        else:
            print("Access Denied: Please log in first.")

    return wrapper


@login_required
def view_salary(logged_in):
    print("Employee salary: $55,000")


@login_required
def view_personal_details(logged_in):
    print("Employee Name: John")
    print("Employee ID: E101")


@login_required
def download_report(logged_in):
    print("Employee report downloaded successfully.")


# Testing the functions

print("---- Logged in employee ----")
view_salary(True)
view_personal_details(True)
download_report(True)

print("\n---- Employee not logged in ----")
view_salary(False)
view_personal_details(False)
download_report(False)