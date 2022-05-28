!alias phoenix tembed
<drac2>
cc_name = "FierySoul"
cc_value = character().get_cc(cc_name)
return_string = ""
if cc_value >= 4:
    cc_use = 4
    character().mod_cc(cc_name, -cc_use)
    return_string = (
        f'-title "{name} uses their Phoenix Crown to reinvigorate themself!" '
        f'-desc "When you are reduced to 0 hit points but not killed outright, you can expend 4 charges to drop to 1 hit point instead, as phoenix fire invigorates you." '    
        )
else:
    cc_use = 0
    return_string = (
        f' -title "{name} fails to use their Phoenix Crown!" '
        f' -desc "This ability requires 4 charges." '
        )
cc_current = character().cc_str(cc_name)
return_string += (
    f'-f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    f'-footer "{ctx.prefix}{ctx.alias}"'
    )
return return_string
</drac2>