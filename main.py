import logging


logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)

formatter = logging.Formatter("%(asctime)s:%(name)s:%(message)s")
file_handler = logging.FileHandler("employee.app")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)



class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info(f"{self.email}")

    @property
    def email(self):
        return f"{self.first}.{self.last}@gmail.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"


emp = Employee("saran", "subramani")
emp_1 = Employee("subramani", "saran")
print(emp_1.email)


