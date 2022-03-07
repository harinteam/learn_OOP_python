"""
Class and object
"""


class Player:
    name = ''

    def getName(self, name2):
        self.name = name2
        return self.name


# outside class
pemain = Player()
pemain2 = Player()
print(pemain.getName('Jorginho'))
print(pemain2.getName('Mason Mount'))