!alias flash tembed
<drac2>
input_recieved = False
if len(&ARGS&) > 0:
    input_recieved = True
    args = &ARGS&        
    input = int(args[0])
ability_name = "Flash of Genius"
cc_name = "Flash of Genius"
cc_value = character().get_cc(cc_name)
return_string = ""
if cc_value >= 1:
    cc_use = 1
    character().mod_cc(cc_name, -cc_use)
    return_string = (
        f'-title "{name} uses {ability_name}!" '
        f'-desc "When you or another creature you can see within 30 feet of you makes an ability check or a saving throw, you can use your reaction to add your Intelligence modifier to the roll." '
        )
    if input_recieved:
        return_string += (f'-f "New Roll|{str(input)} + {str(intelligenceMod)} = {str(int(input)+intelligenceMod)}|inline" ')
    else:
        return_string += (f'-f "Roll Bonus|+{intelligenceMod}|inline" ')
else:
    cc_use = 0
    return_string = (
        f' -title "{name} fails to use {ability_name}!" '
        f' -desc "Take a long rest." '
        )
cc_current = cc_str(cc_name)
return_string += (
    f'-f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    f'-footer "{ctx.prefix}{ctx.alias} [original roll (optional)]"'
    )
return return_string
</drac2>