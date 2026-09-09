from argparse import ArgumentParser
from datetime import date
from db import Session
from models import Teacher, Group, Student, Subject, Grade


session = Session()

parser = ArgumentParser()

parser.add_argument(
    "--action",
    choices=["create", "list", "update", "remove"],
    required=True
)

parser.add_argument(
    "--model",
    choices=["Teacher", "Group", "Student", "Subject", "Grade"],
    required=True
)

parser.add_argument("--id", type=int)
parser.add_argument("--name", type=str)
parser.add_argument("--group_id", type=int)
parser.add_argument("--teacher_id", type=int)
parser.add_argument("--grade_date", type=date.fromisoformat)

args = parser.parse_args()


if args.model == "Teacher":

    if args.action == "create":
        if not args.name:
            print("Потрібно вказати --name")
        else:
            teacher = Teacher(name=args.name)
            session.add(teacher)
            session.commit()

            print(f"Викладача {teacher.name} створено")

    elif args.action == "list":
        teachers = session.query(Teacher).all()

        for teacher in teachers:
            print(f"id={teacher.id}, name={teacher.name}")

    elif args.action == "update":
        if not args.id or not args.name:
            print("Потрібно вказати --id та --name")
        else:
            teacher = session.query(Teacher).filter(
                Teacher.id == args.id
            ).first()

            if teacher is None:
                print("Викладача не знайдено")
            else:
                teacher.name = args.name
                session.commit()

                print("Викладача оновлено")

    elif args.action == "remove":
        if not args.id:
            print("Потрібно вказати --id")
        else:
            teacher = session.query(Teacher).filter(
                Teacher.id == args.id
            ).first()

            if teacher is None:
                print("Викладача не знайдено")
            else:
                session.delete(teacher)
                session.commit()

                print("Викладача видалено")


elif args.model == "Group":

    if args.action == "create":
        if not args.name:
            print("Потрібно вказати --name")
        else:
            group = Group(name=args.name)
            session.add(group)
            session.commit()

            print(f"Групу {group.name} створено")

    elif args.action == "list":
        groups = session.query(Group).all()

        for group in groups:
            print(f"id={group.id}, name={group.name}")

    elif args.action == "update":
        if not args.id or not args.name:
            print("Потрібно вказати --id та --name")
        else:
            group = session.query(Group).filter(
                Group.id == args.id
            ).first()

            if group is None:
                print("Групу не знайдено")
            else:
                group.name = args.name
                session.commit()

                print("Групу оновлено")

    elif args.action == "remove":
        if not args.id:
            print("Потрібно вказати --id")
        else:
            group = session.query(Group).filter(
                Group.id == args.id
            ).first()

            if group is None:
                print("Групу не знайдено")
            else:
                session.delete(group)
                session.commit()

                print("Групу видалено")

elif args.model == "Student":

    if args.action == "create":
        if not args.name or not args.group_id:
                print("Потрібно вказати --name та --group_id")
        else:
            student = Student(
                name=args.name,
                group_id=args.group_id
            )

            session.add(student)
            session.commit()

            print(f"Студента {student.name} створено")

    elif args.action == "list":
        students = session.query(Student).all()

        for student in students:
            print(
                f"id={student.id}, "
                f"name={student.name}, "
                f"group_id={student.group_id}"
            )

    elif args.action == "update":
        if not args.id:
            print("Потрібно вказати --id")
        else:
            student = session.query(Student).filter(
                Student.id == args.id
            ).first()

            if student is None:
                print("Студента не знайдено")
            else:
                if args.name:
                    student.name = args.name

                if args.group_id:
                    student.group_id = args.group_id

                session.commit()

                print("Студента оновлено")

    elif args.action == "remove":
        if not args.id:
            print("Потрібно вказати --id")
        else:
            student = session.query(Student).filter(
                Student.id == args.id
            ).first()

            if student is None:
                print("Студента не знайдено")
            else:
                session.delete(student)
                session.commit()

                print("Студента видалено")

elif args.model == "Subject":

    if args.action == "create":
        if not args.name or not args.teacher_id:
            print("Потрібно вказати --name та --teacher_id")
        else:
            subject = Subject(
                name=args.name,
                teacher_id=args.teacher_id
            )

            session.add(subject)
            session.commit()

            print(f"Предмет {subject.name} створено")

    elif args.action == "list":
        subjects = session.query(Subject).all()

        for subject in subjects:
            print(
                f"id={subject.id}, "
                f"name={subject.name}, "
                f"teacher_id={subject.teacher_id}"
            )

    elif args.action == "update":
        if not args.id:
            print("Потрібно вказати --id")
        else:
            subject = session.query(Subject).filter(
                Subject.id == args.id
            ).first()

            if subject is None:
                print("Предмет не знайдено")
            else:
                if args.name:
                    subject.name = args.name

                if args.teacher_id:
                    subject.teacher_id = args.teacher_id

                session.commit()

                print("Предмет оновлено")

    elif args.action == "remove":
        if not args.id:
            print("Потрібно вказати --id")
        else:
            subject = session.query(Subject).filter(
                Subject.id == args.id
            ).first()

            if subject is None:
                print("Предмет не знайдено")
            else:
                session.delete(subject)
                session.commit()

                print("Предмет видалено")
if args.model == "Grade":

    if args.action == "create":
        if (
            not args.student_id
            or not args.subject_id
            or args.grade is None
            or not args.grade_date
        ):
            print(
                "Потрібно вказати --student_id, --subject_id, "
                "--grade та --grade_date"
            )
        else:
            grade = Grade(
                student_id=args.student_id,
                subject_id=args.subject_id,
                grade=args.grade,
                grade_date=args.grade_date
            )

            session.add(grade)
            session.commit()

            print("Оцінку створено")

    elif args.action == "list":
        grades = session.query(Grade).all()

        for grade in grades:
            print(
                f"id={grade.id}, "
                f"student_id={grade.student_id}, "
                f"subject_id={grade.subject_id}, "
                f"grade={grade.grade}, "
                f"date={grade.grade_date}"
            )

    elif args.action == "update":
        if not args.id:
            print("Потрібно вказати --id")
        else:
            grade = session.query(Grade).filter(
                Grade.id == args.id
            ).first()

            if grade is None:
                print("Оцінку не знайдено")
            else:
                if args.student_id:
                    grade.student_id = args.student_id

                if args.subject_id:
                    grade.subject_id = args.subject_id

                if args.grade is not None:
                    grade.grade = args.grade

                if args.grade_date:
                    grade.grade_date = args.grade_date

                session.commit()

                print("Оцінку оновлено")

    elif args.action == "remove":
        if not args.id:
            print("Потрібно вказати --id")
        else:
            grade = session.query(Grade).filter(
                Grade.id == args.id
            ).first()

            if grade is None:
                print("Оцінку не знайдено")
            else:
                session.delete(grade)
                session.commit()

                print("Оцінку видалено")

session.close()

