  
# Класс студент  
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

# Задание 2       
    def lecturer_grades(self, course, grade, lecturer):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attsched and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
# Задание 3            
    def __str__(self):
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за домашние задания: {? ? ? ? ? ? ?}\n"
            f"Курсы в процессе изучений: {self.courses_in_progress}\n"
            f"Завершённые курсы: {self.finished_courses}"
            )
        


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
        return f"Имя: {self.name}\nФамилия: {self.surname}"
        


# Задание 1: Класс лектор (от родительского ментор)      
class Lecturer(Mentor):
    def __init_(self, name, surname):
        super.__init__(name, surname)
    grades = {}
    
# Задание 3
    def __str__(self):  
        return f"Имя: {self.name}\nФамиля: {self.surname}\nСредняя оценка за лекции: {? ? ? ? ? ? ?}"
    
    
# Задание 4: Создаю 2 объекта каждого класса: студенты, лекторы, проверяющие
student_1 = Student("Дмитрий", "Золотов", "М")
student_1.grades = {}
student_1.courses_in_progress = ["Python", "Git"]
student_1.finished_courses = ["Введение в программирование"]

student_2 = Student("Анатолий", "Матвеев", "М")
student_2.grades = {}
student_2.courses_in_progress = ["Python", "Git"]
student_2.finished_courses = ["Введенией в программирование"]

lecturer_1 = Lecturer("Олег", "Булыгин")
lecturer_1.grades = {}

lecturer_2 = Lecturer("Евгений", "Шмаргунов")
lecturer_2.grades = {}

reviewer_1 = Reviewer("Елена", "Никитина")