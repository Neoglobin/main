class Player:
    name = "Alex"
    health = 100
    stamina = 100
    mana = 100
    fire_resist = 15

class Immolate_Improved:
    def degrade(self):
        pass
class Fire_Ball(Immolate_Improved):
        def degrade(self):
            Player.fire_resist = (Player.fire_resist * 0.05)
            Player.health = Player.health - 20
            print("health: " + str(citizen.health))
            print("fire_resist: " + str(citizen.fire_resist))
class Snow_Ball(Immolate_Improved):
    def degrade(self):
        Player.fire_resist = (Player.fire_resist * -0.2)
        Player.health = Player.health - 40
        print("health: " + str(citizen.health))
        print("fire_resist: " + str(round(citizen.fire_resist, 2)))

citizen = Player

print(f"Cast! to {citizen.name}" + "\n")
Fire_Ball.degrade(citizen)
print("Another cast!" + "\n")
Snow_Ball.degrade(citizen)

