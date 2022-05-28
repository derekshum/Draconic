!alias gtt tembed
<drac2>
ability_name = "casts Tenser's Transformation"
cc_name = "Topaz Spell Gem"
cc_value = character().get_cc(cc_name)
return_string = ""
cc_request = 1
if cc_value >= cc_request:
    cc_use = cc_request
    character().mod_cc(cc_name, -cc_use)
    if character().temp_hp < 50:
        character().set_temp_hp(50)
    return_string = (
        f' -title "{name} {ability_name}!" '
        f' -desc "- You gain 50 temporary hit points. If any of these remain when the spell ends, they are lost.\n- You have advantage on attack rolls that you make with simple and martial weapons.\n- When you hit a target with a weapon attack, that target takes an extra 2d12 force damage.\n- You have proficiency with all armor, shields, simple weapons, and martial weapons.\n- You have proficiency in Strength and Constitution saving throws.\n- You can attack twice, instead of once, when you take the Attack action on your turn. You ignore this benefit if you already have a feature, like Extra Attack, that gives you extra attacks." '
        f' -f "HP|{character().hp_str()}|inline" '
        )
else:
    cc_use = 0
    return_string = (
        f' -title "{name} fails to cast!" '
        f' -desc "{cc_name} Empty." '
        )
cc_current = character().cc_str(cc_name)
return_string += (
    f' -f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    f' -footer "{ctx.prefix}{ctx.alias}" '
    )
return return_string
</drac2>