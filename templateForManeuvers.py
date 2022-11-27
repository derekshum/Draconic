!alias MANEUVER tembed #TODO
<drac2>
cc_request = 1
num_die = 1
crit_text = ""
for input in &ARGS&:
   input = input.lower()
   length = len(input)
   if input == "critical"[0:length]:
       num_die = 2
       crit_text = " (CRIT!)"
ability_name = "MANEUVER NAME HERE" #TODO
cc_name = "Superiority Dice"
cc_value = character().get_cc(cc_name)
return_string = ""
if cc_value >= cc_request:
    cc_use = cc_request
    character().mod_cc(cc_name, -cc_use)
    if FighterLevel >= 18:  #may be incorrect for non BM fighters
        roll_string = "1d12"
    elif FighterLevel >= 10:
        roll_string = "1d10"
    elif FighterLevel >= 3: 
        roll_string = "1d8"
    else:
        roll_string = "1d6"
    damage = vroll(roll_string)
    return_string = (
        f' -title "{name} uses {ability_name}!" '
        f' -desc "PUT MANEUVER DESCRIPTION HERE" ' #TODO
        f' -f "Roll{crit_text}|{str(damage)}|inline" '
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
    f' -footer "{ctx.prefix}{ctx.alias} [crit]" '
    )
return return_string
</drac2>