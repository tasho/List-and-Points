from pprint import pprint
from student import Student

actions = ['new', 'add', 'all', 'close', 'check']

if __name__ == "__main__":  # for windows
    students = []
    while True:
        try:
            action = input()  # read action
            action = str(action)
            if not action in actions:
                print('[ERROR] incorrect action')

            if action == 'close':  # close program
                break

            if action == 'all':  # print all students
                if not len(students):
                    print('list is empty.')
                    continue

                students.sort()
                for student in students:
                    print(student)

            if action == 'check': #cheking existance of student

                name = str(input())

                if not len(students):
                    print('No matches.')
                    continue

                check = 0
                for s in students:
                    if s.name == name:
                        check = 1

                if check:
                    print('Yep')
                else:
                    print('No')

            if action == 'new':  # adding new student
                name = input()
                name = str(name)
                points = 0

                check = 0
                for s in students:
                    if s.name == name:
                        check = 1

                if not check:
                    students.append(Student(name=name, points=points))
                    print('Student', name, 'added.')
                else:
                    print('Student', name, 'is already exists.')

            if action == 'add':  # adding new student
                name, points = input().split(' ')
                name = str(name)
                points = float(points)

                check = 0
                for s in students:
                    if s.name == name:
                        s.points += points
                        check = 1

                if check:
                    print('Points for student', name, 'added.')
                else:
                    print('Student', name, 'does not exists.')
        except (Exception, e):
            print('[ERROR]', e)
            print('HELP:')
            print('    stdin must be <action> <name student> <points>')
            print('    <action> one if', actions)
            print('    <name student> must be string without separate')
            print('    <points> must be float or int number')
