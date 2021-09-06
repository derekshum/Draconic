!snippet bfr2 tembed
<drac2>
num = 2
cc_name = "Blood Fury Tattoo"
cc_value = character().get_cc(cc_name)
n = min(cc_value, num)
return_string = f'-rr {num}'
cc_use = n
character().mod_cc(cc_name, -cc_use)
if n == 0:  
    return_string += f' -f "No {cc_name} Charges Left|These attacks were made without the additional necrotic damage."'
else:
    return_string += f' -d{n} 4d6'
    if n < num:
        b = " was"
        if n > 1:
            b = "s were"
        return_string += f' -f "Not Enough {cc_name} Charges Left|The {n} remaining {cc_name} charge{b} expent." '
cc_value = character().get_cc(cc_name)
cc_current = cc_str(cc_name)
return_string += f' -f "{cc_name} (-{cc_use})| {cc_current}|inline"'
return return_string
</drac2>