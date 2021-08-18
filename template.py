!alias template tembed #TODO
<drac2>
# input declaration
# if len(&ARGS&) > 0:
    # args = &ARGS&
    # input = args[0].lower()
    # #TODO
ability_name = ""   #TODO
cc_name = ""    #TODO
cc_value = character().get_cc(cc_name)
return_string = ""
if cc_value >= 1:
    cc_use = 1
    character().mod_cc(cc_name, -cc_use)
    return_string = (
        f'-title "{name} uses {ability_name}!" '
        f'-desc "" '    #TODO
        # TODO f' -f "Damage{crit_text}|{str(damage)}|inline" '
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