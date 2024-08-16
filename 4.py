'Полиморфизм'

class Cat:
    def __init__(self, name, preferences):
        self.name = name
        self.prefences = preferences

    def info(self):
        print(f'Я кот. Меня зовут  {self.name}. Мне {self.prefences}  Года')
    def make_sound(self):
        print('Мяу')


class Dog:
    def __init__(self, name, preferences):
        self.name = name
        self.prefences = preferences

    def info(self, color):
        print(f'Я собака. Меня зовут  {self.name}. Мне {self.prefences}  Года, цвета {color}')
    def make_sound(self):
        print('Гав')

cat = Cat('Васька', 2)
dog = Dog('Мухтар', 3)


for animal in (cat, dog):
    animal.make_sound()
    animal.info()
    animal.make_sound()


    class PaymentMethod:
        def pay(self, amount):
            pass

    class Creditcard(PaymentMethod):
        def pay(self, amount):
            return f'Сумма {amount}, оплачиватся по кредтной карте'
    
    class PayPal(PaymentMethod):
        def pay(self, amount):
            return f'Сумма {amount}, оплачивается по PayPal'
        
    class BankTransfer(PaymentMethod):
        def pay(self, amount):
            return f'Сумма {amount}, оплачивается по банковскому переводу'
        
        payments = [Creditcard(), PayPal(), BankTransfer()]
        for payments in payments:
            print(payments.pay(100))
        