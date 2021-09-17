tembed
<drac2>
ability_name = "Diamond Soul" 
cc_name = "Ki Points"    
save = ""
vantage = "1d20"
bonus = "0"
death_fails_removed = 1 #number of death fails to remove on a successful death save, 1 if regular death fail, 2 if crit death fail
for input in &ARGS&:
    input = input.lower()
    length = len(input)
    #check for save type
    if input == "strength"[0:length]:
        save = "Strength"
        modifier = strengthSave
    elif input == "dexterity"[0:length]:
        save = "Dexterity"
        modifier = dexteritySave
    elif input == "constitution"[0:length]:
        save = "Constitution"
        modifier = constitutionSave
    elif input == "intelligence"[0:length]:
        save = "Intelligence"
        modifier = intelligenceSave
    elif input == "wisdom"[0:length]:
        save = "Wisdom"
        modifier = wisdomSave
    elif input == "charisma"[0:length]: #c will default to Consitution
        save = "Charisma"
        modifier = charismaSave
    elif input == "death"[0:length] or input == "ds":   #d and de will default to Dexterity
        save = "Death"
        modifier = 0   #assumes 0 as RAW it is unclear if bonuses that aren't rerolls apply to death saves
    #check for advantage/disadvantage on the save
    elif input == "advantage"[0:length]:
        vantage =  "2d20kh1"
    elif input == "disadvantage"[0:length]:
        vantage = "2d20kl1"
    #check for save bonus
    elif input[0].isnumeric() or input[0] == "d" or input[0] == "-":
        bonus = input
    #check for death critfail removal
    elif input == "critfail"[0:length] or input == "criticalfailure"[0:length]:
        death_fails_removed = 2
cc_value = character().get_cc(cc_name)
return_string = ""
if save == "":
    cc_use = 0
    return_string = (
        f' -title "{name} fails to use {ability_name}!" '
        f' -desc "Input specifying save type required." '   #could state allowed saves
        )
elif cc_value < 1:
    cc_use = 0
    return_string = (
        f' -title "{name} fails to use {ability_name}!" '
        f' -desc "Not enough {cc_name}." '
        )
else:                             
    cc_use = 1
    character().mod_cc(cc_name, -cc_use)
    if bonus != "0":
        new_save = vroll(vantage + " + " + str(modifier) + " + " + str(bonus)) 
    else: 
        new_save = vroll(vantage + " + " + str(modifier)) 
    return_string += (
        f' -title "{name} uses {ability_name} to reroll a {save} Save!" '
        f' -desc "Your mastery of ki grants you proficiency in all saving throws.\n\nAdditionally, whenever you make a saving throw and fail, you can spend 1 ki point to reroll it and take the second result." '
        f' -f "New {save} Save | {new_save}|inline" ' 
        )
    if save == "Death":
        if new_save.result.crit == 2:
            success_change = "+0"
            failure_change = "-0"
        else:
            if new_save.result.crit == 1:
                character().death_saves.fail(-1*death_fails_removed)
                character().death_saves.succeed(2)
                success_change = "+2"
                failure_change = str(-1*death_fails_removed)
            elif new_save.total >= 10:
                character().death_saves.fail(-1*death_fails_removed)
                character().death_saves.succeed(1)
                success_change = "+1"
                failure_change = str(-1*death_fails_removed)
            elif death_fails_removed == 2:
                character().death_saves.fail(-1)
                success_change = "+0"
                failure_change = "-1"
            else:
                success_change = "+0"
                failure_change = "-0"
        return_string += (
            f' -f "Death Saves|Successes ({success_change}): {str(character().death_saves.successes)}/3\nFailures ({failure_change}): {str(character().death_saves.fails)}/3|inline" '
            )
    
cc_current = cc_str(cc_name)
return_string += (
        f' -f "{cc_name} (-{cc_use})| {cc_current}|inline" '
        f' -footer "{ctx.prefix}{ctx.alias}[save][?vantage][?bonus][?critDS]" '
        )
return return_string
</drac2>