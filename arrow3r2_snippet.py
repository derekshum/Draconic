!snippet p3r2 tembed
<drac2>
num = 2
cc_name = "+3 Arrows"
cc_value = character().get_cc(cc_name)
if cc_value < num:
    1 = 0   #not enough +3 Arrows left
cc_use = num
character().mod_cc(cc_name, -cc_use)
return_string = f'-b 3 -d 3 -rr {num}'
cc_current = cc_str(cc_name)
return_string += f' -f "{cc_name} (-{cc_use})| {cc_current}|inline"'
return return_string
</drac2>