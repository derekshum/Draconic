!alias mm tembed
<drac2>
cc_request = 1
is_resistant = False
is_vulnerable = False
for input in &ARGS&:
   input = input.lower()
   length = len(input)
   if input.isnumeric():
       cc_request = int(input)
   elif input == "resistant"[0:length] or input == "resistance"[0:length]:
       is_resistant = True
   elif input == "vulnerable"[0:length] or input == "vulnerability"[0:length]:
       is_vulnerable = True
cc_name = "Wand of Magic Missiles"
ability_name = "their " + cc_name
cc_value = character().get_cc(cc_name)
return_string = ""
if cc_value >= cc_request:
    cc_use = cc_request
    character().mod_cc(cc_name, -cc_use)
    darts = 2 + cc_request
    if is_resistant and is_vulnerable:     
        return_string += f' -f "Calculation Uncertainty|Resisted and Vulnerable damage may have a lower total than displayed due to rounding down odds." '    
    roll_string = "1d4+1[force]"
    if is_resistant:
        roll_string = "(" + roll_string + ")/2"
    if is_vulnerable:
        roll_string = "(" + roll_string + ")*2"
    damage = vroll(roll_string)
    return_string = (
        f' -title "{name} uses {ability_name}!" '
        f' -desc "Each dart hits a creature of your choice that you can see within range. A dart deals 1d4+1 force damage to its target. The darts all strike simultaneously and you can direct them to hit one creature or several." '
        f' -f "Damage ({darts} Darts)|{str(damage)} (Total: `{int(damage.total) * darts}`)|inline" '
        )
else:
    cc_use = 0
    return_string = (
        f' -title "{name} fails to use {ability_name}!" '
        f' -desc "No {cc_name} remaining." '
        )
cc_current = character().cc_str(cc_name)
return_string += (
    f' -f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    f' -footer "{ctx.prefix}{ctx.alias} [uses] [res] [vuln]" '
    )
return return_string
</drac2>