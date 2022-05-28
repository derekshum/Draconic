!alias foua tembed 
<drac2>
ability_name = "Fist of Unborken Air"
cc_name = "Ki Points"
ki_usage = 2
if len(&ARGS&) > 0:
    args = &ARGS&
    ki_usage = int(args[0])
    if ki_usage < 2:
        return_string = (
            f' -title "{name} fails to use {ability_name}!" '
            f' -desc "{cc_name} usage must be 2 or more." '
            )
        return return_string
cc_value = character().get_cc(cc_name)
return_string = ""
if cc_value >= ki_usage:
    cc_use = ki_usage
    character().mod_cc(cc_name, -cc_use)
    damage = vroll(int(cc_use + 1) + "d10")
    return_string = (
        f'-title "{name} uses {ability_name}!" '
        f'-desc "You can create a blast of compressed air that strikes like a mighty fist. As an action, you can spend 2 ki points and choose a creature within 30 feet of you. That creature must make a Strength saving throw. On a failed save, the creature takes 3d10 bludgeoning damage, plus an extra 1d10 bludgeoning damage for each additional ki point you spend, and you can push the creature up to 20 feet away from you and knock it prone. On a successful save, the creature takes half as much damage, and you don\'t push it or knock it prone." '
        f'-f "Damage|{str(damage)}|inline" '
        f'-f "Str Save|DC {int(8 + wisdomMod + proficiencyBonus)}|inline" '
        )
else:
    cc_use = 0
    return_string = (
        f' -title "{name} fails to use {ability_name}!" '
        f' -desc "Less than {ki_usage} {cc_name} remaining, take a rest." '
        )
cc_current = character().cc_str(cc_name)
return_string += (
    f'-f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    f'-footer "{ctx.prefix}{ctx.alias} [total # of ki]" '
    )
return return_string
</drac2>