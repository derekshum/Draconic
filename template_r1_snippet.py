!snippet tr1 tembed  #TODO
<drac2>
num = 1
cc_name = ""    #TODO
cc_value = character().get_cc(cc_name)
if cc_value >= num:
    cc_use = num
    character().mod_cc(cc_name, -cc_use)
    return_string = (
        f' -d{num} XdY[type] '    #TODO
        f' -f"|" '  #TODO
        )
else:
    cc_use = 0
    return_string = f' -f "No {cc_name} Charges Left|This attack was made without this enhancement."'
cc_current = cc_str(cc_name)
return_string += f' -f "{cc_name} (-{cc_use})| {cc_current}|inline"'
return return_string
</drac2>