
import datetime

class Car:
    def __init__(self,mark,model,year,mileage):
        self.mark=mark
        self.model=model
        self._year=year
        self.__mileage=mileage
    def display_info(self):
        print(self.mark,self.model)
    def _calculate_age(self):
        current=datetime.datetime.now().year
        return current - self._year
    
    def  _update_mileage(self):
        return self.__mileage

    def set_mileage(self):
        return self._update_mileage()
    
car = Car('Mazda', 'Demio', 2008, 142000)

print(car.mark)
print(car.model)
print(car._year)
print(car._update_mileage())
print(car._calculate_age())