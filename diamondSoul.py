tembed
<drac2>
ability_name = "Diamond Soul" 
cc_name = "Ki Points"
cc_value = character().get_cc(cc_name)
return_string = ""
if len(&ARGS&) == 0:
    cc_use = 0
    return_string = (
        f' -title "{name} fails to use {ability_name}!" '
        f' -desc "Input required to speciy save type." '   #could state allowed saves
        )
else:
    error = False
    args = &ARGS&
    input = args[0].lower()
    length = len(input)
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
        modifier = strengthSave - strengthMod   #best guess for capturing proficiency and items effects
    else:
        error = True   #indicates invalid save specified
    
    if error:
        cc_use = 0
        return_string = (
            f' -title "{name} fails to use {ability_name}!" '
            f' -desc "Input {str(input)} is not a recognized save." '   #could state allowed saves
            )
    else:
        if cc_value < 1:
            cc_use = 0
            return_string = (
                f' -title "{name} fails to use {ability_name}!" '
                f' -desc "Not enough {cc_name}." '
                )
        else: 
            vantage = "1d20"
            bonus = "0"
            death_fails_removed = 1 #number of death fails to remove on a successful death save, 1 if regular death fail, 2 if crit death fail
            if len(args) > 1:
                input = args[1].lower()
                length = len(input)
                if input == "advantage"[0:length]:
                    vantage =  "2d20kh1"
                elif input == "disadvantage"[0:length]:
                    vantage = "2d20kl1"
                #otherwise flat roll
                if len(args) > 2:
                    bonus = args[2].lower()
                    return_string += (f' -f "{input}" ') #TODO: test and remove
                    if len(args) > 3:
                        input = args[3].lower()
                        length = len(input)
                        if input == "yes"[0:length] or input == "fail"[0:length] or input == "critfail"[0:length]:
                            death_fails_removed = 2
                        return_string += (f' -f "{input}" ') #TODO: test and remove
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
                    f' -f "Death Saves Successes ({success_change}): {str(character().death_saves.successes)}/3\nFailures ({failure_change}): {str(character().death_saves.fails)}/3" '
                    )
            
cc_current = cc_str(cc_name)
return_string += (
        f' -f "{cc_name} (-{cc_use})| {cc_current}|inline" '
        f' -footer "{ctx.prefix}{ctx.alias} [save] [adv/dis (optional)] [bonus (optional)]" '
        )
return return_string
</drac2>