!alias breath tembed
<drac2>
ability_name = "Drake's Breath"
cc_name = "Drake's Breath"
cc_value = character().get_cc(cc_name)
return_string = ""
if cc_value >= 1:
    cc_use = 1
    character().mod_cc(cc_name, -cc_use)
    if RangerLevel < 15:        
        d = vroll("6d6")
    else:
        d = vroll("8d6")
    return_string = (
        f'-title "{name} uses {ability_name}!" '
        f'-desc "As an action, you can exhale a 30-foot cone of damaging breath or cause your drake to exhale it. Choose acid, cold, fire, lightning, or poison damage. Each creature in the cone must make a **DC {str(character().spellbook.dc)}** Dexterity saving throw, taking {str(d)} damage on a failed save, or half as much (`{str(int(d.total/2))}`) damage on a successful one." '
        )
else:
    cc_use = 0
    return_string = (
        f' -title "{name} fails to use {ability_name}!" '
        f' -desc "Take a long rest or expend a spell slot of 3rd level or higher to use it again." '
        )
cc_current = character().cc_str(cc_name)
return_string += (
    f'-f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    f'-footer "{ctx.prefix}{ctx.alias}"'
    )
return return_string
</drac2>