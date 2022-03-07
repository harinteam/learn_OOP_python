class Player:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def getName(self):
        return self.name

    def getSpeed(self):
        return self.speed


class ArgentinaPlayer(Player):
    def setAge(self, age):
        self.age = age
        return self.age


player = Player('Kai Havertz', '90')
player2 = Player('Timo Werner', '87')
player3 = ArgentinaPlayer('Messi', '98')

print(player.getName() + " punya speed " + player.getSpeed())
print(player2.getName() + " punya speed " + player2.getSpeed())
print(player3.getName() + " umurnya " + player3.setAge('33'))
