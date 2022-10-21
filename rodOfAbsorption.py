!alias roa tembed
<drac2>
cc_request = 0
for input in &ARGS&:
   input = input.lower()
   length = len(input)
   if input.isnumeric():
       cc_request = int(input)
ability_name = "their Rod of Absorption"
cc_name_1 = "RoA Energy Absorbed"   
cc_max_1 = 50 
cc_name_2 = "RoA Energy Available"
cc_value_1 = character().get_cc(cc_name_1)
return_string = ""
if cc_value_1 + cc_request <= cc_max_1:
    cc_add = cc_request
    character().mod_cc(cc_name_1, cc_add)
    character().mod_cc(cc_name_2, cc_add)
    return_string = (
        f' -title "{name} uses {ability_name} to absorb {cc_add} charges!" '
        f' -desc "While holding this rod, you can use your reaction to absorb a spell that is targeting only you and not with an area of effect. The absorbed spell\'s effect is canceled, and the spell\'s energy -- not the spell itself -- is stored in the rod. The energy has the same level as the spell when it was cast. The rod can absorb and store up to 50 levels of energy over the course of its existence" '
        )
else:
    cc_add = 0
    return_string = (
        f' -title "{name} fails to use {ability_name}!" '
        f' -desc "Too much {cc_name_1}." '
        )
cc_current_1 = character().cc_str(cc_name_1)
cc_current_2 = character().cc_str(cc_name_2)
return_string += (
    f' -f "{cc_name_1} (+{cc_add})| {cc_current_1}|inline" '
    f' -f "{cc_name_2} (+{cc_add})| {cc_current_2}|inline" '
    f' -footer "{ctx.prefix}{ctx.alias} [charges absorbed]" '
    )
return return_string
</drac2>