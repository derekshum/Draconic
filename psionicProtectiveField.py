!alias pf tembed
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
ability_name = "Protective Field"
cc_name = "Psionic Power: Psionic Energy"
cc_value = character().get_cc(cc_name)
return_string = ""
if cc_value >= cc_request:
    cc_use = cc_request
    character().mod_cc(cc_name, -cc_use)
    if is_resistant and is_vulnerable:     
        return_string += f' -f "Calculation Uncertainty|Resisted and Vulnerable damage may have a lower total than displayed due to rounding down odds." '    
    roll_string = f'1d6+{intelligenceMod}' #not set up for level 5+ psi warrior
    if is_resistant:
        roll_string = "(" + roll_string + ")/2"
    if is_vulnerable:
        roll_string = "(" + roll_string + ")*2"
    damage = vroll(roll_string)
    return_string = (
        f' -title "{name} uses {ability_name}!" '
        f' -desc "When you or another creature you can see within 30 feet of you takes damage, you can use your reaction to expend one Psionic Energy die, roll the die, and reduce the damage taken by the number rolled plus your Intelligence modifier." '
        f' -f "Damage Reduction|{str(damage)}|inline" '
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