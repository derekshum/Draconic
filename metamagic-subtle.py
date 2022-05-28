!alias subtle tembed
<drac2>
ability_name = "Subtle Spell"
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
if cc_value_1 + cc_value_2 >= 1:
    if cc_value_1 > 0:
        cc_use_1 = 1
        character().mod_cc(cc_name_1, -cc_use_1)
    else:    #cc_value_2 > 1:
        cc_use_2 = 1
        character().mod_cc(cc_name_2, -cc_use_2)
    return_string = (
        f'-title "{name} uses {ability_name}!" '
        f'-desc "When you cast a spell, you can spend 1 sorcery point to cast it without any somatic or verbal components." '
        )
else:
    return_string = (
        f' -title "{name} fails to use {ability_name}!" '
        f' -desc "No {cc_name_1} or {cc_name_2} left, take a long rest." '
        )
if character().cc_exists(cc_name_1):
    cc_use_string_1 = ""
    if cc_use_1 > 0:
        cc_use_string_1 = " (-" + cc_use_1 + ")"
    return_string += (f'-f "{cc_name_1} {cc_use_string_1}| {cc_str(cc_name_1)}|inline" ')
if character().cc_exists(cc_name_2):
    cc_use_string_2 = ""
    if cc_use_2 > 0:
        cc_use_string_2 = " (-" + cc_use_2 + ")"
    return_string += (f'-f "{cc_name_2} {cc_use_string_2}| {cc_str(cc_name_2)}|inline" ')
return_string += (f'-footer "{ctx.prefix}{ctx.alias}"')
return return_string
</drac2>