!alias ar3 tembed
<drac2>
input = 1
if len(&ARGS&) > 0:
    args = &ARGS&
    input = int(args[0].lower())
if input > 1:
    ability_name = "+3 arrows"
else:
    ability_name = "+3 arrow"
cc_name = "+3 Arrows"
cc_value = character().get_cc(cc_name)
return_string = ""
if cc_value >= input:
    cc_use = input
    character().mod_cc(cc_name, -cc_use)
    return_string = (
        f'-title "{name} uses {input} {ability_name}!" '
        )
else:
    cc_use = 0
    return_string = (
        f'-title "{name} doesn\'t have {input} {ability_name} to use!" '
        )
cc_current = character().cc_str(cc_name)
return_string += (
    f'-f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    f'-footer "{ctx.prefix}{ctx.alias} [# used(optional)]" '
    )
return return_string
</drac2>