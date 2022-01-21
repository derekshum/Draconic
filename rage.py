!alias rage tembed
<drac2>
cc_request = 1
ability_name = "their rage"
cc_name = "Rage"
cc_value = character().get_cc(cc_name)
return_string = ""
if cc_value >= cc_request:
    cc_use = cc_request
    character().mod_cc(cc_name, -cc_use)
    if BarbarianLevel < 9:
        D = 2
    elif BarbarianLevel < 16:
        D = 3
    else:
        D = 4
    return_string = (
        f' -title "{name} uses {ability_name}!" '
        f' -desc "On your turn, you can enter a rage as a bonus action. While raging, you gain several benefits if you aren\'t wearing heavy armor.\n• You have advantage on Strength checks and Strength saving throws.\n• When you make a melee weapon attack using Strength, you deal an additional {D} damage.\n• You have resistance to bludgeoning, piercing, and slashing damage.\n\nIf you are able to cast spells, you can\'t cast them or concentrate on them while raging.\n\nYour rage lasts for 1 minute. It ends early if you are knocked unconscious or if your turn ends and you haven\'t attacked a hostile creature since your last turn or taken damage since then. You can also end your rage on your turn as a bonus action." '
        f' -f "Ancestral Protectors|While you’re raging, the first creature you hit with an attack on your turn becomes the target of the warriors, which hinder its attacks. Until the start of your next turn, that target has disadvantage on any attack roll that isn\'t against you, and when the target hits a creature other than you with an attack, that creature has resistance to the damage of the target’s attacks." ' #ancestral specific
        )
else:
    cc_use = 0
    return_string = (
        f' -title "{name} fails to use {ability_name}!" '
        f' -desc "No {cc_name}s remaining." '
        )
cc_current = cc_str(cc_name)
return_string += (
    f' -f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    f' -footer "{ctx.prefix}{ctx.alias}" '
    )
return return_string
</drac2>

