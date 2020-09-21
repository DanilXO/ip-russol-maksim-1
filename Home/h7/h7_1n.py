# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе
class Person:
    def __init__(self, name, surname, f_name):
        self.name = name
        self.surname = surname
        self.f_name = f_name

    def get_full_name(self):
        return "{} {} {}".format(self.name, self.surname, self.f_name)

    def full_name_format(self):
        return "{} {}. {}.".format(self.name, self.surname[0].upper(), self.f_name[0].upper())


class Student(Person):
    def __init__(self, name, surname, f_name, class_group, father, mother):
        Person.__init__(self, name, surname, f_name)
        self.class_group = class_group
        self.father = father
        self.mother = mother


class Teacher(Person):
    def __init__(self, name, surname, f_name, subjects):
        Person.__init__(self, name, surname, f_name)
        self.subjects = subjects


class Class:
    def __init__(self, num, letter, students, teacher):
        assert all((isinstance(_, Student) for _ in students)), 'что-то не так в базе учеников'
        self.students = classes
        self.letter = letter
        self.num = num

    @ property
    def class_name(self):
        return f'{self.num} {self.letter}'


class Subject:
    def __init__(self, name, student_classes, teacher):
        assert isinstance(teacher, Teacher), 'С учителем что-то не так'
        assert all(isinstance(_, Class) for _ in students)


class School:
    def __init__(self, name, classes):
        self.classes = classes
        self.teacher_dirs = {t.subjects: t for t in teachers}


teachers = [Teacher('Торсунов', 'Никон', 'Егорович', 'История'),
            Teacher('Квакина', 'Марфа', 'Семеновна', 'Русский язык'),
            Teacher('Юганцева', 'Анастасия', 'Елизаровна', 'Математика'),
            Teacher('Шатова', 'Тамара', 'Ростиславовна', 'Иностранные языки'),
            Teacher('Нырцева', 'Альбина', 'Святославовна', 'Информатика'),
            Teacher('Ярополов', 'Аскольд', 'Наумович', 'Трудовое воспитание'),
            Teacher('Борхеса', 'Юлия', 'Якововна', 'Физика'),
            Teacher('Лазарева', 'Ирина', 'Мироновна', 'Химия'),
            Teacher('Лившиц', 'Богдан', 'Феликсович', 'Биология'),
            Teacher('Сарычев', 'Эдуард', 'Прохорович', 'Физкультура'),
            Teacher('Грекова', 'Римма', 'Степановна', 'Социология'),
            Teacher('Кручинин', 'Мир', 'Святославович', 'Экономика'),
            Teacher('Пищикова', 'Арина', 'Семеновна', 'Политология'),
            Teacher('Малец', 'Авдей', 'Михаилович', 'География')]
classes = [
           School('7 A', [teachers[0], teachers[1], teachers[2], teachers[3]]),
           School('7 Б', [teachers[2], teachers[3], teachers[4], teachers[5]]),
           School('8 A', [teachers[4], teachers[5], teachers[6], teachers[7]]),
           School('8 Б', [teachers[6], teachers[7], teachers[8], teachers[9]]),
           School('9 A', [teachers[8], teachers[9], teachers[10], teachers[11]]),
           School('9 Б', [teachers[10], teachers[11], teachers[12], teachers[13]]),
           School('10 A', [teachers[12], teachers[13], teachers[0], teachers[1]]),
           School('10 Б', [teachers[0], teachers[1], teachers[2], teachers[3]]),
           School('11 A', [teachers[2], teachers[3], teachers[4], teachers[5]]),
           School('11 Б', [teachers[4], teachers[5], teachers[6], teachers[7]]),
           ]
dad = [Person('Голубов', 'Геннадий', 'Андреевич'),
       Person('Буданов', 'Степан', 'Адрианович'),
       Person('Мальчиков', 'Руслан', 'Геннадиевич'),
       Person('Попов', 'Модест', 'Прокофиевич'),
       Person('Рагозин', 'Филимон', 'Фролович'),
       Person('Шверник', 'Семен', 'Тимурович'),
       Person('Буров', 'Елисей', 'Сигизмундович'),
       Person('Дуванов', 'Денис', 'Тарасович'),
       Person('Ювелев', 'Емельян', 'Севастьянович'),
       Person('Кручинин', 'Роман', 'Архипович'),
       Person('Задорнов', 'Лавр', 'Фролович'),
       Person('Якунькин', 'Харитон', 'Аникитевич'),
       Person('Евремович', 'Артур', 'Валерьянович'),
       Person('Скоробогатов', 'Зиновий', 'Онисимович'),
       Person('Зарубин', 'Захар', 'Дмитриевич'),
       Person('Паршиков', 'Игорь', 'Федотович'),
       Person('Новосельцев', 'Фока', 'Андреевич'),
       Person('Квартин', 'Феликс', 'Эрнестович'),
       Person('Грибанов', 'Дмитрий', 'Александрович'),
       Person('Николаенко', 'Кузьма', 'Зиновиевич')]
