!alias s tembed
<drac2>
sneak = False
sneakCrit = False
s = []  #level of smites requested as int
c = []  #whether each smite entry is a crit as bool
allCrit = False
crit_text = ""
isFiend = False
isUndead = False
isResistant = False     #will apply to all sneak and smite
isVulnerable = False    #will apply to all sneak and smite
for input in &ARGS&:
    input = input.lower()
    length = len(input)
    if input[0].isdigit() or input[len(input) - 1].isdigit() or input[0] == 's' or input[len(input) - 1] == 's':    
        if '0' in input or 's' in input:
            sneak = True
            if 'c' in input:
                sneakCrit = True
        else:
            for j, i in enumerate(input):
                if i.isdigit(): #0's should be handled above
                    s.append(int(i))
                    if 'c' in input:
                        c.append(True)
                    else:
                        c.append(False)
                    break
    elif input == "critical"[0:length]:
        allCrit = True
        crit_text = " (CRIT!)"
    elif input == "fiend"[0:length]:
        isFiend = True
    elif input == "undead"[0:length]:
        isUndead = True
    elif input == "resistant"[0:length] or input == "resistance"[0:length]:
        isResistant = True
    elif input == "vulnerable"[0:length] or input == "vulnerability"[0:length]:
        isVulnerable = True
return_string = ""

if len(s) == 0:
    sneak = True    #defaults to sneak attack if no smite levels entered
else:   #check if adequate spell slots and resistance issue
    #TODO
    
    if len(s) > 1 and isResistant:     #check if isResistance issue
        return_string += f' -f "Calculation Uncertainty|Multiple resisted smites may have a lower total than displayed due to rounding down odds." '

#TODO
        
#TODO: display spell slot levels modified
return_string += f' -footer "{ctx.prefix}{ctx.alias} [crit(n)] [charges(1)] [?res/vuln]" '
return return_string
</drac2>



