!snippet a3r1 tembed
<drac2>
num = 1
bonus = 3
cc_name = "+" + bonus +" Arrows"
cc_value = character().get_cc(cc_name)
if cc_value >= num:
    cc_use = num
    character().mod_cc(cc_name, -cc_use)
    return_string = f' -b{num} {bonus} -d{num} {bonus} '
else:
    cc_use = 0
    return_string = f' -f "No {cc_name} Left|This attack was made with a mundane ammunition." '
cc_current = character().cc_str(cc_name)
return_string += f' -f "{cc_name} (-{cc_use})| {cc_current}|inline" '
return return_string
</drac2>