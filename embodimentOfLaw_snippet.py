!snippet eol tembed
<drac2>
cc_name = "Embodiment of Law"
ability_name = cc_name
cc_value = 0
cc_value = character().get_cc(cc_name)
if cc_value > 0:
    cc_use = 1
    character().mod_cc(cc_name, -cc_use)
    return_string = (
        f'-f "{ability_name}|If you cast a spell of the enchantment school using a spell slot of 1st level or higher, you can change the spell\'s casting time to 1 bonus action for this casting, provided the spell\'s casting time is normally 1 action." '
        )
else:
    cc_use = 0
    return_string = (
        f' -f "Failure to use {ability_name}|No uses left, take a long rest." '
        )
cc_use_string = ""
if cc_use > 0:
    cc_use_string = " -(" + cc_use + ")"
return_string += (f'-f "{cc_name} {cc_use_string}| {cc_str(cc_name)}|inline" ')
return return_string
</drac2>