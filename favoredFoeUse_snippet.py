!snippet foe1 tembed
<drac2>
num = 1
cc_name = "Favored Foe"
cc_value = character().get_cc(cc_name)
if cc_value >= num:
    cc_use = num
    character().mod_cc(cc_name, -cc_use)
    die = 4+2*int((RangerLevel+2)/8)
    return_string = f' -d{num} 1d{die} -f "{cc_name}|When you hit a creature with an attack roll, you can call on your mystical bond with nature to mark the target as your favored enemy for 1 minute or until you lose your concentration (as if you were concentrating on a spell).\n\nThe first time on each of your turns that you hit the favored enemy and deal damage to it, including when you mark it, you can increase that damage by 1d4." '
else:
    cc_use = 0
    return_string = f' -f "No remaining {cc_name} uses|Damage was not added." '
cc_current = cc_str(cc_name)
return_string += f' -f "{cc_name} (-{cc_use})| {cc_current}|inline" '
return return_string
</drac2>

#!snippet fo -d1 1d{4+2*((RangerLevel+2)/8)}
#!cc create "Favored Foe" -min 0 -max {proficiencyBonus} -type bubble -reset long -disc "When you hit a creature with an attack roll, you can call on your mystical bond with nature to mark the target as your favored enemy for 1 minute or until you lose your concentration (as if you were concentrating on a spell).

The first time on each of your turns that you hit the favored enemy and deal damage to it, including when you mark it, you can increase that damage by 1d4.

You can use this feature to mark a favored enemy a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest.

This feature's extra damage increases when you reach certain levels in this class: to 1d6 at 6th level and to 1d8 at 14th level."
