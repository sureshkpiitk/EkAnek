import random
import string


class Student(object):
    def __init__(self, name: str, age: int, marks: int, roll_number: str):
        self.name = name
        self.age = age
        self.marks = marks
        self.roll_number = roll_number

    def __repr__(self):
        return f"{self.name}-{self.age}-{self.marks}-{self.roll_number}"


def custom_filter_tuple(student, filters):
    return tuple(getattr(student, key) for key in filters)


def sort(student_objs, filters):

    return sorted(student_objs, key=lambda student: custom_filter_tuple(student, filters))


if __name__ == '__main__':
    letters = string.ascii_lowercase
    student_list = []
    for i in range(100):
        s = Student(name=''.join(random.choice(letters) for _ in range(8)), age=random.randrange(10, 100),
                    marks=random.randrange(0, 600),
                    roll_number=''.join(random.choice(letters) for j in range(4)))
        student_list.append(s)
    print(sort(student_list, ('name', 'age')))
