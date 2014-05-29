from pprint import pprint
from student import Student

actions = ['add', 'all', 'close']

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

            if action == 'add':  # adding new student
                name, points = input().split(' ')
                name = str(name)
                points = float(points)
                students.append(Student(name=name, points=points))
                print('Points for student ', name, ' added.')
        except (Exception, e):
            print('[ERROR]', e)
            print('HELP:')
            print('    stdin must be <action> <name student> <points>')
            print('    <action> one if', actions)
            print('    <name student> must be string without separate')
            print('    <points> must be float or int number')
