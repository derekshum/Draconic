tembed
<drac2>
#!cc create "Blood Fury Tattoo" -max 10 -min 0 -type bubble -reset long -title "Blood Fury Tattoo" -desc "The tattoo has 10 charges, and it regains all expended charges daily at dawn. While this tattoo is on your skin, you gain the following benefits: 

#- When you hit a creature with a weapon attack, you can expend a charge to deal an extra 4d6 necrotic damage to the target, and you regain a number of hit points equal to the necrotic damage dealt. 
#- When a creature you can see damages you, you can expend a charge and use your reaction to make a melee attack against that creature, with advantage on your attack roll."
die_num = 4  #num d6
crit_text = ""
if len(&ARGS&) > 0:
    args = &ARGS&
    input = args[0].lower()
    length = len(input)
    if input == "critical"[0:length]:
        die_num = 8
        crit_text = " (CRIT!)"
cc_name = "Blood Fury Tattoo"
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
    damage = vroll(str(die_num) + "d6")
    return_string = (
        f' -title "{name} makes a Bloodthirsty Strike!" '
        f' -desc "When you hit a creature with a weapon attack, you can expend a charge to deal an extra 4d6 necrotic damage to the target, and you regain a number of hit points equal to the necrotic damage dealt." '
        f' -f "Damage{crit_text}|{str(damage)}|inline" '
        )
    former_hp = character().hp
    missing_hp = character().max_hp - former_hp
    if damage.total <= missing_hp: 
        character().modify_hp(damage.total)
        return_string += (
            f' -f "Healing|{str(former_hp)} + {str(damage.total)} = {str(character().hp)}/{str(character().max_hp)}|inline" '
            )
    elif missing_hp >= 0: 
        character().modify_hp(missing_hp)
        return_string += (
            f' -f "Healing|{str(former_hp)} + {str(missing_hp)} = {str(character().hp)}/{str(character().max_hp)}|inline" '
            f' -f "Unused healing|!hp {str(damage.total - missing_hp)}|inline" '
            )
    else: 
        return_string += (
            f' -f "Healing|{str(former_hp)} + 0 = {str(character().hp)}/{str(character().max_hp)}|inline" '
            f' -f "Unused healing|!hp {str(damage.total)}|inline" '
            )    
cc_current = cc_str(cc_name)
return_string += (
    f' -f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    f' -footer "{ctx.prefix}{ctx.alias}[?crit]" '
    )
return return_string
</drac2>