mom = [Person('Голубова', 'Арина', 'Василиевна'),
       Person('Буданова', 'Евгения', 'Игоревна'),
       Person('Мальчикова', 'Виктория', 'Юлиевна'),
       Person('Попова', 'Пелагея', 'Афанасиевна'),
       Person('Рагозина', 'Инга', 'Захаровна'),
       Person('Шверник', 'Любава', 'Филипповна'),
       Person('Бурова', 'Василиса', 'Никитевна'),
       Person('Дуванова', 'Фаина', 'Ипполитовна'),
       Person('Ювелева', 'Рада', 'Святославовна'),
       Person('Кручинина', 'Валерия', 'Георгиевна'),
       Person('Задорнова', 'Пелагея', 'Алексеевна'),
       Person('Якунькина', 'Лариса', 'Алексеевна'),
       Person('Евремович', 'Валентина', 'Серафимовна'),
       Person('Скоробогатова', 'Кристина', 'Тимуровна'),
       Person('Зарубина', 'Нина', 'Фомевна'),
       Person('Паршикова', 'Влада', 'Елизаровна'),
       Person('Новосельцев', 'Розалия', 'Яновна'),
       Person('Квартин', 'Доминика', 'Михеевна'),
       Person('Грибанов', 'Наталья', 'Романовна'),
       Person('Николаенко', 'Анисья', 'Трофимовна')]
students = [Student('Голубова', 'Дина', 'Геннадиевна', classes[0], dad[0], mom[0]),
            Student('Буданова', 'Агафья', 'Степановна', classes[1], dad[1], mom[1]),
            Student('Мальчиков', 'Лука', 'Руслан', classes[2], dad[2], mom[2]),
            Student('Попов', 'Фома', 'Модестович', classes[3], dad[3], mom[3]),
            Student('Рагозин', 'Герман', 'Филимонович', classes[4], dad[4], mom[4]),
            Student('Шверник', 'Адам', 'Семенович', classes[5], dad[5], mom[5]),
            Student('Буров', 'Никифор', 'Елисеевич', classes[6], dad[6], mom[6]),
            Student('Дуванова', 'Инга', 'Денисовна', classes[7], dad[7], mom[7]),
            Student('Ювелев', 'Мир', 'Емельянович', classes[8], dad[8], mom[8]),
            Student('Кручинин', 'Иннокентий', 'Романович', classes[9], dad[9], mom[9]),
            Student('Задорнов', 'Моисей', 'Лаврович', classes[0], dad[10], mom[10]),
            Student('Якунькин', 'Наум', 'Харитонович', classes[1], dad[11], mom[11]),
            Student('Евремович', 'Фома', 'Артурович', classes[2], dad[12], mom[12]),
            Student('Скоробогатов', 'Петр', 'Зиновиевич', classes[3], dad[13], mom[13]),
            Student('Зарубина', 'Бронислава', 'Захарович', classes[4], dad[14], mom[14]),
            Student('Паршиков', 'Платон', 'Игорьевич', classes[5], dad[15], mom[15]),
            Student('Новосельцев', 'Пимен', 'Фокаевич', classes[6], dad[16], mom[16]),
            Student('Квартин', 'Осип', 'Феликсович', classes[7], dad[17], mom[17]),
            Student('Грибанов', 'Артемий', 'Дмитриевич', classes[8], dad[18], mom[18]),
            Student('Николаенко', 'Евдоким', 'Кузьмич', classes[9], dad[19], mom[19])]

# 1. Получить полный список всех классов школы
# print('CПИСОК ВСЕХ КЛАССОВ ШКОЛЫ: ')
# for _ in classes:
#     print(_.classes)
# 2. Получить список всех учеников в указанном классе
# for _ in classes:
#     print('УЧЕНИКИ {} КЛАССА'.format(_.classes))
#     for st in students:
#         # print(st.full_name_format())for