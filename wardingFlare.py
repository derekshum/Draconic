!alias warding tembed
<drac2>
cc_name = "Warding Flare"
cc_value = character().get_cc(cc_name)
return_string = ""
if cc_value < 1:
    cc_use = 0
    cc_recharge_change = 0
    return_string = (
        f' -title "{name} fails to use their {cc_name}!" '
        f' -desc "Your {cc_name} has no remaining charges." '
        )
else:
    cc_use = 1
    cc_recharge_change = 1
    character().mod_cc(cc_name, -cc_use)
    return_string = (
        f' -title "EMBRACE THE MIGHTY POWER OF LAMP. :D" '
        f' -desc "**Warding Flare**\n\nYou can interpose divine light between yourself and an attacking enemy.\n\nWhen you are attacked by a creature within 30 feet of you that you can see, you can use your reaction to impose disadvantage on the attack roll, causing light to flare before the attacker before it hits or misses.\n\nAn attacker that can''t be blinded is immune to this feature." '
        f' -image https://cdn.discordapp.com/attachments/714291596102860851/846227679779094528/2b5d08367f6cb1dcb5bacf95aba29381.gif -color <color> -thumb <image> '
        )
cc_current = character().cc_str(cc_name)
return_string += (
    f' -f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    f' -footer "{ctx.prefix}{ctx.alias}" '
    )
return return_string
</drac2>