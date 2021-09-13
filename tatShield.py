!alias tatShield tembed
<drac2>
other_AC_bonus = 0
other_AC_bonus_set = False
if len(&ARGS&) > 0:
    args = &ARGS&
    input = args[0].lower()
    other_AC_bonus = int(input)
    other_AC_bonus_set = True
ability_name = "their Shield Spellwrought Tattoo"
cc_name = "Shield Spellwrought Tattoo"
cc_value = character().get_cc(cc_name)
return_string = ""
if cc_value > 0:
    cc_use = 1
    character().mod_cc(cc_name, -cc_use)
    return_string = f' -title "{name} invokes {ability_name}!"'
    if other_AC_bonus_set: 
        return_string += f' -f "New AC|{armor + other_AC_bonus} + 5 = {armor + other_AC_bonus + 5}|inline"'
    else:
        return_string += f' -f "AC Bonus|+5|inline"'  
else:
    cc_use = 0
    return_string = (
        f' -title "{name} fails to use {ability_name}!"'
        f' -desc "No tattoo available."'
        )
cc_current = cc_str(cc_name)
return_string += f' -f "{cc_name} (-{cc_use})| {cc_current}|inline"'
return_string += f' -footer "{ctx.prefix}{ctx.alias} [other AC bonus (optional)]"'     
return return_string
</drac2>