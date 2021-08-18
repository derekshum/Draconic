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
                damage = args[3]
                length = len(damage)
                if damage.lower() == "bludgeoning"[0:length]:
                    damage = "Bludgeoning"
                elif damage.lower() == "piercing"[0:length]:
                    damage = "Piercing"
                elif damage.lower() == "slashing"[0:length]:
                    damage = "Slashing"
                elif damage.lower() == "acid"[0:length]:
                    damage = "Acid"   
                elif damage.lower() == "cold"[0:length]:
                    damage = "Cold"
                elif damage.lower() == "fire"[0:length]:
                    damage = "Fire"
                elif damage.lower() == "force"[0:length]:   #f is fire
                    damage = "Force"
                elif damage.lower() == "lightning"[0:length]:
                    damage = "Lightning"
                elif damage.lower() == "necrotic"[0:length]:
                    damage = "Necrotic"
                elif damage.lower() == "poison"[0:length]:
                    damage = "Poison"
                elif damage.lower() == "psychic"[0:length]:
                    damage = "Psychic"
                elif damage.lower() == "radiant"[0:length]:
                    damage = "Radiant"
                elif damage.lower() == "thunder"[0:length]:
                    damage = "Thunder"                
                if len(args) > 4: 
                    nh = args[4].lower()
                    length = len(nh)
                    if nh == "no"[0:length]:
                        dispHalf = False
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
desc_string += "Full Damage: " + dmgRoll + "[" + damage + "]\n"
if dispHalf:
    desc_string += "Half Damage: " + dmgRoll.total + " / 2 = " + (int)(dmgRoll.total / 2) + "\n"
else:
    desc_string += "No damage on a success!\n"
return_string += (
    f'-desc "{desc_string}" '
    f'-footer "{ctx.prefix}{ctx.alias} [roll] (Optionals: [save] [dc] [dmg type] [half] [shape] [size])" '
    )
return return_string
</drac2>