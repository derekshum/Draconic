!alias devout tembed
<drac2>
cc_name = "Amulet of the Devout"
cc_value = character().get_cc(cc_name)
cc_recharge_name = "Channel Divinity"
cc_recharge_value = character().get_cc(cc_recharge_name)
cc_recharge_value_max = character().get_cc_max(cc_recharge_name)
return_string = ""
if cc_value < 1:
    cc_use = 0
    cc_recharge_change = 0
    return_string = (
        f' -title "{name} fails to use their {cc_name}!" '
        f' -desc "Your {cc_name} has no remaining charges." '
        )
elif cc_recharge_value >= cc_recharge_value_max: 
    cc_use = 0
    cc_recharge_change = 0
    return_string = (
        f' -title "{name} fails to use their {cc_name}!" '
        f' -desc "You are at your maximum number of {cc_recharge_name}(s)." '
        )
else:
    cc_use = 1
    cc_recharge_change = 1
    character().mod_cc(cc_name, -cc_use)
    character().mod_cc(cc_recharge_name, cc_recharge_change)
    return_string = (
        f' -title "{name} uses their {cc_name}!" '
        f' -desc "While you wear this amulet, you can use your Channel Divinity feature without expending one of the feature’s uses. Once this property is used, it can’t be used again until the next dawn." '
        )
cc_current = cc_str(cc_name)
cc_recharge_current = cc_str(cc_recharge_name)
return_string += (
    f' -f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    f' -f "{cc_recharge_name} (+{cc_recharge_change})| {cc_recharge_current}|inline" '
    f' -footer "{ctx.prefix}{ctx.alias}" '
    )
return return_string
</drac2>