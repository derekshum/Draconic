#!alias fh 
tembed
<drac2>
rollText = ""
save = ""
dc = ""
damage = ""
shape = ""
size = ""
dispHalf = True
if len(&ARGS&) > 0:
    args = &ARGS&
    rollText = args[0]
    if len(args) > 1:
        save = args[1]
        length = len(save)
        if save.lower() == "strength"[0:length]:
            save = "Strength"
        elif save.lower() == "dexterity"[0:length]:
            save = "Dexterity"
        elif save.lower() == "constitution"[0:length]:
            save = "Constitution"
        elif save.lower() == "intelligence"[0:length]:
            save = "Intelligence"
        elif save.lower() == "wisdom"[0:length]:
            save = "Wisdom"
        elif save.lower() == "charisma"[0:length]: #c will default to Consitution
            save = "Charisma"
        if len(args) > 2:
            dc = args[2]
            if len(args) > 3: 
                nh = args[3].lower()
                length = len(nh)
                if nh == "no"[0:length]:
                    dispHalf = False
                if len(args) > 4:
                    damage = args[4]
                    length = len(damage)
                    if damage.lower() == "bludgeoning"[0:length]:
                        damage = "bludgeoning"
                    elif damage.lower() == "piercing"[0:length]:
                        damage = "piercing"
                    elif damage.lower() == "slashing"[0:length]:
                        damage = "slashing"
                    elif damage.lower() == "acid"[0:length]:
                        damage = "acid"   
                    elif damage.lower() == "cold"[0:length]:
                        damage = "cold"
                    elif damage.lower() == "fire"[0:length]:
                        damage = "fire"
                    elif damage.lower() == "force"[0:length]:   #f is fire
                        damage = "force"
                    elif damage.lower() == "lightning"[0:length]:
                        damage = "lightning"
                    elif damage.lower() == "necrotic"[0:length]:
                        damage = "necrotic"
                    elif damage.lower() == "poison"[0:length]:
                        damage = "poison"
                    elif damage.lower() == "psychic"[0:length]:
                        damage = "psychic"
                    elif damage.lower() == "radiant"[0:length]:
                        damage = "radiant"
                    elif damage.lower() == "thunder"[0:length]:
                        damage = "thunder"   
                    damage = "[" + damage + "]"
                    if len(args) > 5:
                        shape = args[5]
                        if len(args) > 6:
                            size = args[6]
if save != "":
    save += " "
    if dc != "":
        save = "DC " + dc + " " + save
save += "Saving Throw"
return_string = (f'-title "Make a {save}!" ')
desc_string = ""
if shape != "":
    if size != "":
        shape = size + "ft " + shape
    desc_string += shape + "\n"
dmgRoll = vroll(rollText)
desc_string += "Full Damage: " + dmgRoll + damage + "\n"
if dispHalf:
    desc_string += "Half Damage: " + dmgRoll.total + " / 2 = " + (int)(dmgRoll.total / 2) + damage + "\n"
else:
    desc_string += "No damage on a success!\n"
return_string += (
    f'-desc "{desc_string}" '
    f'-footer "{ctx.prefix}{ctx.alias} [roll] (Optionals: [save] [dc] [half(y)] [dmg type] [shape] [size])" '
    )
return return_string
</drac2>