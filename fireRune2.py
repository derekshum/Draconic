!alias fr2 tembed
<drac2>
cc_request = 1
num_die = 2
return_string = ""
roll_string = str(num_die) + "d6"
damage = vroll(roll_string)
return_string = (
    f' -title "{name}\'s Fire Rune burns the target!" '
    f' -desc "While restrained by the shackles, the target takes {damage} fire damage at the start of each of its turns. The target can repeat the **DC {8+proficiencyBonus+constitutionMod} Strength saving throw** at the end of each of its turns, banishing the shackles on a success." '
    f' -f "Damage|{str(damage)}|inline" '
)
return_string += f' -footer "{ctx.prefix}{ctx.alias}" '
return return_string
</drac2>