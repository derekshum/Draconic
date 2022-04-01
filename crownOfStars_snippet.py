!snippet crown tembed
<drac2>
num = 1
cc_name = "Crown of Stars"
cc_value = character().get_cc(cc_name)
if cc_value >= num:
    cc_use = num
    character().mod_cc(cc_name, -cc_use)
    return_string = ""
else:
    cc_use = 0
    return_string = f' -f "No {cc_name} Motes Left|Probably ignore this attack."'
cc_current = cc_str(cc_name)
return_string += f' -f "{cc_name} (-{cc_use})| {cc_current}|inline"'
return return_string
</drac2>