class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if 0 <= grade <= 10:
                if course in lecturer.student_rate_lecture:
                    lecturer.student_rate_lecture[course] += [grade]
                else:
                    lecturer.student_rate_lecture[course] = [grade]
        else:
            return 'Ошибка'

    def _average_rat(self, grade):
        average_rat = []
        courses = []
        for key, value in self.grades.items():
            average_rat += value
            if key not in courses:
                courses.append(key)
            else:
                courses += key
        average = round((sum(average_rat) / len(average_rat)), 1)
        if grade == 'grade':
            return average
        elif grade == 'list courses':
            return courses

    def __str__(self):
        grade = 'grade'
        list_courses_with_grade = 'list courses'
        res = (f'\nИмя: {self.name}'
               f'\nФамилия: {self.surname}'
               f'\nСредняя оценка за домашние задания: {self._average_rat(grade)}'
               f'\nКурсы в процессе изучения: {", ".join(self._average_rat(list_courses_with_grade))}'
               f'\nЗавершенные курсы: {", ".join(self.finished_courses)}')
        return res

    def __lt__(self, other):
        grade = 'grade'
        if not isinstance(other, Lecturer):
            print('Данный Лектор не найден')
            return
        return self._average_rat(grade) < other.average_rate_lecture()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.student_rate_lecture = {}

    def average_rate_lecture(self):
        average_rate_lecture = []
        for key, value in self.student_rate_lecture.items():
            average_rate_lecture += value
        average = round((sum(average_rate_lecture) / len(average_rate_lecture)), 1)
        return average

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rate_lecture()}'
        return res


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if 0 <= grade <= 10:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


# Функция по подсчету средней оценки всех студентов
def _average_rat_students(course, *students):
    list_rat = []
    for student in students:
        if student.grades.get(course):
            list_rat.extend(student.grades[course])
    return round(sum(list_rat) / len(list_rat), 1)


# Функция по подсчету средней оценки всех лекторов
def _average_rat_lecturers(course, *lecturers):
    list_rat = []
    for lecturer in lecturers:
        if lecturer.student_rate_lecture.get(course):
            list_rat.extend(lecturer.student_rate_lecture[course])
    return round(sum(list_rat) / len(list_rat), 1)


