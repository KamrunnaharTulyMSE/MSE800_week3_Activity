# main.py
# OOP Inheritance Project - University People

class Person:
    def __init__(self, person_id, name):
        self.id = person_id
        self.name = name

    def display_details(self):
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")


class Staff(Person):
    def __init__(self, person_id, name, staff_id, tax_num):
        super().__init__(person_id, name)
        self.staff_id = staff_id
        self.tax_num = tax_num


class General(Staff):
    def __init__(self, person_id, name, staff_id, tax_num, rate_of_pay):
        super().__init__(person_id, name, staff_id, tax_num)
        self.rate_of_pay = rate_of_pay

    def calculate_pay_rate(self):
        return self.rate_of_pay

    def display_pay_rate(self):
        print(f"General Staff: {self.name}")
        print(f"Pay Rate: ${self.calculate_pay_rate():.2f} per hour")


class Academic(Staff):
    def __init__(self, person_id, name, staff_id, tax_num, publications):
        super().__init__(person_id, name, staff_id, tax_num)
        self.publications = publications

    def calculate_publications(self):
        return self.publications


class Lecturer(Academic):
    def display_publications(self):
        print(f"Lecturer: {self.name}")
        print(f"Number of Publications: {self.calculate_publications()}")


# Create objects
lecturer = Lecturer(101, "Dr. Sarah Lee", 501, "TX12345", 12)
general_staff = General(102, "John Smith", 502, "TX67890", 28.50)

# Display results
print("=== University Staff Information ===")
lecturer.display_publications()
print()
general_staff.display_pay_rate()
