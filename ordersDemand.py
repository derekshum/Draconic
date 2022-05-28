!alias od tembed
<drac2>
ability_name = "Channels Divinity to invoke Order's Demand"
cc_name = "Channel Divinity"
cc_value = character().get_cc(cc_name)
return_string = ""
if cc_value >= 1:
    cc_use = 1
    character().mod_cc(cc_name, -cc_use)
    return_string = (
        f'-title "{name} {ability_name}!" '
        f'-desc "You can use your Channel Divinity to exert an intimidating presence over others.\n\nAs an action, you present your holy symbol, and each creature of your choice that can see or hear you within 30 feet of you must succeed on a Wisdom saving throw or be charmed by you until the end of your next turn or until the charmed creature takes any damage. You can also cause any of the charmed creatures to drop what they are holding when they fail the saving throw." '
        )
else:
    cc_use = 0
    return_string = (
        f' -title "{name} fails to {ability_name}!" '
        f' -desc "Take a rest." '
        )
cc_current = character().cc_str(cc_name)
return_string += (
    f'-f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    f'-footer "{ctx.prefix}{ctx.alias}" '
    )
return return_string
</drac2>