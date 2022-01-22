#!cc create "Clockwork Amulet" -min 0 -max 1 -type bubble -reset long -desc "When you make an attack roll while wearing the amulet, you can forgo rolling the d20 to get a 10 on the die."

!snippet ca tembed
<drac2>
num = 1
cc_name = "Clockwork Amulet"
cc_value = character().get_cc(cc_name)
if cc_value >= num:
    cc_use = num
    character().mod_cc(cc_name, -cc_use)
    return_string = (
        f' hit{num} '
        f' -f "{cc_name}|When you make an attack roll while wearing the amulet, you can forgo rolling the d20 to get a 10 on the die." '
        )
else:
    cc_use = 0
    return_string = f' -f "Your {cc_name} has already been used today|This attack was made without this enhancement."'
cc_current = cc_str(cc_name)
return_string += f' -f "{cc_name} (-{cc_use})| {cc_current}|inline"'
return return_string
</drac2>