!snippet fob tembed
<drac2>
cc_name = "Ki Points"
cc_value = character().get_cc(cc_name)
if cc_value >= 1:
    character().mod_cc(cc_name, -1)
    return_string = (f' -rr {2}'
        f' -f "Flurry of Blows|Immediately after you take the Attack action on your turn, you can spend 1 ki point to make two unarmed strikes as a bonus action.\n\n**{cc_name} (-1)** {character().cc_str(cc_name)}"'
        )
else:
    return_string = (f' -f "Not enough {cc_name} for Flurry of Blows: **{cc_name}** {character().cc_str(cc_name)}"')
return return_string
</drac2>
    
    