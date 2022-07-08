!alias ll tembed
<drac2>
ability_name = "Lightning Launcher"
ds = "d6"
crit_text = ""
if len(&ARGS&) > 0:
    args = &ARGS&
    input = args[0].lower()
    if input == "critical hit"[0:len(input)]:
        ds = "2d6"
        crit_text = " (CRIT!)"
damage = vroll(ds)
return_string = (
    f' -title "{name} uses their {ability_name}!"'
    f' -desc "Once on each of your turns when you hit a creature with your {ability_name}, you can deal an extra 1d6 lightning damage to that target."'
    f' -f "Damage{crit_text}|{str(damage)}|inline"'
    )
return_string += f' -footer "{ctx.prefix}{ctx.alias}"'
return return_string
</drac2>