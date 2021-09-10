!alias rad tembed
<drac2>
ability_name = "Radiant Weapon"
bonus = 0
if len(&ARGS&) > 0:
    args = &ARGS&
    bonus = int(args[0]) #bonus
cc_name = ability_name
cc_value = character().get_cc(cc_name)
return_string = ""
if cc_value >= 1:
    cc_use = 1
    character().mod_cc(cc_name, -cc_use)
    return_string = (
        f'-title "{name} uses their {ability_name}!" '
        f'-desc "As a reaction immediately after being hit by an attack, the wielder can expend 1 charge and cause the attacker to be blinded until the end of the attacker\'s next turn, unless the attacker succeeds on a **DC {int(get_raw().spellbook.dc) + bonus}** Constitution saving throw." '
        )
else:
    cc_use = 0
    return_string = (
        f' -title "{name} fails to use their {ability_name}!" '
        f' -desc "It will recharge (a bit) at dawn." '
        )
cc_current = cc_str(cc_name)
return_string += (
    f'-f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    f'-footer "{ctx.prefix}{ctx.alias}"'
    )
return return_string
</drac2>