tembed
<drac2>
damage_notes = ""
cc_request = 1
isCrit = False
isResistant = False
isVulnerable = False
for input in &ARGS&:
    input = input.lower()
    length = len(input)
    if input == "critical"[0:length]:
        isCrit = True
    elif input.isnumeric():
        cc_request = int(input)
    elif input == "resistant"[0:length] or input == "resistance"[0:length]:
        isResistant = True
    elif input == "vulnerable"[0:length] or input == "vulnerability"[0:length]:
        isVulnerable = True
cc_name = "Blood Fury Tattoo"
cc_value = character().get_cc(cc_name)
return_string = ""
if cc_value < cc_request:
    cc_use = 0
    return_string = (
        f' -title "{name} fails to use of their {cc_name}!" '
        f' -desc "Your {cc_name} does not have {str(cc_request)} remaining charges." '
        )
else:
    die_num = 4  #num d6
    if isCrit:
        die_num = 8
    cc_use = cc_request
    character().mod_cc(cc_name, -cc_use)
    roll_string = str(die_num) + "d6"
    if isResistant:
        roll_string += "/2"
    if isVulnerable:
        roll_string += "*2"
    damage = vroll(roll_string)
    if cc_use == 1:
        num_text_1 = "a"
        num_text_2 = ""
        return_string += f'-f "Damage{damage_notes}|{str(damage)}|inline" '
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
    else:
        num_text_1 = str(cc_use)
        num_text_2 = "s"  
        for i in range(cc_use - 1):
            #TODO: display both Healing and Unused Healing titles
            #TODO: keep track of totals and display at bottom
    return_string += (
        f'-title "{name} makes {num_text_1} Bloodthirsty Strike{num_text_2}!" '
        f'-desc "When you hit a creature with a weapon attack, you can expend a charge to deal an extra 4d6 necrotic damage to the target, and you regain a number of hit points equal to the necrotic damage dealt." '
        )        
    
cc_current = cc_str(cc_name)
return_string += (
    f' -f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    f' -footer "{ctx.prefix}{ctx.alias} [crit(n)] [charges(1)] [?res/vuln]" '
    )
return return_string
</drac2>