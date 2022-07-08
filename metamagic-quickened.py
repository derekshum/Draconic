!alias quickened tembed
<drac2>
an = "Quickened Spell"
cn1 = "Metamagic Points"
cn2 = "Sorcery Points"
cv1 = 0
if character().cc_exists(cn1):
    cv1 = character().get_cc(cn1)
cv2 = 0
if character().cc_exists(cn2):
    cv2 = character().get_cc(cn2)
cu1 = 0
cu2 = 0
if cv1 + cv2 >= 2:
    if cv1 >= 2:
        cu1 = 2
        character().mod_cc(cn1, -cu1)
    elif cv1 < 2 and cv1 > 0:
        cu1 = cv1
        cu2 = 2 - cv1
        character().mod_cc(cn1, -cu1)
        character().mod_cc(cn2, -cu2)
    else:
        cu2 = 2
        character().mod_cc(cn2, -cu2)
    rs = (
        f'-title "{name} uses {an}!" '
        f'-desc "When you cast a spell that has a casting time of 1 action, you can spend 2 sorcery points to change the casting time to 1 bonus action for this casting." '
        )
else:
    rs = (
        f' -title "{name} fails to use {an}!" '
        f' -desc "Fewer than 2 {cn1} or {cn2} left, take a long rest." '
        )
if character().cc_exists(cn1):
    cc_use_string_1 = ""
    if cu1 > 0:
        cc_use_string_1 = " (-" + cu1 + ")"
    rs += (f'-f "{cn1} {cc_use_string_1}| {character().cc_str(cn1)}|inline" ')
if character().cc_exists(cn2):
    cc_use_string_2 = ""
    if cu2 > 0:
        cc_use_string_2 = " (-" + cu2 + ")"
    rs += (f'-f "{cn2} {cc_use_string_2}| {character().cc_str(cn2)}|inline" ')
rs += (f'-footer "{ctx.prefix}{ctx.alias}"')
return rs
</drac2>