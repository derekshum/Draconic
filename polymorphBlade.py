!alias poly tembed
<drac2>
ability_name = "their Polymorph Blade"
r = vroll("d20")
a = " "
if r.total == 1:
    a = " Tyrannosaurus"
elif r.total == 2:
    a = " Giant ape"
elif r.total == 3:
    a = "n Elephant"
elif r.total == 4:
    a = " Giant scorpion"
elif r.total == 5:
    a = " Rhinoceros"
elif r.total == 6:
    a = " Polar bear"
elif r.total == 7:
    a = " Giant toad"
elif r.total == 8:
    a = " Giant eagle"
elif r.total == 9:
    a = " Black bear"
elif r.total == 10:
	a = " Crocodile"
elif r.total == 11:
    a = " Wolf"
elif r.total == 12:
    a = " Horse"
elif r.total == 13:
    a = "n Ox"
elif r.total == 14:
    a = " Giant frog"
elif r.total == 15:
    a = " Poisonous snake"
elif r.total == 16:
    a = " Hawk"
elif r.total == 17:
    a = "n Octopus"
elif r.total == 18:
    a = " Cat"
elif r.total == 19:
    a = " Rat"
elif r.total == 20:
    a = " Rabbit"
return_string = (
    f' -title "{name} uses {ability_name}!"'
    f' -desc "When you attack a creature with this magic weapon and roll a 20 on the attack roll, the creature must make a **DC 15 Wisdom saving throw** in addition to suffering the attack\'s normal effects. On a failed save, the creature also suffers the effects of a Polymorph spell, turning into **a{a}** ({str(r)})."'
)
return_string += f' -footer "{ctx.prefix}{ctx.alias}"'
return return_string
</drac2>