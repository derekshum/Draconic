!alias deft tembed
<drac2>
crit = False
if len(&ARGS&) > 0:
    args = &ARGS&
    input = args[0].lower()
    if input == "c" or input == "crit" or input == "critical":
        crit = True    
ability_name = "Deft Strike"
cc_name = "Ki Points"
cc_value = character().get_cc(cc_name)
return_string = ""
if cc_value >= 1:
    cc_use = 1
    character().mod_cc(cc_name, -cc_use)
    crit_text = ""
    die = int(4 + int((MonkLevel + 1) / 6) * 2)
    die_num = 1
    if crit:
        crit_text = " (CRIT!)"
        die_num = 2
    damage = vroll(str(die_num) + "d" + str(die))
    return_string = (
        f'-title "{name} uses {ability_name}!" '
        f'-desc "When you hit a target with a kensei weapon, you can spend 1 ki point to cause the weapon to deal extra damage to the target equal to your Martial Arts die. You can use this feature only once on each of your turns." '
        f' -f "Damage{crit_text}|{str(damage)}|inline" '
        )
else:
    cc_use = 0
    return_string = (
        f' -title "{name} fails to use {ability_name}!" '
        f' -desc "Not enough Ki." '
        )
cc_current = cc_str(cc_name)
return_string += (
    f'-f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    f'-footer "{ctx.prefix}{ctx.alias} [crit (optional)]"'
    )
return return_string
</drac2>