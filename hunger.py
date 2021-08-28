#!cc create "Hunger" -max 8 -min 0 -type bubble -reset long -title "Hunger" -desc "This weapon has 8 charges. When you hit a creature with this weapon, you can expend 1 charge to deal an extra 2d4 damage to the target and gain a number of temporary hit points equal to the extra damage dealt. Additionally, if the attack kills the the target creature, you regain hit points equal to the extra damage dealt. This weapon regains all charges daily at midnight."

!alias hunger tembed
<drac2>
die_num = 2  #num d4
crit_text = ""
if len(&ARGS&) > 0:
    args = &ARGS&
    input = args[0].lower()
    length = len(input)
    if input == "critical"[0:length]:
        die_num = 2 * die_num
        crit_text = " (CRIT!)"
        if len(&ARGS&) > 1:
            input = args[1].lower()
            cc_request = int(input)
            die_num = cc_request * die_num
cc_name = "Hunger"
cc_value = character().get_cc(cc_name)
return_string = ""
if cc_value < 1:
    cc_use = 0
    return_string = (
        f' -title "{name} fails to use a charge of {cc_name}!" '
        f' -desc "{cc_name} does not have {str(cc_request)} remaining charges." '
        )
else:
    cc_use = 1
    character().mod_cc(cc_name, -cc_use)
    damage = vroll(str(die_num) + "d4")
    if damage.total > character().temp_hp:
        character().set_temp_hp(damage.total)
    return_string += (
        f' -title "{name}\'s {cc_name} grows stronger!" '
        f' -desc "When you hit a creature with this weapon, you can expend 1 charge to deal an extra 2d4 damage to the target and gain a number of temporary hit points equal to the extra damage dealt. Additionally, if the attack kills the the target creature, you regain hit points equal to the extra damage dealt. This weapon regains all charges daily at midnight." '
        f' -f "Damage{crit_text}|{str(damage)}|inline" '
        f' -f "Kill Heal|!hp {damage.total}|inline" '
        f' -f "Current HP|{character().hp_str()}|inline" '
        )
cc_current = cc_str(cc_name)
return_string += (
    f' -f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    f' -footer "{ctx.prefix}{ctx.alias} [?crit(n)]" '
    )
return return_string
</drac2>