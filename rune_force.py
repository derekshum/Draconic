!alias forceRune tembed
<drac2>
cc_request = 1
num_die = 2
crit_text = ""
is_resistant = False
is_vulnerable = False
for input in &ARGS&:
   input = input.lower()
   length = len(input)
   if input == "critical"[0:length]:
       num_die = 4
       crit_text = " (CRIT!)"
   elif input == "resistant"[0:length] or input == "resistance"[0:length]:
       is_resistant = True
   elif input == "vulnerable"[0:length] or input == "vulnerability"[0:length]:
       is_vulnerable = True
cc_name = "Spike of Ethereal Tethers Rune"
ability_name = "invokes their " + cc_name
cc_value = character().get_cc(cc_name)
return_string = ""
if cc_value >= cc_request:
    cc_use = cc_request
    character().mod_cc(cc_name, -cc_use)
    roll_string = str(num_die) + "d6"
    if is_resistant and is_vulnerable:     
        return_string += f' -f "Calculation Uncertainty|Resisted and Vulnerable damage may have a lower total than displayed due to rounding down odds." '    
    if is_resistant:
        roll_string = "(" + roll_string + ")/2"
    if is_vulnerable:
        roll_string = "(" + roll_string + ")*2"
    damage = vroll(roll_string+"[force]")
    return_string = (
        f' -title "{name} {ability_name}!" '
        f' -desc "When you make an attack with the ~~whip~~ dagger and hit, you can use your reaction to invoke the ~~whip\'s~~ dagger\'s rune. Doing so increases the extra ~~fire~~ force damage dealt by the ~~whip~~ dagger to 2d6." '
        f' -f "Damage{crit_text}|{str(damage)}|inline" '
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
    f' -footer "{ctx.prefix}{ctx.alias} [crit] [res] [vuln]" '
    )
return return_string
</drac2>