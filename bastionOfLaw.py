!alias bol tembed
<drac2>
lvl = 1
target = ""
a = &ARGS&
for i in a:
    if i.isnumeric():
        lvl = int(i)
    else:
        target = i
an = "Bastion of Law"
cn = "Sorcery Points"
cu = 0
rs = ""
if character().get_cc(cn) >= lvl:
    cu = lvl
    character().mod_cc(cn, -cu)
    character().set_cc(an, lvl)
    if target == "":
        rs += f'-title "{name} uses {an}!" '
    else:
        rs += f'-title "{name} uses {an} on {target}!" '
    rs += f'-desc "You can tap into the grand equation of existence to imbue a creature with a shimmering shield of order. As an action, you can expend 1 to 5 sorcery points to create a magical ward around yourself or another creature you can see within 30 feet of you.\n\nThe ward lasts until you finish a long rest or until you use this feature again. The ward is represented by a number of d8s equal to the number of sorcery points spent to create it. When the warded creature takes damage, it can expend a number of those dice, roll them, and reduce the damage taken by the total rolled on those dice." '
else:
    rs += (
        f' -title "{name} fails to use {an}!" '
        f' -desc "Fewer than {lvl} {cn} left, take a long rest." '
        )
cc_use_string = "(-" + cu + ")"
rs += f'-f "{cn} {cc_use_string}| {character().cc_str(cn)}|inline" '
rs += f'-f "{an}|{character().cc_str(an)}|inline" '
rs += f'-footer "{ctx.prefix}{ctx.alias}"'
return rs
</drac2>