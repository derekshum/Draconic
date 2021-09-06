!snippet p3r1 tembed
<drac2>
num = 1
cc_name = "+3 Arrows"
cc_value = character().get_cc(cc_name)
if cc_value >= num:
    cc_use = num
    character().mod_cc(cc_name, -cc_use)
    return_string = f' -b 3 -d 3 '
else:
    cc_use = 0
    return_string = f' -f "No +3 Arrows Left|This attack was made with a mundane arrow." '
cc_current = cc_str(cc_name)
return_string += f' -f "{cc_name} (-{cc_use})| {cc_current}|inline" '
return return_string
</drac2>