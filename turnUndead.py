!alias tu tembed
<drac2>
ability_name = "Channels Divinity to Turn Undead"
cc_name = "Channel Divinity"
cc_value = character().get_cc(cc_name)
return_string = ""
if cc_value >= 1:
    cc_use = 1
    character().mod_cc(cc_name, -cc_use)
    desc = "As an action, you present your holy symbol and speak a prayer censuring the undead. Each undead that can see or hear you within 30 feet of you must make a Wisdom saving throw. If the creature fails its saving throw, it is turned for 1 minute or until it takes any damage.\n\nA turned creature must spend its turns trying to move as far away from you as it can, and it can\'t willingly move to a space within 30 feet of you. It also can\'t take reactions. For its action, it can use only the Dash action or try to escape from an effect that prevents it from moving. If there\'s nowhere to move, the creature can use the Dodge action."
    if ClericLevel > 4:
        ability_name = "Channels Divinity to Turn and Destroy Undead"
        destroyCR = "1/2"
        if ClericLevel > 7:
            destroyCR = str(min(int((ClericLevel - 5) / 3), 4))
        desc = desc + "\n\nWhen an undead fails its saving throw against your Turn Undead feature, the creature is instantly destroyed if its challenge rating is at or below **" + destroyCR + "**."
    return_string = (
        f'-title "{name} {ability_name}!" '
        f'-desc "{desc}" '
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