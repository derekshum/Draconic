!alias grow tembed
<drac2>
ability_name = "a Potion of Growth"
cc_name = "Potions of Growth"
cc_value = character().get_cc(cc_name)
return_string = ""
cc_request = 1
if cc_value >= cc_request:
    cc_use = cc_request
    character().mod_cc(cc_name, -cc_use)
    return_string = (
        f' -title "{name} drinks {ability_name}!" '
        f' -desc "When you drink this potion, you gain the "enlarge" effect of the enlarge/reduce spell for 1d4 hours (no concentration required). The red in the potion\'s liquid continuously expands from a tiny bead to color the clear liquid around it and then contracts. Shaking the bottle fails to interrupt this process." '
        f' -f "Duration|{vroll("1d4")} hours|inline" '
        )
else:
    cc_use = 0
    return_string = (
        f' -title "{name} fails to drink {ability_name}!" '
        f' -desc "No {cc_name} remaining." '
        )
cc_current = character().cc_str(cc_name)
return_string += (
    f' -f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    f' -footer "{ctx.prefix}{ctx.alias}" '
    )
return return_string
</drac2>