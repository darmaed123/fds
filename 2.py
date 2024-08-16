# class Game:
#     def init(self, game_name, game_release, company):
#         self.game_name = game_name
#         self.game_release = game_release
#         self.company = company
        
#     def info(self):
#         print(f'Игра - Название - {self.game_name}, Дата релиза - {self.game_release}, Компания - {self.company}')

# game = Game('Minecraft', 2009, 'Mojang')
# game.info()

# class Roblox(Game):
#     def init(self, game_name, game_release, company):
#         # super().init(game_name, game_release, company) # можно использовать super(), это предпочтительный метод
#         Game.init(self, game_name, game_release, company) # тоже верный способ, но менее предпочтительный
        
#         self.name = "Player"
#         self.gender = "man"
#         self.skin = "Naruto"
#         self.hp = 100
        
#     def info_player(self):
#         # Исправлено название метода и отступы
#         print(f"Игрок - {self.name}, Гендер - {self.gender}, Скин вашего бомжа - {self.skin}, Начальное здоровье вашего персонажа - {self.hp}")

#     def edit_player(self):
#         # Исправлено название метода и отступы
#         self.name = input("Введите своё имя: ")
#         self.gender = input("Введите свой пол: ")
#         self.skin = input("Введите свой скин: ")

# roblox = Roblox('Roblox', 2006, 'Roblox')
# roblox.info()
# roblox.info_player()
# roblox.edit_player()
# roblox.info_player()


# class BloxFruit(Roblox):
#     def init(self, name, gender, skin, hp):
#         self.name = name
#         self.gender = gender
#         self.skin = skin
#         self.hp = hp

#     def info_player(self):
#         print(f"Игрок - {self.name}, Гендер - {self.gender}, Скин вашего бомжа - {self.skin}, Начальное здоровье вашего персонажа - {self.hp}")

# blox = BloxFruit('', '', '', '')
                                        
