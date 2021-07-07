!snippet fots tembed
<drac2>
ability_name = "Fury of the Small"
cc_name = ability_name
cc_value = character().get_cc(cc_name)
if cc_value >= 1:
    cc_use = 1
    character().mod_cc(cc_name, -cc_use)
    return_string = (f' -d1 {str(level)} '
        f' -f "Fury of the Small|When you damage a creature with an attack or a spell and the creature\'s size is larger than yours, you can cause the attack or spell to deal extra damage to the creature. The extra damage equals your level. Once you use this trait, you can\'t use it again until you finish a short or long rest." '
        )
else:
    cc_use = 0
    return_string = (
        f' -f "Fury of the Small unavailable|Take a rest." '
        )
cc_current = cc_str(cc_name)
return_string += (
    f' -f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    )
return return_string
</drac2>