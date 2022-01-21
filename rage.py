!alias rage tembed #ancestral
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

!alias rage 
tembed #beast
<drac2>
cc_request = 1
beast_form = ""
for input in &ARGS&:
    input = input.lower()
    l = len(input)
    if input == "bite"[0:l]:
        beast_form = "b"
    elif input == "claws"[0:l]:
        beast_form = "c"
    elif input == "tail"[0:l]:
        beast_form = "t"
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
        )
    if beast_form != "":     
        if beast_form == "b":
            t = "**Bite.** Your mouth transforms into a bestial muzzle or great mandibles (your choice). It deals 1d8 piercing damage on a hit. Once on each of your turns when you damage a creature with this bite, you regain a number of hit points equal to your proficiency bonus, provided you have less than half your hit points when you hit."
        elif beast_form == "c":
            t = "**Claws.** Each of your hands transforms into a claw, which you can use as a weapon if it's empty. It deals 1d6 slashing damage on a hit. Once on each of your turns when you attack with a claw using the Attack action, you can make one additional claw attack as part of the same action."
        elif beast_form == "t":
            t = "**Tail.** You grow a lashing, spiny tail, which deals 1d8 piercing damage on a hit and has the reach property. If a creature you can see within 10 feet of you hits you with an attack roll, you can use your reaction to swipe your tail and roll a d8, applying a bonus to your AC equal to the number rolled, potentially causing the attack to miss you."
        return_string += f' -f "Form of the Beast|{t}" '
else:
    cc_use = 0
    return_string = (
        f' -title "{name} fails to use {ability_name}!" '
        f' -desc "No {cc_name}s remaining." '
        )
cc_current = cc_str(cc_name)
return_string += (
    f' -f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    f' -footer "{ctx.prefix}{ctx.alias} [beast form]" '
    )
return return_string
</drac2>

