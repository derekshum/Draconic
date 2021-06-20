!snippet net tembed
<drac2>
return_string = ""
cc_name = "Nets"
cc_value = character().get_cc(cc_name)
if cc_value >= 1:
    cc_use = 1
    character().mod_cc(cc_name, -cc_use)
else:
    cc_use = 0
    return_string += (f' -f "No more nets."')
cc_current = cc_str(cc_name)
return_string += (f' -f "{cc_name} (-{cc_use})| {cc_current}|inline"')
return return_string
</drac2>