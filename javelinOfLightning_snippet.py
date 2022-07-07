!snippet jol tembed
<drac2>
weapon_type = "Javelin"
cc_name = weapon_type + "s of Lightning"
cc_value = character().get_cc(cc_name)
if cc_value >= 1:
    character().mod_cc(cc_name, -1)
    bolt = vroll("4d6")
    return_string = (f' -d "4d6[lightning]"'
        f' -f "{weapon_type} of Lightning|When you hurl this weapon and speak its command word, it transforms into a bolt of lightning, forming a line 5 feet wide that extends out from you to a target within 120 feet. Each creature in the line excluding you and the target must make a DC 13 Dexterity saving throw, taking {str(bolt)} lightning damage on a failed save, and half as much ({str(int(bolt.total/2))}) damage on a successful one.\n\n**{cc_name} remaining:** {character().cc_str(cc_name)}"'
        )
else:
    return_string = (f' -f "No more uses of {weapon_type}s of Lightning|This weapon\'s property can\'t be used again until the next dawn.\n\n**{weapon_type}s of Lightning remaining:** {character().cc_str(cc_name)}"')
return return_string
</drac2>