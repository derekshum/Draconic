!alias twinned tembed
<drac2>
input = 1
if len(&ARGS&) > 0:
    args = &ARGS&
    input = int(args[0].lower())
ability_name = "Twinned Spell"
cc_name = "Sorcery Points"
cc_value = character().get_cc(cc_name)
return_string = ""
if cc_value >= input:
    cc_use = input
    character().mod_cc(cc_name, -cc_use)
    return_string = (
        f'-title "{name} uses {ability_name}!" '
        f'-desc "When you cast a spell that targets only one creature and doesn\'t have a range of self, you can spend a number of sorcery points equal to the spell\'s level to target a second creature in range with the same spell (1 sorcery point if the spell is a cantrip).\n\nTo be eligible, a spell must be incapable of targeting more than one creature at the spell\'s current level. For example, magic missile and scorching ray aren\'t eligible, but ray of frost and chromatic orb are." '
        )
else:
    cc_use = 0
    return_string = (
        f' -title "{name} fails to use {ability_name}!" '
        f' -desc "Fewer than {input} {cc_name} left, take a long rest." '
        )
cc_current = cc_str(cc_name)
return_string += (
    f'-f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    f'-footer "{ctx.prefix}{ctx.alias} [spell level (optional, !defaults to 1)]"'
    )
return return_string
</drac2>