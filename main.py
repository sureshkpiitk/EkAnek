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
    # Time O(n*log(n))
    # Space O(n)
    return sorted(student_objs, key=lambda student: custom_filter_tuple(student, filters))


def flight_fair(delhi_to_mumbai, mumbai_to_delhi, k):
    # Space O(k*k)
    # Time O(n*log(n)) + O(k*K)

    s_delhi_to_mumbai, s_mumbai_to_delhi = sorted(delhi_to_mumbai), sorted(mumbai_to_delhi)
    mix_sort = [(i, j, i+j) for i in s_delhi_to_mumbai[:k] for j in s_mumbai_to_delhi[:k]]
    sorted_fair_list = sorted(mix_sort, key=lambda x: (x[2], x[0], x[1]))
    return [(item[0], item[1]) for item in sorted_fair_list[:k]]


if __name__ == '__main__':
    letters = string.ascii_lowercase
    student_list = []
    for i in range(100):
        s = Student(name=''.join(random.choice(letters) for _ in range(8)), age=random.randrange(10, 100),
                    marks=random.randrange(0, 600),
                    roll_number=''.join(random.choice(letters) for j in range(4)))
        student_list.append(s)
    print(sort(student_list, ('name', 'age')))

    delhi_to_mumbai = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
    mumbai_to_delhi = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]

    print(flight_fair(delhi_to_mumbai, mumbai_to_delhi, 10))
