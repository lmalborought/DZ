class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lr(self, lecturer, course, grade):
        if not isinstance(lecturer,
                          Lecturer) or course not in lecturer.courses_attached or course not in self.courses_in_progress:
            return 'Ошибка'
        else:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]

    def av_grade(self):
        sum_of_grade = 0
        len_of_grade = 0
        for grades in self.grades.values():
            sum_of_grade += sum(grades)
            len_of_grade += len(grades)
        average_rating = round(sum_of_grade / len_of_grade, 2)
        return average_rating

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:{self.av_grade()}\nКурсы в ' \
               f'процессе изучения:{",".join(self.courses_in_progress)}\nЗавершенные ' \
               f'курсы: {",".join(self.finished_courses)} '

    def __lt__(self, other):
        if not isinstance(other, Student):
            return "Преподователей и студентов между собой сравнивать нельзя!"
        return self.av_grade() < other.av_grade()

    def av_course_grade(self, course):
        sum_of_grade = 0
        len_of_grade = 0
        for subj in self.grades.keys():
            if subj == course:
                sum_of_grade += sum(self.grades[course])
                len_of_grade += len(self.grades[course])
            average_rating = round(sum_of_grade / len_of_grade, 2)
            return average_rating


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


class Lecturer(Mentor):
    def av_grade(self):
        sum_of_grade = 0
        len_of_grade = 0
        for grades in self.grades.values():
            sum_of_grade += sum(grades)
            len_of_grade += len(grades)
        average_rating = round(sum_of_grade / len_of_grade, 2)
        return average_rating

    def __str__(self):
        return f'Имя:{self.name}\nФамилия:{self.surname}\nСредняя оценка за лекции:{self.av_grade()}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return "Преподователей и студентов между собой сравнивать нельзя!"
        return self.av_grade() < other.av_grade()

    def av_course_grade(self, course):
        sum_of_grade = 0
        len_of_grade = 0
        for subj in self.grades.keys():
            if subj == course:
                sum_of_grade += sum(self.grades[course])
                len_of_grade += len(self.grades[course])
            average_rating = round(sum_of_grade / len_of_grade, 2)
            return average_rating


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


# Students
student_1 = Student('Абобка', 'Бобкин', 'м')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['git']

student_2 = Student('Сан', 'Саныч', 'м')
student_2.courses_in_progress += ['Python']
student_2.finished_courses += ['git']

# Lecturer
lecturer_1 = Lecturer('Денис', 'Папич')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Андрей', 'Петров')
lecturer_2.courses_attached += ['Python']

# Reviewer
reviewer_1 = Reviewer('Синдзи', 'Икари')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Геннадий', 'Горин')
reviewer_2.courses_attached += ['Python']

# Students grades
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)

reviewer_2.rate_hw(student_2, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Python', 7)
reviewer_2.rate_hw(student_2, 'Python', 9)

# Lecturer grades
student_1.rate_lr(lecturer_1, 'Python', 10)
student_1.rate_lr(lecturer_1, 'Python', 7)
student_1.rate_lr(lecturer_1, 'Python', 10)

student_2.rate_lr(lecturer_2, 'Python', 10)
student_2.rate_lr(lecturer_2, 'Python', 5)
student_2.rate_lr(lecturer_2, 'Python', 7)

student_list = [student_1, student_2]
lecturer_list = [lecturer_1, lecturer_2]


def average_course_rating(course, student_list):
    sum_rating = 0
    quantity_rating = 0
    for i in student_list:
        for course in i.grades:
            stud_sum_rating = i.av_course_grade(course)
            sum_rating += stud_sum_rating
            quantity_rating += 1
    average_rating = round(sum_rating / quantity_rating, 2)
    return average_rating


print(average_course_rating('Python', student_list))
print(average_course_rating('Python', lecturer_list))
print(student_1)
print(student_2)
print(lecturer_1)
print(lecturer_2)
