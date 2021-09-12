!alias de tembed
<drac2>
ability_name = "Deflect Energy"
return_string = ""
if MonkLevel >= 11:
    die = int(4 + int((MonkLevel + 1) / 6) * 2)
    damage = vroll("d" + str(die) + "+" + str(wisdomMod))
    return_string = (
        f' -title "{name} uses {ability_name}!"'
        f' -desc "When you take acid, cold, fire, force, lightning, or thunder damage, you can use your reaction to deflect it. When you do so, the damage you take is reduced by 1d10 + your Wisdom modifier (minimum reduction of 1)."'
        f' -f "Damage Reduction|{str(damage)}|inline"'
        )
else:
    return_string = (
        f' -title "{name} fails to use {ability_name}!"'
        f' -desc "Not enough levels in Monk." '
        )
return_string += f' -footer "{ctx.prefix}{ctx.alias}"'
return return_string
</drac2>