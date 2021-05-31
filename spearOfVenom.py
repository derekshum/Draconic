#!cc create "Spear of Venom" -max 1 -min 0 -reset long -type bubble -desc "You can use an action to cause thick, black poison to coat the this weapon. The poison remains for 1 minute or until an attack using this weapon hits a creature. That creature must succeed on a DC 15 Constitution saving throw or take 2d10 poison damage and become poisoned for 1 minute. The weapon can't be used this way again until the next dawn."

!alias venom tembed
<drac2>
ability_name = "their Spear of Venom"
cc_name = "Spear of Venom"
cc_value = character().get_cc(cc_name)
return_string = ""
if cc_value >= 1:
    cc_use = 1
    character().mod_cc(cc_name, -cc_use)
    damage = vroll("2d10")
    return_string = (
        f'-title "{name} uses {ability_name}!" '
        f'-desc "You can use an action to cause thick, black poison to coat this weapon. The poison remains for 1 minute or until an attack using this weapon hits a creature. That creature must succeed on a DC 15 Constitution saving throw or take {str(damage)} poison damage and become poisoned for 1 minute. The weapon can\'t be used this way again until the next dawn." '
        )
else:
    cc_use = 0
    return_string = (
        f' -title "{name} fails to use {ability_name}!" '
        f' -desc "Your {cc_name} has no remaining charges." '
        )
cc_current = cc_str(cc_name)
return_string += (
    f'-f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    f'-footer "{ctx.prefix}{ctx.alias}"'
    )
return return_string
</drac2>