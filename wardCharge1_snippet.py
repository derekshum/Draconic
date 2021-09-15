!snippet w1 tembed 
<drac2>
spell_level = 1
cc_name = "ward"
cc_value = character().get_cc(cc_name)
cc_max = character().get_cc_max(cc_name)
charge = int(2 * spell_level)
return_string = f'-f "Arcane Ward|Whenever you cast an abjuration spell of 1st level or higher, the ward regains a number of hit points equal to twice the level of the spell." '
if cc_value + charge > cc_max:
        charge = cc_max - cc_value
character().mod_cc(cc_name, charge)
cc_current = cc_str(cc_name)
return_string += f'-f "{cc_name} (+{charge})|{cc_current}|inline" '
return_string += f'-gif "https://media.discordapp.net/attachments/533815265562066957/887487154081636372/a4fec7faa0b32a7945ed3bae10bae2d7.gif" '
return return_string
</drac2>