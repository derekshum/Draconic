!alias valor tembed
<drac2>
a = "Pendant of Valor"
b = character().get_cc(a)
c = "Superiority Dice"
d = character().get_cc(c)
e = character().get_cc_max(c)
return_string = ""
if b < 1:
    h = 0
    cc_recharge_change = 0
    return_string = (
        f' -title "{name} fails to use their {a}!" '
        f' -desc "Your {a} has no remaining charges." '
        )
else:
    h = 1
    character().mod_cc(a, -h)  
    i = vroll("1d10 + " + str(FighterLevel))
    return_string = (
        f' -title "{name} uses their {a}!" '
        f' -desc "While you wear this pendant, you can use your Second Wind feature without expending the feature\'s use. When you do so, if you have any spent superiority dice, you can regain one. Once this property is used, it can\'t be used again until the next dawn." '
        f' -f "Second Wind|{str(i)}|inline" '
        )
    #heal
    j = character().hp
    k = character().max_hp - j
    if i.total <= k: 
        character().modify_hp(i.total)
        return_string += (
            f' -f "Healing|{str(j)} + {str(i.total)} = {str(character().hp)}/{str(character().max_hp)}|inline" '
            )
    elif k >= 0: 
        character().modify_hp(k)
        return_string += (
            f' -f "Healing|{str(j)} + {str(k)} = {str(character().hp)}/{str(character().max_hp)}|inline" '
            f' -f "Unused Healing|!hp {str(i.total - k)}|inline" '
            )
    else: 
        return_string += (
            f' -f "Healing|{str(j)} + 0 = {str(character().hp)}/{str(character().max_hp)}|inline" '
            f' -f "Unused Healing|!hp {str(i.total)}|inline" '
            )
    #recharge superiority die
    g = 0
    if d < e:
        g = 1
        character().mod_cc(c, g)
    return_string += (    
        f' -f "{c} (+{g})| {character().cc_str(c)}|inline" '
        )
return_string += (
    f' -f "{a} (-{h})| {character().cc_str(a)}|inline" '
    f' -footer "{ctx.prefix}{ctx.alias}" '
    )
return return_string
</drac2>