#!cc create "Defensive Field" -min 0 -max proficiencyBonus -type bubble -reset long -desc "As a bonus action, you can gain temporary hit points equal to your level in this class, replacing any temporary hit points you already have. You lose these temporary hit points if you doff the armor. You can use this bonus action a number of times equal to your proficiency bonus, and you regain all expended uses when you finish a long rest."
#TODO: updating num defensive field to PB when needed with !updateDefensiveField

!alias df tembed
<drac2>
cc_name = "Defensive Field"
cc_value = character().get_cc(cc_name)
return_string = ""
if cc_value >= 1:
    cc_use = 1
    character().mod_cc(cc_name, -cc_use)
    character().set_temp_hp(ArtificerLevel)
    return_string = (
        f'-title "{name} activates their {cc_name}!" '
        f'-desc "As a bonus action, you can gain temporary hit points equal to your level **({ArtificerLevel})** in this class. You lose these temporary hit points if you doff the armor." '
        )
else:
    cc_use = 0
    return_string = (
        f'-title "{name} fails to activate their {cc_name}!" '
        f'-desc "Take a long rest." '
        )
cc_current = character().cc_str(cc_name)
return_string += (
    f'-f "HP|{character().hp_str()}|inline" '
    f'-f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    f'-footer "{ctx.prefix}{ctx.alias}"'
    )
return return_string
</drac2>