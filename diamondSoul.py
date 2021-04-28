!alias sharpen tembed
<drac2>
ability_name = "Diamond Soul" 
if len(&ARGS&) > 0:
    args = &ARGS&
    input = args[0].lower()
    length = len(input)
    if input == "strength"[0,length]:
        save = "Strength"
    elif input == "dexterity"[0,length]:
        save = "Dexterity"
    elif input == "constitution"[0,length]:
        save = "Constitution"
    elif input == "intelligence"[0,length]:
        save = "Intelligence"
    elif input == "wisdom"[0,length]:
        save = "Wisdom"
    elif input == "charisma"[0,length]:
        save = "Charisma"
    elif input == "death"[0,length] or input == "ds":
        save = "Death"
    if  
        cc_name = "Ki Points"
        cc_value = character().get_cc(cc_name)
        return_string = ""
        if cc_value >= 1:
            cc_use = 1
            character().mod_cc(cc_name, -cc_use)
            #TODO
            return_string = (
                f'-title "{name} uses {ability_name}!" '
                f'-desc "Your mastery of ki grants you proficiency in all saving throws.\n\nAdditionally, whenever you make a saving throw and fail, you can spend 1 ki point to reroll it and take the second result." '
                f'-f "New {save} Save | " ' #TODO
                )
        else:
            cc_use = 0
            return_string = (
                f' -title "{name} fails to use {ability_name}!" '
                f' -desc "Not enough {cc_name}." '
                )
    else:
        cc_use = 0
        return_string = (
            f' -title "{name} fails to use {ability_name}!" '
            f' -desc "Input {str(input)} is not a recognized save." '   #could state allowed saves
            )    
else:
    cc_use = 0
    return_string = (
        f' -title "{name} fails to use {ability_name}!" '
        f' -desc "Input {str(input)} is not a recognized save." '   #could state allowed saves
        )
cc_current = cc_str(cc_name)
return_string += (
        f'-f "{cc_name} (-{cc_use})| {cc_current}|inline" '
        f'-footer "{ctx.prefix}{ctx.alias} [save]"'
        )
return return_string
</drac2>