!snippet bfr tembed
<drac2>
return_string = ""
cc_name = "Blood Fury Tattoo"
cc_value = character().get_cc(cc_name)
if cc_value >= 1:
    cc_use = 1
    character().mod_cc(cc_name, -cc_use)
    return_string += (
        f' adv'
        f' -title "{name} retaliates from their Blood Fury Tattoo!"'
        f' -f "Bloodthirsty Strikes|When a creature you can see damages you, you can expend a charge and use your reaction to make a melee attack against that creature, with advantage on your attack roll."'
        )   
else:
    cc_use = 0
    return_string += (f' -title "No more Blood Fury charges, this attack didn\'t happen"')
cc_current = character().cc_str(cc_name)
return_string += (f' -f "{cc_name} (-{cc_use})| {cc_current}|inline"')
return return_string
</drac2>