from abc import ABC, abstractmethod

class Appliance(ABC):
    def turn_on(self):
        pass

    def turn_off(self):
        pass

    
    def use(self):
        pass

    
    def repair(self):
        pass

class WashingMachine(Appliance):
    def use(self):
        print("Стиральная машина начала стирку")

    def repair(self):
        print("Ремонт стиральной машины")

class Microwave(Appliance):
    def use(self):
        print("Микроволновая печь разогревает еду")

    def repair(self):
        print("Ремонт микроволновой печи")

class Refrigerator(Appliance):
    def use(self):
        print("Холодильник охлаждает продукты")

    def repair(self):
        print("Ремонт холодильника")


washing_machine = WashingMachine()
microwave = Microwave()
refrigerator = Refrigerator()

washing_machine.turn_on()
washing_machine.use()
washing_machine.turn_off()
washing_machine.repair()

microwave.turn_on()
microwave.use()
microwave.turn_off()
microwave.repair()
refrigerator.turn_on()
refrigerator.use()
refrigerator.turn_off()
refrigerator.repair()

