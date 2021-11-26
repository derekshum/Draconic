!alias ssi tembed
<drac2>
cc_request = 1
for input in &ARGS&:
    input = input.lower()
    length = len(input)
    if input.isnumeric():
        cc_request = int(input)
cc_name = "Spell-Storing Item"
cc_value = character().get_cc(cc_name)

if cc_value >= cc_request:
    cc_use = cc_request
    character().mod_cc(cc_name, -cc_use)
    if cc_request > 1:
        return_string = f' -title "{name}\'s {cc_name} is used {cc_request} times!" '
    else:
        return_string = f' -title "{name}\'s {cc_name} is used!" '
    return_string += (        
        f' -desc "While holding the object, a creature can take an action to produce the spell\'s effect from it, using your spellcasting ability modifier." '
        )
else:
    cc_use = 0
    return_string = (
        f' -title "Not enough uses remaining in {name}\'s {cc_name}!" '
        f' -desc "Re-store at the end of a long rest." '
        )
cc_current = cc_str(cc_name)
return_string += (
    f' -f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    f' -footer "{ctx.prefix}{ctx.alias} [uses]" '
    )
return return_string
</drac2>