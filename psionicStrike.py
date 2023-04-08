!alias ps 
tembed
<drac2>
cc_request = 1
is_resistant = False
is_vulnerable = False
for input in &ARGS&:
   input = input.lower()
   length = len(input)
   if input == "resistant"[0:length] or input == "resistance"[0:length]:
       is_resistant = True
   elif input == "vulnerable"[0:length] or input == "vulnerability"[0:length]:
       is_vulnerable = True
ability_name = "Psionic Strike"
cc_name = "Psionic Power: Psionic Energy"
cc_value = character().get_cc(cc_name)
return_string = ""
if cc_value >= cc_request:
    cc_use = cc_request
    character().mod_cc(cc_name, -cc_use)
    if is_resistant and is_vulnerable:     
        return_string += f' -f "Calculation Uncertainty|Resisted and Vulnerable damage may have a lower total than displayed due to rounding down odds." '  
    roll_string='1d6'
    if level >= 17:
        roll_string='1d12'
    elif level >= 11:
        roll_string='1d10'
    elif level >= 5:
        roll_string='1d8'
    roll_string += f'+{intelligenceMod}'
    if is_resistant:
        roll_string = "(" + roll_string + ")/2"
    if is_vulnerable:
        roll_string = "(" + roll_string + ")*2"
    damage = vroll(roll_string)
    return_string = (
        f' -title "{name} uses {ability_name}!" '
        f' -desc "Once on each of your turns, immediately after you hit a target within 30 feet of you with an attack and deal damage to it with a weapon, you can expend one Psionic Energy die, rolling it and dealing force damage to the target equal to the number rolled plus your Intelligence modifier.\n\nWhen you deal damage to a target with your Psionic Strike, you can force the target to make a **DC {8 + proficiencyBonus + intelligenceMod} Strength saving throw**. If the save fails, you can knock the target prone or move it up to 10 feet in any direction horizontally." '
        f' -f "Damage|{str(damage)}[force]|inline" '
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
    f' -footer "{ctx.prefix}{ctx.alias}" '
    )
return return_string
</drac2>