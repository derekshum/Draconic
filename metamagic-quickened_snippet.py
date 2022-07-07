!snippet quickened tembed
<drac2>
cost = 2
ability_name = "Quickened Spell"
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
if cc_value_1 + cc_value_2 >= cost:
    if cc_value_1 >= cost:
        cc_use_1 = cost
        character().mod_cc(cc_name_1, -cc_use_1)
    elif cc_value_1 < cost and cc_value_1 > 0:
        cc_use_1 = cc_value_1
        cc_use_2 = cost - cc_value_1
        character().mod_cc(cc_name_1, -cc_use_1)
        
    else:
        cc_use_2 = cost
        character().mod_cc(cc_name_2, -cc_use_2)
    return_string = (
        f'-f "{ability_name}|When you cast a spell that has a casting time of 1 action, you can spend 2 sorcery points to change the casting time to 1 bonus action for this casting." '
        )
else:
    return_string = (
        f' -f "Failure to use {ability_name}|Not enough {cc_name_1} or {cc_name_2} left, take a long rest." '
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