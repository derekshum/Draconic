!snippet net tembed
<drac2>
return_string = ""
cc_name = "Nets"
cc_value = character().get_cc(cc_name)
if cc_value >= 1:
    cc_use = 1
    character().mod_cc(cc_name, -cc_use)
else:
    cc_use = 0
    return_string = f' -f "No {cc_name}|CC {cc_name} is currently at 0."'
cc_current = character().cc_str(cc_name)
return_string += f' -f "{cc_name} (-{cc_use})| {cc_current}|inline"'
return return_string
</drac2>

#return_string = f' -f "Net|A Large or smaller creature hit by a net is restrained until it is freed. A net has no effect on creatures that are formless, or creatures that are Huge or larger. A creature can use its action to make a DC 10 Strength check, freeing itself or another creature within its reach on a success. Dealing 5 slashing damage to the net (AC 10) also frees the creature without harming it, ending the effect and destroying the net.\n\nWhen you use an action, bonus action, or reaction to attack with a net, you can make only one attack regardless of the number of attacks you can normally make." '