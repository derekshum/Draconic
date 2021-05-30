!alias bf tembed
<drac2>
#!cc create "Blood Fury Tattoo" -max 10 -min 0 -type bubble -reset long -title "Blood Fury Tattoo" -desc "The tattoo has 10 charges, and it regains all expended charges daily at dawn. While this tattoo is on your skin, you gain the following benefits: 

#- When you hit a creature with a weapon attack, you can expend a charge to deal an extra 4d6 necrotic damage to the target, and you regain a number of hit points equal to the necrotic damage dealt. 
#- When a creature you can see damages you, you can expend a charge and use your reaction to make a melee attack against that creature, with advantage on your attack roll."

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
    damage = vroll("4d6")
    missing_hp = character().max_hp - character().hp
    if damage.total >= missing_hp: 
        healing = damage
        unused_healing = 0
    else: 
        healing = missing_hp
        unused_healing = damage = missing_hp
    return_string = (
        f' -title "{name} makes a Bloodthirsty Strike!" '
        f' -desc "When you hit a creature with a weapon attack, you can expend a charge to deal an extra 4d6 necrotic damage to the target, and you regain a number of hit points equal to the necrotic damage dealt." '
        f' -f "Damage|{str(damage)}|inline" '    #TODO f' -f "Damage{crit_text}|{str(damage)}|inline" '
        )
cc_current = cc_str(cc_name)
return_string += (
    f' -f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    f' -footer "{ctx.prefix}{ctx.alias}" '  #TODO add crits
    )
return return_string
</drac2>