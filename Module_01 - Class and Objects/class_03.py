class Customer:
    def __init__(self,name,type):
        self.name = name
        self.type = type

c1 = Customer('Messi','BFC')
c2 = Customer('Neymar','PSG')
c3 = Customer('Ronaldo','REAL')

players = [c1,c2,c3]

for player in players:
    print("Team Player Name : {}".format(player.name))

print("".center(50,"="))

for team in players:
    print("Team Type Name : {}".format(team.type))

print("".center(50,"="))

print("Player Name : ",c1.name)
print("Player Name : ",c2.name)
print("Player Name : ",c3.name)

