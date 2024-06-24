from abc import abstractmethod


class Person:
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob

    @abstractmethod
    def describe(self):
        pass


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.grade = grade

    def describe(self):
        print(f">> Student - Name: {self.name} - YoB: {self.yob} - Grade: {self.grade}")


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        print(f">> Teacher - Name: {self.name} - YoB: {self.yob} - Subject: {self.subject}")


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        print(f">> Doctor - Name: {self.name} - YoB: {self.yob} - Specialist: {self.specialist}")


student1 = Student(name="studentA", yob=2010, grade="7")
student1.describe()
teacher1 = Teacher(name="teacherA", yob=1969, subject="Math ")
teacher1.describe()
doctor1 = Doctor(name="doctorA ", yob=1945, specialist="Endocrinologists ")
doctor1.describe()

print()
teacher2 = Teacher(name="teacherB ", yob=1995, subject="History ")
doctor2 = Doctor(name="doctorB ", yob=1975, specialist="Cardiologists ")


class Ward:
    def __init__(self, name):
        self.name = name
        self.list_people = list()

    def add_person(self, person: Person):
        self.list_people.append(person)

    def describe(self):
        print(f">> Ward Name: {self.name}")
        for person in self.list_people:
            person.describe()

    def count_doctor(self):
        count = 0
        for person in self.list_people:
            if isinstance(person, Doctor):
                count += 1
        return count

    def sort_age(self):
        self.list_people.sort(key=lambda x: x.yob, reverse=True)

    def compute_average(self):
        sum_age = 0
        count = 0
        for person in self.list_people:
            if isinstance(person, Teacher):
                sum_age += person.yob
                count +=1
        return sum_age / count if count > 0 else 0


ward1 = Ward(name=" Ward1 ")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
ward1.describe()

print(f"\n>> Number of doctors: {ward1.count_doctor()}\n")
print(">> After sorting Age of Ward1 people")
ward1.sort_age()
ward1.describe()

print(f"\nAverage year of birth (teachers): {ward1.compute_average()}")