if __name__ == '__main__':
    # зачисляем студентов на курсы
    student_1 = Student('Bran', 'Stark', 'your_gender')
    student_1.courses_in_progress += ['Стрельба из лука']
    student_1.courses_in_progress += ['Фехтование']
    student_1.courses_in_progress += ['Религия']
    student_1.finished_courses += ['Великие дома']
    student_2 = Student('Arya', 'Stark', 'your_gender')
    student_2.courses_in_progress += ['Стрельба из лука']
    student_2.courses_in_progress += ['Фехтование']
    student_2.courses_in_progress += ['Религия']
    student_2.finished_courses += ['Великие дома']
    student_3 = Student('John', 'Snow', 'your_gender')
    student_3.courses_in_progress += ['Стрельба из лука']
    student_3.courses_in_progress += ['Фехтование']
    student_3.courses_in_progress += ['Религия']
    student_3.finished_courses += ['Великие дома']
    # Определяем Лекторов и Экспертов по курсам
    lecturer_1 = Lecturer('Tyrion', 'Lannister')
    lecturer_1.courses_attached += ['Стрельба из лука']
    lecturer_1.courses_attached += ['Фехтование']
    lecturer_1.courses_attached += ['Религия']
    lecturer_2 = Lecturer('Ned', 'Stark')
    lecturer_2.courses_attached += ['Стрельба из лука']
    lecturer_2.courses_attached += ['Фехтование']
    lecturer_2.courses_attached += ['Религия']
    reviewer_1 = Reviewer('Jeor', 'Mormont')
    reviewer_1.courses_attached += ['Стрельба из лука']
    reviewer_1.courses_attached += ['Фехтование']
    reviewer_1.courses_attached += ['Религия']
    reviewer_2 = Reviewer('Petyr', 'Baelish')
    reviewer_2.courses_attached += ['Стрельба из лука']
    reviewer_2.courses_attached += ['Фехтование']
    reviewer_2.courses_attached += ['Религия']
    # эксперты оценивают работы студентов
    reviewer_1.rate_hw(student_1, 'Стрельба из лука', 5)
    reviewer_1.rate_hw(student_1, 'Стрельба из лука', 6)
    reviewer_2.rate_hw(student_1, 'Стрельба из лука', 4)
    reviewer_2.rate_hw(student_1, 'Стрельба из лука', 5)
    reviewer_1.rate_hw(student_1, 'Фехтование', 6)
    reviewer_1.rate_hw(student_1, 'Фехтование', 7)
    reviewer_2.rate_hw(student_1, 'Фехтование', 5)
    reviewer_2.rate_hw(student_1, 'Фехтование', 6)
    reviewer_1.rate_hw(student_1, 'Религия', 9)
    reviewer_1.rate_hw(student_1, 'Религия', 10)
    reviewer_2.rate_hw(student_1, 'Религия', 10)
    reviewer_2.rate_hw(student_1, 'Религия', 9)
    reviewer_1.rate_hw(student_2, 'Стрельба из лука', 10)
    reviewer_1.rate_hw(student_2, 'Стрельба из лука', 9)
    reviewer_2.rate_hw(student_2, 'Стрельба из лука', 8)
    reviewer_2.rate_hw(student_2, 'Стрельба из лука', 10)
    reviewer_1.rate_hw(student_2, 'Фехтование', 8)
    reviewer_1.rate_hw(student_2, 'Фехтование', 7)
    reviewer_2.rate_hw(student_2, 'Фехтование', 9)
    reviewer_2.rate_hw(student_2, 'Фехтование', 10)
    reviewer_1.rate_hw(student_2, 'Религия', 5)
    reviewer_1.rate_hw(student_2, 'Религия', 5)
    reviewer_2.rate_hw(student_2, 'Религия', 6)
    reviewer_2.rate_hw(student_2, 'Религия', 6)
    reviewer_1.rate_hw(student_3, 'Стрельба из лука', 9)
    reviewer_1.rate_hw(student_3, 'Стрельба из лука', 10)
    reviewer_2.rate_hw(student_3, 'Стрельба из лука', 8)
    reviewer_2.rate_hw(student_3, 'Стрельба из лука', 9)
    reviewer_1.rate_hw(student_3, 'Фехтование', 10)
    reviewer_1.rate_hw(student_3, 'Фехтование', 10)
    reviewer_2.rate_hw(student_3, 'Фехтование', 9)
    reviewer_2.rate_hw(student_3, 'Фехтование', 10)
    reviewer_1.rate_hw(student_3, 'Религия', 7)
    reviewer_1.rate_hw(student_3, 'Религия', 6)
    reviewer_2.rate_hw(student_3, 'Религия', 8)
    reviewer_2.rate_hw(student_3, 'Религия', 7)
    # студенты оценивают лекции
    student_1.rate_lecturer(lecturer_1, 'Стрельба из лука', 7)
    student_1.rate_lecturer(lecturer_1, 'Стрельба из лука', 6)
    student_1.rate_lecturer(lecturer_1, 'Фехтование', 7)
    student_1.rate_lecturer(lecturer_1, 'Фехтование', 8)
    student_1.rate_lecturer(lecturer_1, 'Религия', 8)
    student_1.rate_lecturer(lecturer_1, 'Религия', 8)
    student_1.rate_lecturer(lecturer_2, 'Стрельба из лука', 9)
    student_1.rate_lecturer(lecturer_2, 'Стрельба из лука', 9)
    student_1.rate_lecturer(lecturer_2, 'Фехтование', 9)
    student_1.rate_lecturer(lecturer_2, 'Фехтование', 8)
    student_1.rate_lecturer(lecturer_2, 'Религия', 7)
    student_1.rate_lecturer(lecturer_2, 'Религия', 8)
    student_2.rate_lecturer(lecturer_1, 'Стрельба из лука', 7)
    student_2.rate_lecturer(lecturer_1, 'Стрельба из лука', 7)
    student_2.rate_lecturer(lecturer_1, 'Фехтование', 6)
    student_2.rate_lecturer(lecturer_1, 'Фехтование', 7)
    student_2.rate_lecturer(lecturer_1, 'Религия', 7)
    student_2.rate_lecturer(lecturer_1, 'Религия', 9)
    student_2.rate_lecturer(lecturer_2, 'Стрельба из лука', 10)
    student_2.rate_lecturer(lecturer_2, 'Стрельба из лука', 9)
    student_2.rate_lecturer(lecturer_2, 'Фехтование', 10)
    student_2.rate_lecturer(lecturer_2, 'Фехтование', 9)
    student_2.rate_lecturer(lecturer_2, 'Религия', 9)
    student_2.rate_lecturer(lecturer_2, 'Религия', 0)
    student_3.rate_lecturer(lecturer_1, 'Стрельба из лука', 6)
    student_3.rate_lecturer(lecturer_1, 'Стрельба из лука', 7)
    student_3.rate_lecturer(lecturer_1, 'Фехтование', 9)
    student_3.rate_lecturer(lecturer_1, 'Фехтование', 8)
    student_3.rate_lecturer(lecturer_1, 'Религия', 7)
    student_3.rate_lecturer(lecturer_1, 'Религия', 9)
    student_3.rate_lecturer(lecturer_2, 'Стрельба из лука', 10)
    student_3.rate_lecturer(lecturer_2, 'Стрельба из лука', 9)
    student_3.rate_lecturer(lecturer_2, 'Фехтование', 10)
    student_3.rate_lecturer(lecturer_2, 'Фехтование', 9)
    student_3.rate_lecturer(lecturer_2, 'Религия', 9)
    student_3.rate_lecturer(lecturer_2, 'Религия', 8)
    # задание 2, пример вывода оценок
    print(f'{"*" * 25} задание 2 {"*" * 25}')
    print(f'\n{student_1.grades}')
    print(f'\n{lecturer_1.student_rate_lecture}')
    # задание 3, пример магического вывода (__str__)
    print(f'{"*" * 25} задание 3 {"*" * 25}')
    print(f'{student_1}')
    print(f'{lecturer_1}')
    print(f'{reviewer_1}')
    # задание 4.
    print(f'{"*" * 25} задание 4 {"*" * 25}')
    print(student_1 < lecturer_2)
    course = 'Фехтование'
    print(_average_rat_students(course, student_1, student_2, student_3))
    print(_average_rat_lecturers(course, lecturer_1, lecturer_2))
