!snippet ol tembed
<drac2>
cc_name = "Obviator's Lenses"
cc_value = character().get_cc(cc_name)
if cc_value >= 1:
    character().mod_cc(cc_name, -1)
    return_string = (
        f' adv1 ea1 -d1 "1d10" -f "{cc_name}|You can focus the power of the lenses to gain accuracy in combat, gaining advantage on a weapon attack roll (no action required). If that attack hits, roll one additional weapon damage die.\n**{cc_name}:** {cc_str(cc_name)}"'
        )
else:
    return_string = (
        f' -f "{cc_name} has already been used|This property of the lenses can\'t be used again until the next dawn.\n**{cc_name}:** {cc_str(cc_name)}"')
return return_string
</drac2>