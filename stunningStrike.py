!alias stun tembed
<drac2>
dc_boost = 0
cc_request = 1
for input in &ARGS&:
   input = input.lower()
   length = len(input)
   if input.isnumeric():
       cc_request = int(input)
ability_name = "Stunning Strike"
cc_name = "Ki Points"
cc_value = character().get_cc(cc_name)
return_string = ""
if cc_value >= cc_request:
    cc_use = cc_request
    character().mod_cc(cc_name, -cc_use)
    return_string = (
        f' -title "{name} uses {ability_name}!" '
        f' -desc "When you hit another creature with a melee weapon attack, you can spend 1 ki point to attempt a stunning strike. The target must succeed on a **DC {8 + wisdomMod + proficiencyBonus + dc_boost}** Constitution saving throw or be stunned until the end of your next turn." '
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
    f' -footer "{ctx.prefix}{ctx.alias} [uses]" '
    )
return return_string
</drac2>