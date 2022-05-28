!snippet pg tembed
<drac2>
cn = "Perfected Guardian"
cv = character().get_cc(cn)
cu = 0
rs = ""
if cv >= 1:
    cu = 1
    character().mod_cc(cn, -cu)
    rs = f' -phrase "Make a **DC {int(character().spellbook.dc)} Strength saving throw!**" '
    rs += f' -f "Perfected Guardian|When a Huge or smaller creature you can see ends its turn within 30 feet of you, you can use your reaction to magically force the creature to make a **DC {int(character().spellbook.dc)} Strength saving throw**, pulling the creature up to 30 feet toward you to an unoccupied space. If you pull the target to a space within 5 feet of you, you can make a melee weapon attack against it as part of this reaction." '
else:
    rs = f' -phrase "IGNORE THIS, NO USES LEFT" -f "No more uses of {cn}|Ignore this whole thing." '
cc = character().cc_str(cn)
rs += f' -f "{cn} (-{cu})| {cc}|inline" '
return rs
</drac2>