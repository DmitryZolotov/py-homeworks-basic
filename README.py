  
# Класс студент  
class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = float()

# Задание 2       
    def rate_hw(self, course, grade, lecturer):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attsched and course in self.courses_in_progress:
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
        
# Задание 3            
    def __str__(self):
        grades_count = 0
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_course_string = ', '.join(self.finished_courses)
        for x in self.grades:
            grades_count +=len(self.grades[x])
        self.average_rating = sum(sum, self.grades.values()) / grades_count
        res = f"Имя: {self.name}\n" \
              f"Фамилия: {self.surname}\n" \
              f"Средняя оценка за домашние задания: {self.average_rating}\n" \
              f"Курсы в процессе изучений: {self.courses_in_progress}\n" \
              f"Завершённые курсы: {self.finished_courses}"
        return res
        


# Класс ментор         
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
 
 
# Задание 1: Класс проверяющий (от родительского ментор)         
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super.__init__(name, surname)

# Задание 2        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.course_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

# Задание 3    
    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}"
        return res
    


# Задание 1: Класс лектор (от родительского ментор)      
class Lecturer(Mentor):
    def __init_(self, name, surname):
        super.__init__(name, surname)
        self.average_rating = float()
        self.grades = {}
    
# Задание 3
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
    
    
# Задание 4: Создаю 2 объекта каждого класса: студенты, лекторы, проверяющие
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

best_lecturer_2 = Lecturer("Алёна", "Батитская")
best_lecturer_2.courses_attached += ['Git']

# Проверяющие
cool_reviewer_1 = Reviewer("Елена", "Никитина")
cool_reviewer_1.courses_attached += ['Python']
cool_reviewer_1.courses_attached += ['Git']

cool_reviewer_2 = Reviewer("Евгений", "Шмаргунов")
cool_reviewer_2.courses_attached += ['Python']
cool_reviewer_2.courses_attached += ['Git']