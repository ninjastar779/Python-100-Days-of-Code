class job:
    name = None
    salary = None
    hoursWorked = None

    def __init__(self, name: str, salary: int | float, hoursWorked: int | float):
        self.name = name
        self.salary = salary
        self.hoursWorked = hoursWorked


class doctor(job):
    experience = None
    specialty = None

    def __init__(
        self, name: str, salary: int | float, hoursWorked: int | float, experience: int, specialty: str
    ):
        super().__init__(name, salary, hoursWorked)
        self.experience = experience
        self.specialty = specialty


class teacher(job):
    subject = None
    position = None

    def __init__(self, name: str, salary: int | float, hoursWorked: int | float, position: str, subject: str) -> None:
        """
        Initializes a teacher object with the given name, salary, hours worked, position, and subject.
        """
        super().__init__(name, salary, hoursWorked)
        self.position = position
        self.subject = subject


lawyer = job("Neel", 50000, 40)

jamesDoctor = doctor("James", 50000, 40, 7, "Pediatric Consultant")

janeTeacher = teacher("Jane", 50000, 40, "Teacher", "Computer Science")
