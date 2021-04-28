!snippet jol tembed
<drac2>
cc_name = "Javelins of Lightning"
cc_value = character().get_cc(cc_name)
if cc_value >= 1:
    character().mod_cc(cc_name, -1)
    set("bolt", vroll("4d6"))
    return_string = (f' -d "4d6[lightning]"'
        f' -f "Javelin of Lightning|This javelin is a magic weapon. When you hurl it and speak its command word, it transforms into a bolt of lightning, forming a line 5 feet wide that extends out from you to a target within 120 feet. Each creature in the line excluding you and the target must make a DC 13 Dexterity saving throw, taking {str(bolt)} lightning damage on a failed save, and half as much ({str(int(bolt.total/2))}) damage on a successful one.\n\n**{cc_name} remaining:** {cc_str(cc_name)}"'
        )
else:
    return_string = (f' -f "No more uses of Javelins of Lightning|The javelin\'s property can\'t be used again until the next dawn. In the meantime, the javelin can still be used as a magic weapon.\n\n**Javelins of Lightning remaining:** {cc_str(cc_name)}"')
return return_string
</drac2>