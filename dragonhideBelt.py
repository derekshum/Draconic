!alias dh tembed
<drac2>
cc_name = "Dragonhide Belt"
ability_name = "their " + cc_name
cc_value = character().get_cc(cc_name)
return_string = ""
cc_request = 1
if cc_value >= cc_request:
    cc_use = cc_request
    character().mod_cc(cc_name, -cc_use)
    ki_roll = vroll("d" + str(int(4 + int((MonkLevel + 1) / 6) * 2)))
    ki_cc = "Ki Points"
    ki_restore = min(ki_roll.total, character().get_cc_max(ki_cc) - character().get_cc(ki_cc))
    character().mod_cc(ki_cc, ki_restore)
    return_string = (
        f' -title "{name} uses {ability_name}!" '
        f' -desc "You can use an action to regain ki points equal to a roll of your Martial Arts die." '
        f' -f "Ki Restoration|{str(ki_roll)}|inline" '
        f' -f "Ki (+{ki_restore})|{cc_str(ki_cc)}|inline" '
        )
else:
    cc_use = 0
    return_string = (
        f' -title "{name} fails to use {ability_name}!" '
        f' -desc "Take a long rest." '
        )
cc_current = character().cc_str(cc_name)
return_string += (
    f' -f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    f' -footer "{ctx.prefix}{ctx.alias}" '
    )
return return_string
</drac2>