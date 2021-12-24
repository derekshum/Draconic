!alias hero tembed
<drac2>
ability_name = "a Potion of Heroism"
cc_name = "Potions of Heroism"
cc_value = character().get_cc(cc_name)
return_string = ""
cc_request = 1
if cc_value >= cc_request:
    cc_use = cc_request
    character().mod_cc(cc_name, -cc_use)
    if character().temp_hp < 10:
        character().set_temp_hp(10)
    return_string = (
        f' -title "{name} drinks {ability_name}!" '
        f' -desc "For 1 hour after drinking it, you gain 10 temporary hit points that last for 1 hour. For the same duration, you are under the effect of the bless spell (no concentration required). This blue potion bubbles and steams as if boiling." '
        f' -f "HP|{character().hp_str()}|inline" '
        )
else:
    cc_use = 0
    return_string = (
        f' -title "{name} fails to drink {ability_name}!" '
        f' -desc "No {cc_name} remaining." '
        )
cc_current = cc_str(cc_name)
return_string += (
    f' -f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    f' -footer "{ctx.prefix}{ctx.alias}" '
    )
return return_string
</drac2>