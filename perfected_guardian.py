!cc create "Perfected Guardian" -min 0 -max proficiencyBonus -type bubble -reset long -desc "When a Huge or smaller creature you can see ends its turn within 30 feet of you, you can use your reaction to magically force the creature to make a Strength saving throw against your spell save DC, pulling the creature up to 30 feet toward you to an unoccupied space. If you pull the target to a space within 5 feet of you, you can make a melee weapon attack against it as part of this reaction."

!alias pg tembed
<drac2>
ability_name = "Perfected Guardian Armor"
bonus = 0
if len(&ARGS&) > 0:
    args = &ARGS&
    bonus = int(args[0]) #bonus
cc_name = "Perfected Guardian"
cc_value = character().get_cc(cc_name)
return_string = ""
if cc_value >= 1:
    cc_use = 1
    character().mod_cc(cc_name, -cc_use)
    return_string = (
        f'-title "{name} uses their {ability_name}!" '
        f'-desc "When a Huge or smaller creature you can see ends its turn within 30 feet of you, you can use your reaction to magically force the creature to make a **DC {int(get_raw().spellbook.dc) + bonus}** Strength saving throw, pulling the creature up to 30 feet toward you to an unoccupied space. If you pull the target to a space within 5 feet of you, you can make a melee weapon attack against it as part of this reaction. " '
        )
else:
    cc_use = 0
    return_string = (
        f' -title "{name} fails to use their {ability_name}!" '
        f' -desc "Take a long rest." '
        )
cc_current = cc_str(cc_name)
return_string += (
    f'-f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    f'-footer "{ctx.prefix}{ctx.alias} [DC bonus]"'
    )
return return_string
</drac2>