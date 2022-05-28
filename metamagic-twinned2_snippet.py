!snippet twinned2 tembed
<drac2>
lvl = 2
ability_name = "Twinned Spell"
cc_name_1 = "Metamagic Points"
cc_name_2 = "Sorcery Points"
cc_value_1 = 0
if character().cc_exists(cc_name_1):
    cc_value_1 = character().get_cc(cc_name_1)
cc_value_2 = 0
if character().cc_exists(cc_name_2):
    cc_value_2 = character().get_cc(cc_name_2)
cc_use_1 = 0
cc_use_2 = 0
if cc_value_1 + cc_value_2 >= lvl:
    if cc_value_1 >= lvl:
        cc_use_1 = lvl
        character().mod_cc(cc_name_1, -cc_use_1)
    elif cc_value_1 < lvl and cc_value_1 > 0:
        cc_use_1 = cc_value_1
        cc_use_2 = lvl - cc_value_1
        character().mod_cc(cc_name_1, -cc_use_1)
        character().mod_cc(cc_name_2, -cc_use_2)
    else:
        cc_use_2 = lvl
        character().mod_cc(cc_name_2, -cc_use_2)
    return_string = (
        f'-l {lvl} -f "{ability_name} ({lvl})|When you cast a spell that targets only one creature and doesn\'t have a range of self, you can spend a number of sorcery points equal to the spell\'s level to target a second creature in range with the same spell (1 sorcery point if the spell is a cantrip).\n\nTo be eligible, a spell must be incapable of targeting more than one creature at the spell\'s current level. For example, magic missile and scorching ray aren\'t eligible, but ray of frost and chromatic orb are." '
        )
else:
    return_string = (
        f' -f "Failure to use {ability_name} ({lvl})|Not enough {cc_name_1} or {cc_name_2} left, take a long rest." '
        )
if character().cc_exists(cc_name_1):
    cc_use_string_1 = ""
    if cc_use_1 > 0:
        cc_use_string_1 = " (-" + cc_use_1 + ")"
    return_string += (f'-f "{cc_name_1} {cc_use_string_1}| {character().cc_str(cc_name_1)}|inline" ')
if character().cc_exists(cc_name_2):
    cc_use_string_2 = ""
    if cc_use_2 > 0:
        cc_use_string_2 = " (-" + cc_use_2 + ")"
    return_string += (f'-f "{cc_name_2} {cc_use_string_2}| {character().cc_str(cc_name_2)}|inline" ')
return return_string
</drac2>