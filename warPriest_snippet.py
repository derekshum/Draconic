!snippet wp tembed
<drac2>
cn = "War Priest"
cv = character().get_cc(cn)
cu = 0
rs = ""
if cv >= 1:
    cu = 1
    character().mod_cc(cn, -cu)
else:
    rs = f' -f "No more uses of War Priest|One of these attacks didn\'t happen." '
cc = character().cc_str(cn)
rs += f' -f "{cn} (-{cu})| {cc}|inline" '
return rs
</drac2>