import random
#Pokemon: Rhydon
#Type: Rock
#Attack: Stomp

level = 100
power = 65
attack = 414
#Ninetales Sp.Def level 100
defense = 339

target = 1
weather = 1
badge = 1
crit = 1
rndm = round(random.uniform(0.85,1.0),2)
stab = 1.5
type = 0.5
burn = 1
modifier = target*weather*badge*crit*rndm*stab*type*burn*1

damage = ((2*level)/5)+2
damage = (damage*power)*(attack/defense)
damage = ((damage/50)+2)*modifier

print ("Rhydon lvl 100: Stomp"+ "\n" +"S.p Attack:" + str(attack))
print("Damage on Alakazam: " + str( round(damage)))