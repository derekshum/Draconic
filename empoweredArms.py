!alias emp tembed
<drac2>
ability_name = "Empowered Arms"
crit = False
if len(&ARGS&) > 0:
    args = &ARGS&
    input = args[0].lower()
    if input == "c" or input == "crit" or input == "critical":
        crit = True    
if MonkLevel >= 11:
    die = int(4 + int((MonkLevel + 1) / 6) * 2)
    die_num = 1
    crit_text = ""
    if crit:
        crit_text = " (CRIT!)"
        die_num = 2
    damage = vroll(str(die_num) + "d" + str(die))
    return_string = (
        f' -title "{name} uses {ability_name}!"'
        f' -desc "Once on each of your turns when you hit a target with the Arms of the Astral Self, you can deal extra damage to the target equal to your Martial Arts die."'
        f' -f "Damage{crit_text}|{str(damage)}|inline"'
        )
else:
    return_string = (
        f' -title "{name} fails to use {ability_name}!"'
        f' -desc "Not enough levels in Monk." '
        )
return_string += f' -footer "{ctx.prefix}{ctx.alias}"'
return return_string
</drac2>