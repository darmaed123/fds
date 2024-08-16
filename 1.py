# class Car: # шаблон или чертеж
#     "Атрибут класса"
#     # marka = 'mercedes'
#     # model = 'cls'
#     # color = 'black'
#     def __init__(self, marka, model, color): # __init__ - конструктор
#         "Атрибут объекта"
#         self.marka = marka
#         self.model = model 
#         self.color = color
#         self.bak = 10
#         self.is_start = False
        
#     def info(self):
#         print(f'Марка машины-{self.marka}, модель-{self.model}, цвет-{self.color}')
        
#     def start(self):
#         if self.bak > 0:
#             self.is_start = True
#             print(f'Марка машины-{self.marka}, модель-{self.model}, заведена')
#         else:
#             print(f'Марка машины-{self.marka}, модель-{self.model}, нет топлива') 

#     def drive(self, city):
#         if self.is_start == True:
#             print(f'Марка машины-{self.marka}, модель-{self.model}, нет топлива') 
#         else:
#             print(f'Марка машины-{self.marka}, модель-{self.model}, нет топлива') 

# toyota = Car('Toyota', 'camry', 'white')
# toyota.info()
# toyota.start()


                                    # Задание 1
class Book:
    def __init__(self, avtor, book_name, year,):
        self.avtor = avtor
        self.book_name = book_name
        self.year = year
    
    def info(self):
        print(f'Автор-{self.avtor}, Название книги-{self.book_name}, Год-{self.year}')

page = Book('Харпер Ли', 'Убить пересмешника', 1960)
page.info()



