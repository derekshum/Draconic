tembed
<drac2>
sneak = False
sneak_crit = False
s = []  #level of smites requested as int
c = []  #whether each smite entry is a crit as bool
all_crit = False
crit_text = ""
is_fiend = False
is_undead = False
is_resistant = False     #will apply to all sneak and smite
is_vulnerable = False    #will apply to all sneak and smite
for input in &ARGS&:
    input = input.lower()
    length = len(input)
    if input[0].isdigit() or input[0] == 's':    
        if '0' in input or input[0] == 's':
            sneak = True
            if 'c' in input:
                sneak_crit = True
        else:
            s.append(int(input[0]))
            if 'c' in input:
                c.append(True)
            else:
                c.append(False)
    elif input == "critical"[0:length]:
        all_crit = True
        crit_text = " (CRIT!)"
    elif input == "fiend"[0:length]:
        is_fiend = True
    elif input == "undead"[0:length]:
        is_undead = True
    elif input == "resistant"[0:length] or input == "resistance"[0:length]:
        is_resistant = True
    elif input == "vulnerable"[0:length] or input == "vulnerability"[0:length]:
        is_vulnerable = True
return_string = ""
spell_levels = []
slots_used = []
if len(s) == 0:
    sneak = True    #defaults to sneak attack if no smite levels entered
else:   #check if adequate spell slots and resistance issue   
    s2 = [i for i in s]
    s2.sort()
    current_level = s[0]
    current_level_count = 1
    for i in range(1, len(s2) + 1):
        if i == len(s2) or s2[i] != current_level:
            if character().spellbook.get_slots(current_level) < current_level_count:
                return_string = (
                    f' -title "{name} doesn\'t have enough level {current_level} spell slots remaining!" '
                    f' -desc "Spell Slots (-0)| {character().spellbook.slots_str(current_level)}"'
                    )
                return return_string
            spell_levels.append(current_level)
            slots_used.append(current_level_count)
            if i < len(s2):
                current_level = s2[i]
                current_level_count = 1
        else:
            current_level_count += 1
    if len(s) > 1 and is_resistant:     #check if is_resistant issue 1
        return_string += f' -f "Calculation Uncertainty|Multiple resisted smites may have a lower total than displayed due to rounding down odds." '
if is_resistant and is_vulnerable:     #check if isResistant issue 2
    return_string += f' -f "Calculation Uncertainty|Resisted and Vulnerable damage may have a lower total than displayed due to rounding down odds." '
roll_string = ""
sneak_mult = 1
if sneak_crit or all_crit:
    sneak_mult = 2
if sneak:
    roll_string += sneak_mult * int((RogueLevel + 1)/ 2) + "d6+"
extra_smite = 1
if is_fiend or is_undead:
    extra_smite = 2
for i in range(len(s)):
    smite_mult = 1
    if c[i] or all_crit:
        smite_mult = 2
    roll_string += (smite_mult * (min(4,s[i]) + extra_smite)) + "d8+" #max 5d8/6d8 vs fiends
    #TODO
roll_string = roll_string[:len(roll_string) - 1]
if is_resistant:
    roll_string = "(" + roll_string + ")/2"
if is_vulnerable:
    roll_string = "(" + roll_string + ")*2"
if sneak and len(s) > 0:
    title_text = "sneak attacks and smites"
elif sneak:
    title_text = "sneak attacks"
elif len(s) > 0:
    title_text = "smites"
else:
    title_text = "huh, that's not supposed to happen?"
return_string += (
    f' -title "{name} {title_text}!" '
    f' -f "Damage{crit_text}|{str(vroll(roll_string))}" '
    )
if len(spell_levels) > 0:
    return_string += f' -desc "**Spell Slots**'
    for i in range(len(spell_levels)):   #display spell slot levels modified
        for j in range(slots_used[i]):
            character().spellbook.use_slot(spell_levels[i])
        return_string += f'\n{character().spellbook.slots_str(spell_levels[i])} (-{slots_used[i]})'
    return_string += f'" '
return_string += f' -footer "{ctx.prefix}{ctx.alias} [?smite levels] [?res/vuln] [allCrit(n)]" '
return return_string
</drac2>