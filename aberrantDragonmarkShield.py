!cc create "Aberrant Dragonmark: Shield" -max 1 -min 0 -type bubble -reset short -title "Aberrant Dragonmark: Shield" -desc "Once you cast [this spell], you must finish a short or long rest before you can cast it again through the mark. Constitution is your spellcasting ability for these spells.

When you cast the 1st-level spell through your mark, you can expend one of your Hit Dice and roll it. If you roll an even number, you gain a number of temporary hit points equal to the number rolled. If you roll an odd number, one random creature within 30 feet of you (not including you) takes force damage equal to the number rolled. If no other creatures are in range, you take the damage."

### f'-desc "**Casting Time:** 1 reaction, which you take when you are hit by an attack or targeted by the magic missile spell\n**Range:** Self\n**Components:** V, S\n**Duration:** 1 round\n**Description**\nAn invisible barrier of magical force appears and protects you. Until the start of your next turn, you have a +5 bonus to AC, including against the triggering attack, and you take no damage from magic missile." '

# !alias ads 

tembed
<drac2>
HD_size = 0
other_AC_bonus = 0
other_AC_bonus_set = False
if len(&ARGS&) > 0:
    args = &ARGS&
    input = args[0].lower()
    if input == "6":
        HD_size = 6
    elif input == "8":
        HD_size = 8
    elif input == "10":
        HD_size = 10
    elif input == "12":
        HD_size = 12    
    if len(&ARGS&) > 1:
        args = &ARGS&
        input = args[1].lower()
        other_AC_bonus = int(input)
        other_AC_bonus_set = True
ability_name = "their Aberrant Dragonmark to cast Shield"
cc_name = "Aberrant Dragonmark: Shield"
cc_value = character().get_cc(cc_name)
return_string = ""
HD_name = "Hit Dice (d" + str(HD_size) + ")"
HD_use = 0
if cc_value > 0:
    cc_use = 1
    character().mod_cc(cc_name, -cc_use)
    return_string = f' -title "{name} invokes {ability_name}!"'
    if other_AC_bonus_set: 
        return_string += f' -f "New AC|{armor + other_AC_bonus} + 5 = {armor + other_AC_bonus + 5}|inline"'
    else:
        return_string += f' -f "AC Bonus|+5|inline"'  
    if HD_size != 0:
        HD = character().get_cc(HD_name)
        if HD > 0:
            HD_use = 1
            character().mod_cc(HD_name, -HD_use)
            HD_roll = vroll("1d"+str(HD_size))
            return_string += (
                f' -title "{name} invokes {ability_name}, using HD!"'
                f' -desc "When you cast the 1st-level spell through your mark, you can expend one of your Hit Dice and roll it. If you roll an even number, you gain a number of temporary hit points equal to the number rolled. If you roll an odd number, one random creature within 30 feet of you (not including you) takes force damage equal to the number rolled. If no other creatures are in range, you take the damage."'
                f' -f "HD roll|{str(HD_roll)}|inline"'
                )
            if (HD_roll.total % 2) == 0:
                if HD_roll.total > character().temp_hp: 
                    character().set_temp_hp(HD_roll.total)
                    return_string += f' -f "THP Increased|{hp_str()}|inline"'
                else:
                    return_string += f' -f "THP Unchanged|{hp_str()}|inline"'
                return_string += f' -f "Temporary Hit Points|!thp {str(HD_roll.total)}|inline"'
            else:
                return_string += f' -f "Damage|{str(HD_roll.total)}|inline"'
        else:
            return_string += f' -f "No {HD_name} Remaining|Take a long rest|inline"'
else:
    cc_use = 0
    return_string = (
        f' -title "{name} fails to use {ability_name}!"'
        f' -desc "Take a short or long rest."'
        )
cc_current = cc_str(cc_name)
return_string += f' -f "{cc_name} (-{cc_use})| {cc_current}|inline"'
if HD_size != 0:
    HD_current = cc_str(HD_name)
    return_string += f' -f "{HD_name} (-{HD_use})| {HD_current}|inline"'
return_string += f' -footer "{ctx.prefix}{ctx.alias} [HD size (if using HD ability)] [other AC bonus (optional)]"'     
return return_string
</drac2>