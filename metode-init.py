class Player:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def getName(self):
        return self.name

    def getSpeed(self):
        return self.speed

    def getSkill(self):
        return 'normal'

    def setAge(self, age):
        self.age = age
        return self.age


class ArgentinaPlayer(Player):
    def setAge(self, age):
        self.age = age
        return self.age


class BrazilPlayer(Player):
    def getSkill(self):
        return 'samba'


player = Player('Kai Havertz', '90')
player2 = Player('Timo Werner', '87')
player3 = ArgentinaPlayer('Messi', '98')

print(player.getName() + " punya speed " + player.getSpeed())
print(player2.getName() + " punya speed " + player2.getSpeed())
print(player3.getName() + " umurnya " + player3.setAge('33'))

print('\n')
player4 = BrazilPlayer('Neymar', '97')
print(player4.getName() + " skillnya " + player4.getSkill() + " speednya " + player4.getSpeed() + ' umurnya ' +
      player4.setAge('29'))
