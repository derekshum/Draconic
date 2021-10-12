TODO for adding new types: create cc and add type to arguments for alias

!cc create "Arrows of _ Slaying" -min 0 -desc "If a creature belonging to the type, race, or group associated with an arrow of slaying takes damage from the arrow, the creature must make a DC 17 Constitution saving throw, taking an extra 6d10 piercing damage on a failed save, or half as much extra damage on a successful one.

Once an arrow of slaying deals its extra damage to a creature, it becomes a nonmagical arrow."

#TODO: 
    - add unordered input handling if implementing below
    - add vuln and resist
    - add multi-arrow functionality (loop, list, multiline display?)

!alias slay 

tembed
<drac2>
if len(&ARGS&) > 0:
    args = &ARGS&
    type = args[0].lower()
    l = len(type)
    if type == "aberrations"[0:l]:
        type = "Aberration"
    elif type == "beasts"[0:l]:
        type = "Beast"
    elif type == "celestials"[0:l]:
        type = "Celestial"
    elif type == "dragons"[0:l]:
        type = "Dragon"
    elif type == "elementals"[0:l]:
        type = "Elemental"
    elif type == "feys"[0:l]:
        type = "Fey"
    elif type == "fiends"[0:l]:
        type = "Fiend"
    elif type == "giants"[0:l]:
        type = "Giant"
    elif type == "humanoids"[0:l]:
        type = "Humanoid"
    elif type == "monstrositys"[0:l] or type == "monstrosities"[0:l] :
        type = "Monstrosity"
    elif type == "oozes"[0:l]:
        type = "Ooze"
    elif type == "plants"[0:l]:
        type = "Plant"
    elif type == "undeads"[0:l]:
        type = "Undead"
    else:
        rs = (
            f' -title "Specified type of Arrow of Slaying is not enabled!" '
            f' -desc "Correct specification or update this alias." ' 
            )
        return rs
    cc_name = "Arrows of " + type + " Slaying"
    cc_val = character().get_cc(cc_name)
    num = 1
    rs = ""
    if cc_val >= num:
        cc_use = num
        character().mod_cc(cc_name, -cc_use)
        rs += f'-title "{name} looses an Arrow of {type} Slaying!" '
        rs += f'-desc "If a creature belonging to the type, race, or group associated with an arrow of slaying takes damage from the arrow, the creature must make a **DC 17 Constitution saving throw**, taking an extra 6d10 piercing damage on a failed save, or half as much extra damage on a successful one.\n\nOnce an arrow of slaying deals its extra damage to a creature, it becomes a nonmagical arrow." '
        dmg = vroll("6d10[magical piercing]") 
        rs += f'-f "Damage (DC 17 Con, Save for Half)|{dmg} (Half: `{int(dmg.total/2)}`)" '
    else:
        cc_use = 0
        rs += (
            f'-title "{name} fails to loose an Arrow of {type} Slaying!" '
            f'-desc "No arrows remaining." '
            )
    cc_current = cc_str(cc_name)
    rs += (
        f'-f "{cc_name} (-{cc_use})|{cc_current}|inline" '
        f'-footer "{ctx.prefix}{ctx.alias} [type (required)]" '
        )
else:
    rs = (
        f'-title "Specify type of Arrow of Slaying!" '
        f'-desc "This ensures correct cc interaction." ' 
        )
return rs
</drac2>