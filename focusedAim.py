!alias f tembed
<drac2>
additional_disp = False
if len(&ARGS&) > 0:
    args = &ARGS&
    cc_request = int(args[0]) #ki points to spend
    if len(args) > 1:
        additional_disp = True; 
        disp_num = int(args[1]) #initial attack roll
else:
    cc_request = 1
ability_name = "Focused Aim"
cc_name = "Ki Points"
cc_value = character().get_cc(cc_name)
return_string = ""
if cc_request < 1 or cc_request > 3:
    cc_use = 0
    return_string = (
        f' -title "{name} fails to use {ability_name}!" '
        f' -desc "{str(args[0])} is not a valid input. {ability_name} spends 1 to 3 {cc_name}." '
        )
elif cc_value < cc_request:
    cc_use = 0
    return_string = (
        f' -title "{name} fails to use {ability_name}!" '
        f' -desc "Not enough {cc_name}." '
        )
else:
    cc_use = cc_request
    character().mod_cc(cc_name, -cc_request)
    attack_roll_bonus = cc_use * 2
    return_string = (
        f' -title "{name} uses {ability_name}!" '
        f' -desc "When you miss with an attack roll, you can spend 1 to 3 ki points to increase your attack roll by 2 for each of these ki points you spend, potentially turning the miss into a hit." '
        )
    if additional_disp:
        return_string += f' -f "New Attack Roll | {disp_num} + {attack_roll_bonus} = {disp_num + attack_roll_bonus}|inline" '
    else:
        return_string += f' -f "Attack Roll Bonus | +{attack_roll_bonus}|inline" '
cc_current = character().cc_str(cc_name)
return_string += (
    f' -f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    f' -footer "{ctx.prefix}{ctx.alias} [# ki (optional, 1-3, default 1)] [initial attack roll]" '
    )
return return_string
</drac2>