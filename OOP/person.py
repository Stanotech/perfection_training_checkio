class Person:
    def __init__(
        self,
        first_name,
        last_name,
        birth_date,
        job,
        working_years,
        salary,
        country,
        city,
        gender="unknown",
    ):
        self.first_name = first_name 
        self.last_name = last_name
        self.birth_date = birth_date 
        self.job= job
        self.working_years = working_years
        self.salary = salary
        self.country = country
        self.city = city
        self.gender = gender

    def name (self):
        return f"{self.first_name} {self.last_name}"
    
    def age (self):
        date = self.birth_date.split(".")
        return date[2]-2018 if date[1]-1 >= 0 else date[2]-2017
    
if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing

    p1 = Person(
        "John", "Smith", "19.09.1979", "welder", 15, 3600, "Canada", "Vancouver", "male"
    )
    p2 = Person(
        "Hanna Rose", "May", "05.12.1995", "designer", 2.2, 2150, "Austria", "Vienna"
    )
    print(p1.age())
    assert p1.name() == "John Smith", "Name"
    assert p1.age() == 38, "Age"
    assert p2.work() == "Is a designer", "Job"
    assert p1.money() == "648 000", "Money"
    assert p2.home() == "Lives in Vienna, Austria", "Home"