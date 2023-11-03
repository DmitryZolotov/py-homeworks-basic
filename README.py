class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = float()
        
    def __str__(self):
        grades_count = 0
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашнее задание: {self.average_rating}\n' \
              f'Курсы в процессе обучения: {courses_in_progress_string}\n' \
              f'Завершенные курсы: {finished_courses_string}'
        return res
          
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Неверное сравнение')
            return
        return self.average_rating < other.average_rating

       
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
                
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
        res = f"Имя: {self.name}\nФамилия: {self.surname}"
        return res

     
class Lecturer(Mentor):
    def __init_(self, name, surname):
        super().__init__(name, surname)
        self.average_rating = float()
        self.grades = {}

    def __str__(self):
        grades_count = 0
        for x in self.grades:
            grades_count += len(self.grades[x])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        res = f"Имя: {self.name}\nФамиля: {self.surname}\nСредняя оценка за лекции: {self.average_rating}"
        return res
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Неверное сравнение')
            return
        return self.average_rating < other.average_rating
    
    

# Студенты
student_1 = Student("Дмитрий", "Золотов")
student_1.courses_in_progress += ["Python"]
student_1.finished_courses += ["Введение в программирование"]

student_2 = Student("Анатолий", "Матвеев")
student_2.courses_in_progress += ["Git"]
student_2.finished_courses += ["Введенией в программирование"]

# Лекторы
best_lecturer_1 = Lecturer("Олег", "Булыгин")
best_lecturer_1.courses_attached += ['Python']
best_lecturer_1.courses_attached += ['Git']

best_lecturer_2 = Lecturer("Алёна", "Батитская")
best_lecturer_2.courses_attached += ['Python']
best_lecturer_2.courses_attached += ['Git']


# Проверяющие
cool_reviewer_1 = Reviewer("Елена", "Никитина")
cool_reviewer_1.courses_attached += ['Python']
cool_reviewer_1.courses_attached += ['Git']

cool_reviewer_2 = Reviewer("Евгений", "Шмаргунов")
cool_reviewer_2.courses_attached += ['Python']
cool_reviewer_2.courses_attached += ['Git']


# Оцениваю студентов
cool_reviewer_1.rate_hw(student_1, 'Python', 7)
cool_reviewer_2.rate_hw(student_1, 'Python', 10)

cool_reviewer_1.rate_hw(student_2, 'Git', 9)
cool_reviewer_2.rate_hw(student_2, 'Git', 9)

# Оцениваю лекторов
student_1.rate_hw(best_lecturer_1, 'Python', 10)
student_2.rate_hw(best_lecturer_1, 'Python', 10)

student_1.rate_hw(best_lecturer_2, 'Git', 10)
student_2.rate_hw(best_lecturer_2, 'Git', 10)


print(f'Студенты:\n{student_1}\n{student_2}')
print(f'Лекторы:\n{best_lecturer_1}\n{best_lecturer_2}')
print()

print(f'Результат сравнения студентов (по средним оценкам за ДЗ): '
      f'{student_1.name} {student_1.surname} < {student_2.name} {student_2.surname} = {student_1 > student_2}')
print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
      f'{best_lecturer_1.name} {best_lecturer_1.surname} < {best_lecturer_2.name} {best_lecturer_2.surname} = {best_lecturer_1 > best_lecturer_2}')
print()

# Списки студентов и лекторов
student_list = [student_1, student_2]
lecturer_list = [best_lecturer_1, best_lecturer_2]

# Средняя оценка за домашние задания
def student_rating(student_list, course_name):
    sum_all = 0
    count_all = 0
    for studentik in student_list:
        if studentik.courses_in_progress == [course_name]:
            sum_all += studentik.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all

# Средняя оценка за лекции
def lecturer_rating(student_list, course_name):
    sum_all = 0
    count_all = 0
    for ganibal_lecturer in lecturer_list:
        if ganibal_lecturer.courses_attached == [course_name]:
            sum_all += ganibal_lecturer.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all




print(f"Средняя оценка за домашние задания по курсу {'Python'}: {student_rating(student_list, 'Python')}")
print(f"Средняя оценка за домашние задания по курсу {'Git'}: {student_rating(student_list, 'Git')}")
print()
print(f"Средняя оценка лекторам по курсу {'Python'}: {lecturer_rating(lecturer_list, 'Python')}")
print(f"Средняя оценка лекторам по курсу {'Git'}: {lecturer_rating(lecturer_list, 'Git')}")