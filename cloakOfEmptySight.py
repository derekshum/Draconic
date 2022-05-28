!alias coes tembed
<drac2>
cc_request = 1
for input in &ARGS&:
    input = input.lower()
    length = len(input)
    if input.isnumeric():
        cc_request = int(input)
ability_name = "their Cloak of Empty Sight"
cc_name = "Cloak of Empty Sight"
cc_value = character().get_cc(cc_name)
return_string = ""
if cc_value >= cc_request:
    cc_use = cc_request
    character().mod_cc(cc_name, -cc_use)
    return_string = (
        f' -title "{name} uses {ability_name}!" '
        f' -desc "When you hit a Large or smaller creature with a weapon attack, you can expend one charge to force the target to make a **DC 17 Strength saving throw**. On a failed save, you push the target up to 10 feet away from you." '
        )
else:
    cc_use = 0
    return_string = (
        f' -title "{name} fails to use {ability_name}!" '
        f' -desc "No charges remaining." '
        )
cc_current = character().cc_str(cc_name)
return_string += (
    f' -f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    f' -footer "{ctx.prefix}{ctx.alias} [uses]" '
    )
return return_string
</drac2>