from faker import Faker
import random

from db import Session
from models import Group, Teacher, Student, Subject, Grade

faker = Faker('uk-UA')

session = Session()

def groups_seed():
    groups = [
        Group(name="Group_1"),
        Group(name="Group_2"),
        Group(name="Group_3"),
    ]

    session.add_all(groups)
    session.commit()

def teachers_seed():
    teachers = []

    for _ in range(5):
        teacher = Teacher(name=faker.name())
        teachers.append(teacher)

    session.add_all(teachers)
    session.commit()

def subjects_seed():
    subjects_name = [
        'Химия',
        'Математика',
        'Геграфия',
        'История',
        'Литература',
        'Немецкий',
        'Биология',
        'Физика',
    ]

    teachers = session.query(Teacher).all()

    subjects = []

    for name in subjects_name:
        subjects.append(
            Subject(
                name=name, teacher_id=random.choice(teachers).id
            )
        )

    session.add_all(subjects)
    session.commit()

def students_seed():
    students = []

    groups = session.query(Group).all()

    for _ in range(50):
        students.append(
            Student(
                name=faker.name(), group_id = random.choice(groups).id
            )
        )

    session.add_all(students)
    session.commit()

def grades_seed():
    grades = []

    students = session.query(Student).all()
    subjects = session.query(Subject).all()

    for student in students:
        for _ in range(20):
            grade = Grade(
                student_id=student.id,
                subject_id=random.choice(subjects).id,
                grade=random.randint(1, 12),
                grade_date=faker.date_between(
                    start_date="-1y",
                    end_date="today"
                )
            )
            grades.append(grade)

    session.add_all(grades)
    session.commit()

def clear_database():
    session.query(Grade).delete()
    session.query(Student).delete()
    session.query(Subject).delete()
    session.query(Teacher).delete()
    session.query(Group).delete()
    session.commit()



if __name__ == '__main__':
    clear_database()

    groups_seed()
    teachers_seed()
    subjects_seed()
    students_seed()
    grades_seed()
