from sqlalchemy import func, desc, String, cast
from db import Session
from models import Student, Grade, Group, Subject, Teacher


def select_1():
    session = Session()

    result = (
        session.query(
            Student.name,
            func.round(
                func.avg(Grade.grade), 2
            ).label('avg_grade')
        )
        .select_from(Grade)
        .join(Student)
        .group_by(Student.id, Student.name)
        .order_by(desc('avg_grade'))
        .limit(5)
        .all()
    )

    session.close()
    return result

def select_2(subject_id):
    session = Session()

    result = (
        session.query(
            Student.name,
            func.round(func.avg(Grade.grade), 2)
            .label('avg_grade')
        )
        .select_from(Grade)
        .join(Student)
        .filter(Grade.subject_id == subject_id)
        .group_by(Student.id, Student.name)
        .order_by(desc('avg_grade'))
        .first()
    )

    session.close()
    return result

def select_3(subject_id):
    session = Session()

    result = (
        session.query(
            Group.name,
            Subject.name,
            func.round(func.avg(Grade.grade),2)
            .label('avg_grades')
        )
        .select_from(Grade)
        .join(Student)
        .join(Group)
        .join(Subject)
        .filter(Grade.subject_id == subject_id)
        .group_by(Group.id, Group.name, Subject.id, Subject.name)
        .all()
    )

    session.close()
    return result

def select_4():
    session = Session()

    result = (
        session.query(
            func.round(func.avg(Grade.grade), 2)
            .label('avg_grade')
        )
        .select_from(Grade)
        .one()
    )

    session.close()
    return result

def select_5(teacher_id):
    session = Session()

    result = (
        session.query(
            Teacher.name,
            func.string_agg(Subject.name, ','))
        .select_from(Subject)
        .join(Teacher)
        .filter(Subject.teacher_id == teacher_id)
        .group_by(Teacher.id, Teacher.name)
        .all()
    )

    session.close()
    return result

def select_6(group_id):
    session = Session()

    result = (
        session.query(
            Group.name,
            func.string_agg(Student.name, '; ')
        )
        .select_from(Student)
        .join(Group)
        .filter(Student.group_id == group_id)
        .group_by(Group.id, Group.name)
        .first()
    )

    session.close()
    return result

def select_7(group_id, subject_id):
    session = Session()

    result = (
        session.query(
            Student.name,
            Group.name,
            Subject.name,
            func.string_agg(cast(Grade.grade, String), ',')
        )
        .select_from(Grade)
        .join(Student)
        .join(Group)
        .join(Subject)
        .filter(Student.group_id == group_id)
        .filter(Grade.subject_id == subject_id)
        .group_by(
            Student.id,
            Student.name,
            Group.id,
            Group.name,
            Subject.id,
            Subject.name)
        .all()
    )

    session.close()
    return result

def select_8(teacher_id):
    session = Session()

    result = (
        session.query(
            Teacher.name,
            func.string_agg(func.distinct(Subject.name), ',')
            .label('subject'),
            func.round(func.avg(Grade.grade), 2)
            .label('avg_grade')
        )
        .select_from(Grade)
        .join(Subject)
        .join(Teacher)
        .filter(Subject.teacher_id == teacher_id)
        .group_by(Teacher.id, Teacher.name)
        .all()
    )


    session.close()
    return result

def select_9(student_id):
    session = Session()

    result = (
        session.query(
            Student.name,
            func.string_agg(func.distinct(Subject.name), ',')
            .label('subject')
        )
        .select_from(Grade)
        .join(Student)
        .join(Subject)
        .filter(Grade.student_id == student_id)
        .group_by(Student.id, Student.name)
        .first()
    )

    session.close()
    return result

def select_10(student_id, teacher_id):
    session = Session()

    result = (
        session.query(
            Student.name,
            Teacher.name,
            func.string_agg(func.distinct(Subject.name), ',')
            .label('subject')
        )
        .select_from(Grade)
        .join(Student)
        .join(Subject)
        .join(Teacher)
        .filter(Grade.student_id == student_id)
        .filter(Subject.teacher_id == teacher_id)
        .group_by(Student.id, Student.name, Teacher.id, Teacher.name)
        .all()
    )

    session.close()
    return result

def select_11(student_id, teacher_id):
    session = Session()

    result = (
        session.query(
            Student.name,
            Teacher.name,
            func.round(func.avg(Grade.grade), 2)
            .label('avg_grade')
        )
        .select_from(Grade)
        .join(Student)
        .join(Subject)
        .join(Teacher)
        .filter(Grade.student_id == student_id)
        .filter(Subject.teacher_id == teacher_id)
        .group_by(Student.id, Student.name, Teacher.id, Teacher.name)
        .first()
    )

    session.close()
    return result

def select_12(group_id, subject_id):
    session = Session()

    last_date = (
        session.query(
            func.max(Grade.grade_date)
        )
        .select_from(Grade)
        .join(Student)
        .filter(Student.group_id == group_id)
        .filter(Grade.subject_id == subject_id)
        .scalar_subquery()
    )

    result = (
        session.query(
            Group.name,
            Subject.name,
            Student.name,
            Grade.grade,
            Grade.grade_date
        )
        .select_from(Grade)
        .join(Student)
        .join(Group)
        .join(Subject)
        .filter(Group.id == group_id)
        .filter(Subject.id == subject_id)
        .filter(Grade.grade_date == last_date)
        .all()
    )

    session.close()
    return result


if __name__ == '__main__':
    print(select_12(3, 5))

    #print(select_2(1))
    #print(select_3(2))
   # print(select_4())
   # print(select_5(3))
   # print(select_6(3))
   # print(select_7(3, 5))
   # print(select_8(3))
   # print(select_9(4))
   # print(select_10(4, 5))
   # print(select_11(4, 5))
   # print(select_12(3, 5))

