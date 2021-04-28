!alias devout tembed
<drac2>
cc_name_1 = "Amulet of the Devout"
cc_value = character().get_cc(cc_name)
return_string = ""
if cc_value < 1:
    cc_use = 0
    return_string = (
        f' -title "{name} fails to use their {cc_name}!" '
        f' -desc "Your {cc_name} has no remaining charges." '
        )
elif false: #TODO: if CD is full
    
else:
    cc_use = 1
    character().mod_cc(cc_name, -cc_use)
    return_string = (
        f' -title "{name} uses their {cc_name}!" '
        f' -desc "While you wear this amulet, you can use your Channel Divinity feature without expending one of the feature’s uses. Once this property is used, it can’t be used again until the next dawn." '
        #f' -f "Weapon Bonus | +{cc_use}|inline" '
        )
cc_current = cc_str(cc_name)
return_string += (
    f' -f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    f' -footer "{ctx.prefix}{ctx.alias}" '
    )
return return_string
</drac2>