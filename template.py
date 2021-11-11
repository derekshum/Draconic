!alias template tembed #TODO
<drac2>
#cc_request = 1
#num_die = 1
#crit_text = ""
#is_resistant = False
#is_vulnerable = False
#for input in &ARGS&:
#    input = input.lower()
#    length = len(input)
#    if input.isnumeric():
#        cc_request = int(input)
#    elif input == "critical"[0:length]:
#        num_die = 2
#        crit_text = " (CRIT!)"
#    elif input == "resistant"[0:length] or input == "resistance"[0:length]:
#        is_resistant = True
#    elif input == "vulnerable"[0:length] or input == "vulnerability"[0:length]:
#        is_vulnerable = True
ability_name = ""   #TODO
cc_name = ""    #TODO
cc_value = character().get_cc(cc_name)
return_string = ""
if cc_value >= cc_request:
    cc_use = cc_request
    character().mod_cc(cc_name, -cc_use)
    #damage = vroll(str(num_die) + "d6")
    return_string = (
        f'-title "{name} uses {ability_name}!" '
        f'-desc "" '    #TODO
        #f' -f "Damage{crit_text}|{str(damage)}|inline" '
        )
else:
    cc_use = 0
    return_string = (
        f' -title "{name} fails to use {ability_name}!" '
        f' -desc "" '   #TODO
        )
cc_current = cc_str(cc_name)
return_string += (
    f'-f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    f'-footer "{ctx.prefix}{ctx.alias}" '    #TODO: add any additional inputs
    )
return return_string
</drac2>