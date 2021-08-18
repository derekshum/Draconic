!alias fh tembed
<drac2>
rollText = ""
save = ""
dc = ""
shape = ""
size = ""
dispHalf = True
if len(&ARGS&) > 0:
    args = &ARGS&
    rollText = args[0]
    if len(args) > 1:
        save = args[1].lower()
        length = len(save)
        if save == "strength"[0:length]:
            save = "Strength"
        elif save == "dexterity"[0:length]:
            save = "Dexterity"
        elif save == "constitution"[0:length]:
            save = "Constitution"
        elif save == "intelligence"[0:length]:
            save = "Intelligence"
        elif save == "wisdom"[0:length]:
            save = "Wisdom"
        elif save == "charisma"[0:length]: #c will default to Consitution
            save = "Charisma"
        if len(args) > 2:
            dc = args[2]
            if len(args) > 3:
                shape = args[3]
                if len(args) > 4:
                    size = args[4]
                    if len(args) > 5: 
                        nh = args[5].lower()
                        length = len(nh)
                        if nh == "no"[0:min(length,2)]:
                            dispHalf = False
return_string = (f'-title "Make a Save!" ')
desc_string = ""
if save != "":
    save = save + " Saving Throw"
    if dc != "":
        save = "DC " + dc + " " + save
    desc_string += save + "\n"
if shape != "":
    if size != "":
        shape = size + "ft " + shape
    desc_string += shape + "\n"
dmgRoll = vroll(rollText)
desc_string += "Full Damage: " + dmgRoll + "\n"
if dispHalf:
    desc_string += "Half Damage: " + dmgRoll.total + " / 2 = " + (int)(dmgRoll.total / 2) + "\n"
else:
    desc_string += "No damage on a success!\n"
return_string += (
    f'-desc "{desc_string}" '
    f'-footer "{ctx.prefix}{ctx.alias} [roll] (Optionals: [save] [dc] [shape] [size] [no half])" '
    )
return return_string
</drac2>