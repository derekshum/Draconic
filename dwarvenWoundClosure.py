!alias regen tembed
<drac2>
cc_request = 1
cc_name = "Hit Dice (d12)"
cc_value = character().get_cc(cc_name)
return_string = ""
if cc_value >= cc_request:
    cc_use = cc_request
    character().mod_cc(cc_name, -cc_use)
    max_heal = vroll("2*(d12+"+str(constitutionMod)+")")
    return_string = (
        f' -title "{name} dodges!" '
        f' -desc "Whenever you take the Dodge action in combat, you can spend one Hit Die to heal yourself. Roll the die, add your Constitution modifier, and regain a number of hit points equal to the total (minimum of 1).\n\nWhenever you roll a Hit Die to regain hit points, double the number of hit points it restores." '
        f' -f "Heal Roll|{str(max_heal)}|inline" '
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
else:
    cc_use = 0
    return_string = (
        f' -title "{name} fails to use {ability_name}!" '
        f' -desc "No {cc_name} remaining." '
        )
cc_current = character().cc_str(cc_name)
return_string += (
    f' -f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    f' -footer "{ctx.prefix}{ctx.alias}" '
    )
return return_string
</drac2>