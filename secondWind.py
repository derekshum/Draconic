!alias 2nd tembed
<drac2>
cc_name = "Second Wind"
cc_value = character().get_cc(cc_name)
return_string = ""
if cc_value < 1:
    cc_use = 0
    cc_recharge_change = 0
    return_string = (
        f' -title "{name} fails to use {cc_name}!" '
        f' -desc "{cc_name} has no remaining uses." '
        )
else:
    cc_use = 1
    cc_recharge_change = 1
    character().mod_cc(cc_name, -cc_use)
    max_heal = vroll(f"1d10+{FighterLevel}")
    return_string = (
        f' -title "{name} uses {cc_name}." '
        f' -desc " On your turn, you can use a bonus action to regain {str(max_heal)} hit points. Once you use this feature, you must finish a short or long rest before you can use it again." '
        )
    former_hp = character().hp
    missing_hp = character().max_hp - former_hp
    if max_heal.total <= missing_hp: 
        character().modify_hp(max_heal.total)
        return_string += (
            f' -f "Healing|{str(former_hp)} + {str(max_heal.total)} = {str(character().hp)}/{str(character().max_hp)}|inline" '
            )
    elif missing_hp >= 0: 
        character().modify_hp(missing_hp)
        return_string += (
            f' -f "Healing|{str(former_hp)} + {str(missing_hp)} = {str(character().hp)}/{str(character().max_hp)}|inline" '
            f' -f "Unused healing|!hp {str(max_heal.total - missing_hp)}|inline" '
            )
    else: 
        return_string += (
            f' -f "Healing|{str(former_hp)} + 0 = {str(character().hp)}/{str(character().max_hp)}|inline" '
            f' -f "Unused healing|!hp {str(max_heal.total)}|inline" '
            ) 
cc_current = character().cc_str(cc_name)
return_string += (
    f' -f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    f' -footer "{ctx.prefix}{ctx.alias}" '
    )
return return_string
</drac2>