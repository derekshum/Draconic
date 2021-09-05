TODO for adding new types: create cc and add type to arguments for alias

!cc create "Arrows of _ Slaying" -min 0 -desc "If a creature belonging to the type, race, or group associated with an arrow of slaying takes damage from the arrow, the creature must make a DC 17 Constitution saving throw, taking an extra 6d10 piercing damage on a failed save, or half as much extra damage on a successful one.

Once an arrow of slaying deals its extra damage to a creature, it becomes a nonmagical arrow."

!alias slay 

tembed
<drac2>
if len(&ARGS&) > 0:
    args = &ARGS&
    type = args[0].lower()
    l = len(type)
    if type == "aberrations"[0:l]:
        type = "Aberration"
    elif type == "dragons"[0:l]:
        type = "Dragon"
    else:
        rs = (
            f' -title "Specified type of Arrow of Slaying is not enabled!" '
            f' -desc "Correct specification or update this alias." ' 
            )
        return rs
    num = 1
    if len(&ARGS&) > 1:
        num = int(args[1])
    cc_name = "Arrows of " + type + " Slaying"
    cc_val = character().get_cc(cc_name)
    
    if cc_val >= num:
        cc_use = num
        character().mod_cc(cc_name, -cc_use)
        rs = f'-desc "If a creature belonging to the type, race, or group associated with an arrow of slaying takes damage from the arrow, the creature must make a **DC 17 Constitution saving throw**, taking an extra 6d10 piercing damage on a failed save, or half as much extra damage on a successful one.\n\nOnce an arrow of slaying deals its extra damage to a creature, it becomes a nonmagical arrow." '
        if num == 1:
            rs += f'-title "{name} looses an Arrow of {type} Slaying!" '
            dmg = vroll("6d10[magical piercing]") 
            rs += f'-f "Damage (DC 17 Con, Save for Half)|{dmg} (Half: `{int(dmg.total/2)}`)" '
        else:
            rs += f'-title "{name} looses {num} Arrows of {type} Slaying!" '
            for i in range(num):
                dmg = vroll("6d10[magical piercing]")
                rs += f'-f "Damage {(i + 1)} (DC 17 Con, Save for Half)|{dmg} (Half: `{int(dmg.total/2)}`)" '
    else:
        cc_use = 0
        rs = (
            f'-title "{name} fails to loose any Arrows of {type} Slaying!" '
            f'-desc "Insufficient arrows remaining." '
            )
    cc_current = cc_str(cc_name)
    rs += (
        f'-f "{cc_name} (-{cc_use})| {cc_current}" '
        f'-footer "{ctx.prefix}{ctx.alias} [type(required)] [num]" '
        )
else:
    rs = (
        f'-title "Specify type of Arrow of Slaying!" '
        f'-desc "This ensures correct cc interaction." ' 
        )
return rs
</drac2>