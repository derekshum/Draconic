!snippet frost5 tembed
<drac2>
num = 5
cc_name = "Staff of Frost"
cc_value = character().get_cc(cc_name)
if cc_value >= num:
    cc_use = num
    character().mod_cc(cc_name, -cc_use)
    return_string = " -i"
else:
    cc_use = 0
    return_string = f' -f "No {cc_name} Charges Left|Probably ignore this spell."'
cc_current = cc_str(cc_name)
return_string += f' -f "{cc_name} (-{cc_use})| {cc_current}|inline"'
return return_string
</drac2>