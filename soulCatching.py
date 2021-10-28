tembed
<drac2>
die_num = 2  #num d10s
crit_text = ""
isResistant = False
isVulnerable = False
noHeal = False
for input in &ARGS&:
    input = input.lower()
    length = len(input)
    if input == "critical"[0:length] or input == "allcritical"[0:length]:
        die_num = 2 * die_num
        crit_text = " (CRIT!)"
    elif input.isnumeric():
        die_num = 2 * int(input)
    elif input == "resistant"[0:length] or input == "resistance"[0:length]:
        isResistant = True
    elif input == "vulnerable"[0:length] or input == "vulnerability"[0:length]:
        isVulnerable = True
    elif input == "nohealing"[0:length] or input == "advantage"[0:length] or input == "gainadvantage"[0:length] or input == "storeadvantage"[0:length]:
        noHeal = True
return_string = ""
roll_string = str(die_num) + "d10"
if isResistant:
    roll_string += "/2"
    if (die_num > 2 and crit_text == "") or die_num > 4 :
        return_string += f' -f "Calculation Uncertainty|Multiple resisted attacks may have a lower total than displayed due to rounding down odds." '
if isVulnerable:
    roll_string += "*2"
roll_string += "[force]"
damage = vroll(roll_string)  
if noHeal:
    return_string += (
        f' -title "{name} attacks with their Gloves of Soul Catching, storing advantage!" '
        f' -desc "After making a successful unarmed strike while wearing these gloves, you can use the gloves to deal an extra 2d10 force damage to the target, and you can choose to gain advantage on one attack roll, ability check, or saving throw you make before the end of your next turn." '
        f' -f "Damage{crit_text}|{str(damage)}|inline" '
        )
else: 
    return_string += (
        f' -title "{name} attacks with their Gloves of Soul Catching, regaining health!" '
        f' -desc "After making a successful unarmed strike while wearing these gloves, you can use the gloves to deal an extra 2d10 force damage to the target, and you regain a number of hit points equal to the force damage dealt. " '
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
            f' -f "Unused Healing|!hp {str(damage.total - missing_hp)}|inline" '
            )
    else: 
        return_string += (
            f' -f "Healing|{str(former_hp)} + 0 = {str(character().hp)}/{str(character().max_hp)}|inline" '
            f' -f "Unused Healing|!hp {str(damage.total)}|inline" '
            )
return_string += (
    f' -footer "{ctx.prefix}{ctx.alias} [?strikes (crits count as 2)] [?allCrit] [?res/vuln] [?noHeal (stores adv)]" '
    )
return return_string
</drac2>