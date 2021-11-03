!alias piercer tembed
<drac2>
old_roll = 1
if len(&ARGS&) > 0:
    args = &ARGS&
    old_roll = int(args[0])
ability_name = "Piercer"
damage = vroll("1d12-" + old_roll)
return_string = (
    f' -title "{name} uses {ability_name}!"'
    f' -desc "{name}\'s  deadly accuracy inflicts an additional {str(damage)} piercing damage. Once per turn, when they hit a creature with an attack that deals piercing damage, they can reroll one of the attack’s damage dice, and must use the new roll."'
    f' -footer "{ctx.prefix}{ctx.alias} [original roll (1)]"'
    )
return return_string
</drac2>