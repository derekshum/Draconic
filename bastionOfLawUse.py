!alias bolu tembed
<drac2>
an = "Bastion of Law"
lvl = character().get_cc(an)
a = &ARGS&
for i in a:
    if i.isnumeric():
        lvl = int(i)
au = 0
rs = ""
if character().get_cc(an) >= lvl:
    au = lvl
    character().mod_cc(an, -au)
    rs += f'-title "{name} uses {au} {an} d8\'s!" '
    rs += f'-desc "The ward lasts until you finish a long rest or until you use this feature again. The ward is represented by a number of d8s equal to the number of sorcery points spent to create it. When the warded creature takes damage, it can expend a number of those dice, roll them, and reduce the damage taken by the total rolled on those dice." '
    rs += f'-f "Damage Reduction|{str(vroll(str(lvl)+"d8"))}|inline" '
else:
    rs += (
        f' -title "{name} fails to use {an}!" '
        f' -desc "Fewer than {lvl} {an} left, take a long rest." '
        )
cc_use_string = "(-" + au + ")"
rs += f'-f "{an} {cc_use_string}|{character().cc_str(an)}|inline" '
rs += f'-footer "{ctx.prefix}{ctx.alias}"'
return rs
</drac2>