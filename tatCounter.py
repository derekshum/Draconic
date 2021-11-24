!alias swc tembed
<drac2>
bonus = 0
adv = False
dis = False
for input in &ARGS&:
    input = input.lower()
    length = len(input)
    if input[0].isdigit():
        bonus = input
    elif input == "advantage"[0:length]:
        adv = True
    elif input == "disadvantage"[0:length]:
        dis = True  
        
ability_name = "their Counterspell Spellwrought Tattoo"
cc_name = "Counterspell Spellwrought Tattoo"
cc_value = character().get_cc(cc_name)
return_string = ""
if cc_value > 0:
    cc_use = 1
    character().mod_cc(cc_name, -cc_use)
    return_string = f' -title "{name} invokes {ability_name}!"'
    if adv:
        roll_string = "2d20kh1+4"
    elif dis:
        roll_string = "2d20kl1+4"
    else:
        roll_string = "d20+4"
    if bonus != 0: 
        roll_string = roll_string + "+" + bonus
    spell_check = vroll(roll_string)
    return_string += f' -f "Spellcasting Check|{spell_check}|inline"'
else:
    cc_use = 0
    return_string = (
        f' -title "{name} fails to use {ability_name}!"'
        f' -desc "No tattoo available."'
        )
cc_current = cc_str(cc_name)
return_string += f' -f "{cc_name} (-{cc_use})| {cc_current}|inline"'
return_string += f' -footer "{ctx.prefix}{ctx.alias} [other check bonus (optional)]"'     
return return_string
</drac2>