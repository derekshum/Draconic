!alias empty tembed
<drac2>
input = "i"
if len(&ARGS&) > 0:
    args = &ARGS&
    input = args[0].lower()
    length = len(input)
    if input == "astral projection"[0:length]:
        input = "a"
cc_name = "Ki Points"
cc_value = character().get_cc(cc_name)
return_string = ""
if input == "a" and cc_value >= 8:
    cc_use = 8
    character().mod_cc(cc_name, -cc_use)
    return_string = (
        f'-title "{name} uses Empty Body - Astral Projection!" '
        f'-desc "You can spend 8 ki points to cast the astral projection spell, without needing material components. When you do so, you can\'t take any other creatures with you." '
        )
elif cc_value >= 4:
    cc_use = 4
    character().mod_cc(cc_name, -cc_use)
    return_string = (
        f'-title "{name} uses Empty Body - Invisibility!" '
        f'-desc "You can use your action to spend 4 ki points to become invisible for 1 minute. During that time, you also have resistance to all damage but force damage." '
        )
else:
    cc_use = 0
    return_string = (
        f' -title "{name} fails to use {ability_name}!" '
        f' -desc "You must complete a short or long rest to regain your expended ki points." '
        )
cc_current = cc_str(cc_name)
return_string += (
    f'-f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    f'-footer "{ctx.prefix}{ctx.alias} [astral or invis, (invis)]" '
    )
return return_string
</drac2>