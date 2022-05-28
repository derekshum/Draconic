!snippet bfr1 tembed
<drac2>
num = 1
cc_name = "Blood Fury Tattoo"
cc_value = character().get_cc(cc_name)
if cc_value >= num:
    cc_use = num
    character().mod_cc(cc_name, -cc_use)
    return_string = f'-d{num} 4d6'
else:
    cc_use = 0
    return_string = f' -f "No {cc_name} Charges Left|This attack was made without the additional necrotic damage."'
cc_current = character().cc_str(cc_name)
return_string += f' -f "{cc_name} (-{cc_use})| {cc_current}|inline"'
return return_string
</drac2>