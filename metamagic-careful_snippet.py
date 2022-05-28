!snippet careful tembed
<drac2>
ability_name = "Careful Spell"
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
        f'-f "{ability_name}|When you cast a spell that forces other creatures to make a saving throw, you can protect some of those creatures from the spell\'s full force. To do so, you spend 1 sorcery point and choose up to **{max(charismaMod,1)}** creatures. A chosen creature automatically succeeds on its saving throw against the spell." '
        )
else:
    return_string = (
        f' -f "Failure to use {ability_name}|No {cc_name_1} or {cc_name_2} left, take a long rest." '
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
return return_string
</drac2>