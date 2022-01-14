!cc create "Perfected Guardian" -min 0 -max proficiencyBonus -type bubble -reset long -desc "When a Huge or smaller creature you can see ends its turn within 30 feet of you, you can use your reaction to magically force the creature to make a Strength saving throw against your spell save DC, pulling the creature up to 30 feet toward you to an unoccupied space. If you pull the target to a space within 5 feet of you, you can make a melee weapon attack against it as part of this reaction."

!alias template tembed #TODO
<drac2>
cc_request = 1
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
    if is_resistant and is_vulnerable:     
        return_string += f' -f "Calculation Uncertainty|Resisted and Vulnerable damage may have a lower total than displayed due to rounding down odds." '    
    roll_string = str(num_die) + "d6"   #TODO
    if is_resistant:
        roll_string = "(" + roll_string + ")/2"
    if is_vulnerable:
        roll_string = "(" + roll_string + ")*2"
    damage = vroll(roll_string)
    return_string = (
        f' -title "{name} uses {ability_name}!" '
        f' -desc "" '    #TODO
        f' -f "Damage{crit_text}|{str(damage)}|inline" '
        )
else:
    cc_use = 0
    return_string = (
        f' -title "{name} fails to use {ability_name}!" '
        f' -desc "No {cc_name} remaining." '
        )
cc_current = cc_str(cc_name)
return_string += (
    f' -f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    f' -footer "{ctx.prefix}{ctx.alias} [uses] [crit] [res] [vuln]" '    #TODO: input specifications
    )
return return_string
</drac2>