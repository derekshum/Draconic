!alias fr1 tembed
<drac2>
cc_request = 1
num_die = 2
crit_text = ""
for input in &ARGS&:
   input = input.lower()
   length = len(input)
   if input == "critical"[0:length]:
       num_die = 2 * num_die
       crit_text = " (CRIT!)"
cc_name = "Fire Rune"
ability_name = "their " + cc_name
cc_value = character().get_cc(cc_name)
return_string = ""
if cc_value >= cc_request:
    cc_use = cc_request
    character().mod_cc(cc_name, -cc_use)
    roll_string = str(num_die) + "d6"
    damage = vroll(roll_string)
    return_string = (
        f' -title "{name} uses {ability_name}!" '
        f' -desc "When you hit a creature with an attack using a weapon, you can invoke the rune to summon fiery shackles: the target takes an extra {damage} fire damage, and it must succeed on a **DC {8+proficiencyBonus+constitutionMod} Strength saving throw** or be restrained for 1 minute. While restrained by the shackles, the target takes 2d6 fire damage at the start of each of its turns. The target can repeat the saving throw at the end of each of its turns, banishing the shackles on a success." '
        )
else:
    cc_use = 0
    return_string = (
        f' -title "{name} fails to use {ability_name}!" '
        f' -desc "No {cc_name} remaining." '
        )
cc_current = character().cc_str(cc_name)
return_string += (
    f' -f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    f' -footer "{ctx.prefix}{ctx.alias} [crit]" '
    )
return return_string
</drac2>