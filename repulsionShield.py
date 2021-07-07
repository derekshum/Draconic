!alias rep tembed
<drac2>
ability_name = "Repulsion Shield"
cc_name = ability_name
cc_value = character().get_cc(cc_name)
return_string = ""
if cc_value >= 1:
    cc_use = 1
    character().mod_cc(cc_name, -cc_use)
    return_string = (
        f'-title "{name} uses their {ability_name}!" '
        f'-desc "While holding it, the wielder can use a reaction immediately after being hit by a melee attack to expend 1 of the shield\'s charges and push the attacker up to 15 feet away." '
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