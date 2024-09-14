class character:
    name:str = None
    health:int = None
    magicPoints:int = None

    def __init__(self, name:str, health:int, magicPoints:int):
        self.name = name
        self.health = health
        self.magicPoints = magicPoints

    def print(self):
        print(f"{self.name} has {self.health} health and {self.magicPoints} magic points")
    
    def setStats(self, health:int, magicPoints:int):
        self.health = health
        self.magicPoints = magicPoints

class player(character):
    nickname:str = None
    lives:int = None

    def __init__(self, name:str, health:int, magicPoints:int, nickname:str, lives:int):
        super().__init__(name, health, magicPoints)
        self.nickname = nickname
        self.lives = lives

    def isAlive(self):
        if self.lives > 0:
            return True
        else:
            return False
        
class enemy(character):
    type:str = None
    strength:int = None

    def __init__(self, name:str, health:int, magicPoints:int, type:str, strength:int):
        super().__init__(name, health, magicPoints)
        self.type = type
        self.strength = strength

class orc(enemy):
    speed:int = None

    def __init__(self, name:str, health:int, magicPoints:int, type:str, strength:int, speed:int):
        super().__init__(name, health, magicPoints, type, strength)
        self.speed = speed

class vampire(enemy):
    day:bool = None

    def __init__(self, name:str, health:int, magicPoints:int, type:str, strength:int, day:bool):
        super().__init__(name, health, magicPoints, type, strength)
        self.day = day


myChar = player("Neel", 100, 50, "Neel", 3)

myChar.print()

myChar.setStats(200, 100)

myChar.print()

myVampire = vampire("Vampire", 100, 50, "Vampire", 10, True)

myVampire.print()