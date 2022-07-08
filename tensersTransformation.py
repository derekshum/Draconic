!alias tt tembed
<drac2>
ability_name = "casts Tenser's Transformation"
if character().temp_hp < 50:
    character().set_temp_hp(50)
return_string = (
    f' -title "{name} {ability_name}!" '
    f' -desc "- You gain 50 temporary hit points. If any of these remain when the spell ends, they are lost.\n- You have advantage on attack rolls that you make with simple and martial weapons.\n- When you hit a target with a weapon attack, that target takes an extra 2d12 force damage.\n- You have proficiency with all armor, shields, simple weapons, and martial weapons.\n- You have proficiency in Strength and Constitution saving throws.\n- You can attack twice, instead of once, when you take the Attack action on your turn. You ignore this benefit if you already have a feature, like Extra Attack, that gives you extra attacks." '
    f' -f "HP|{character().hp_str()}|inline" '
    )
return_string += f' -footer "{ctx.prefix}{ctx.alias}" '
return return_string
</drac2>