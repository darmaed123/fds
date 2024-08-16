class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    def __make_computations(self):
        addition = self.__cpu + self.__memory
        subtraction = self.__cpu - self.__memory
        multiplication = self.__cpu * self.__memory
        if self.__memory != 0:
            division = self.__cpu / self.__memory
        else:
            division = 'undefined (division by zero)'

        return (
            f"Addition: {self.__cpu} + {self.__memory} = {addition}\n"
            f"Subtraction: {self.__cpu} - {self.__memory} = {subtraction}\n"
            f"Multiplication: {self.__cpu} * {self.__memory} = {multiplication}\n"
            f"Division: {self.__cpu} / {self.__memory} = {division}\n")

    def get_cpu(self):
        return self.__cpu

    def get_memory(self):
        return self.__memory

    def info(self):
        computations = self.__make_computations()
        return (
            f"Computer Info:\n"
            f"CPU: {self.__cpu}\n"
            f"Memory: {self.__memory}\n"
            f"{computations}")

class Laptop(Computer):
    def __init__(self, cpu, memory, memory_card):
        super().__init__(cpu, memory)
        self.__memory_card = memory_card

    def get_memory_card(self):
        return self.__memory_card

    def info(self):
        base_info = super().info()
        return (
            f"{base_info}"
            f"Memory Card: {self.__memory_card}\n")

comp = Computer(cpu=4, memory=8)
laptop = Laptop(cpu=6, memory=16, memory_card=32)

print(comp.info())
print(laptop.info())

print(f"Computer CPU: {comp.get_cpu()}")
print(f"Computer Memory: {comp.get_memory()}")
print(f"Laptop CPU: {laptop.get_cpu()}")
print(f"Laptop Memory: {laptop.get_memory()}")
print(f"Laptop Memory Card: {laptop.get_memory_card()}")