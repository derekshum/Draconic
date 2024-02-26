!alias emp tembed
<drac2>
ability_name = "Empowered Spell"
cc_name_1 = "Metamagic Points"
cc_name_2 = "Sorcery Points"
rs = ""
for input in &ARGS&:
    rs += input.lower()
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
        f'-desc "When you roll damage for a spell, you can spend 1 sorcery point to reroll a number of the damage dice up to your Charisma modifier (minimum of one). You must use the new rolls. You can use Empowered Spell even if you have already used a different Metamagic option during the casting of the spell." '
        )
    if len(rs) > 0:
        return_string += f'-f "Damage Change|{vroll(rs)}|inline" '
else:
    return_string = (
        f' -title "{name} fails to use {ability_name}!" '
        f' -desc "No {cc_name_1} or {cc_name_2} left, take a long rest." '
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
return_string += (f'-footer "{ctx.prefix}{ctx.alias}"')
return return_string
</drac2>