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

    def name (self, first_name, last_name):
        return first_name + last_name
    
    def age (self, birth_date):
        