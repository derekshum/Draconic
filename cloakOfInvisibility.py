!alias coi tembed
<drac2>
input = 1
if len(&ARGS&) > 0:
    args = &ARGS&
    input = int(args[0].lower())
ability_name = "their Cloak of Invisibility"
cc_name = "Cloak of Invisibility"
cc_value = character().get_cc(cc_name)
plural = ""
if input > 1:
    plural = "s"
return_string = ""
if cc_value >= input:
    cc_use = input
    character().mod_cc(cc_name, -cc_use)
    return_string = (
        f'-title "{name} wears {ability_name} for {cc_use} minute{plural}" '
        f'-desc "While wearing this cloak, you can pull its hood over your head to cause yourself to become invisible. While you are invisible, anything you are carrying or wearing is invisible with you. You become visible when you cease wearing the hood. Pulling the hood up or down requires an action.\n\nDeduct the time you are invisible, in increments of 1 minute, from the cloak\'s maximum duration of 2 hours. After 2 hours of use, the cloak ceases to function. For every uninterrupted period of 12 hours the cloak goes unused, it regains 1 hour of duration." '
        )
else:
    cc_use = 0
    return_string = (
        f' -title "{name} cannot wear {ability_name} for {cc_use} minute{plural}!" '
        f' -desc "" '
        )
cc_current = character().cc_str(cc_name)
return_string += (
    f'-f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    f'-footer "{ctx.prefix}{ctx.alias} [minutes (optional, 1)]" '
    )
return return_string
</drac2>