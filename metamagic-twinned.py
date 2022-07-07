!alias twinned tembed
<drac2>
lvl = 1
if len(&ARGS&) > 0:
    args = &ARGS&
    lvl = int(args[0].lower())
an = "Twinned Spell"
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
if cv1 + cv2 >= lvl:
    if cv1 >= lvl:
        cu1 = lvl
        character().mod_cc(cn1, -cu1)
    elif cv1 < lvl and cv1 > 0:
        cu1 = cv1
        cu2 = lvl - cv1
        character().mod_cc(cn1, -cu1)
        character().mod_cc(cn2, -cu2)
    else:
        cu2 = lvl
        character().mod_cc(cn2, -cu2)
    
    rs = (
        f'-title "{name} uses {an} on a Level {lvl} Spell!" '
        f'-desc "When you cast a spell that targets only one creature and doesn\'t have a range of self, you can spend a number of sorcery points equal to the spell\'s level to target a second creature in range with the same spell (1 sorcery point if the spell is a cantrip).\n\nTo be eligible, a spell must be incapable of targeting more than one creature at the spell\'s current level. For example, magic missile and scorching ray aren\'t eligible, but ray of frost and chromatic orb are." '
        )
else:
    rs = (
        f' -title "{name} fails to use {an} on a Level {lvl} Spell!" '
        f' -desc "Fewer than {lvl} {cn1} or {cn2} left, take a long rest." '
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