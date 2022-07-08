tembed  # !alias mm 
<drac2>
cc_request = 1
is_evo = False
is_curse = False
is_resistant = False
is_vulnerable = False
for input in &ARGS&:
    input = input.lower()
    length = len(input)
    if input.isnumeric():
        cc_request = int(input)
    elif input == "evocation"[0:length] or input == "empowered evocation"[0:length]:
        is_evo = True
    elif input == "curse"[0:length] or input == "hexblade's curse"[0:length]:
        is_curse = True
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
    roll_string = "1d4+1"
    if is_evo:
        roll_string += "+" + intelligenceMod  #idk why these aren't part of character()
    if is_curse:
        roll_string += "+" + proficiencyBonus
    roll_string += "[force]"
    if is_resistant and is_vulnerable:     
        return_string += f' -f "Calculation Uncertainty|Resisted and Vulnerable damage may have a lower total than displayed due to rounding down odds." '    
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
        f' -desc "Not enough {cc_name} remaining." '
        )
cc_current = character().cc_str(cc_name)
return_string += f' -f "{cc_name} (-{cc_use})| {cc_current}|inline" '
if cc_use > 0 and character().get_cc(cc_name) == 0:
    rc = vroll("d20")
    return_string += f' -f "The {cc_name} is fully expent...|{str(rc)}: '
    if rc.total > 1:
        return_string += f'it remains!'
    else:
        return_string += f'it crumbles! D='
    return_string += f'|inline" '
return_string += f' -footer "{ctx.prefix}{ctx.alias} [uses/curse/evo/res/vuln]" '
return return_string
</drac2>