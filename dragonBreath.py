#!cc create "Spear of Dragonkind" -min 0 -max 1 -type bubble -reset long -desc "While holding the flail, you can use an action and speak a command word to ~~cause the heads to~~ breathe multicolored flames in a 90-foot cone. Each creature in that area must make a DC 18 Dexterity saving throw. On a failed save, it takes 14d6 damage of one of the following damage types (your choice): acid, cold, fire, lightning, or poison. On a successful save, it takes half as much damage. Once this action is used, it can't be used again until the next dawn."

!alias dra tembed
<drac2>
cc_request = 1
ability_name = "breaths draconic energy"
cc_name = "Spear of Dragonkind"
cc_value = character().get_cc(cc_name)
return_string = ""
if cc_value >= cc_request:
    cc_use = cc_request
    character().mod_cc(cc_name, -cc_use)
    roll_string = "14d6"
    damage = vroll(roll_string)
    return_string = (
        f' -title "{name} {ability_name}!" '
        f' -desc "While holding the flail, you can use an action and speak a command word to ~~cause the heads to~~ breathe multicolored flames in a 90-foot cone. Each creature in that area must make a **DC 18 Dexterity saving throw**. On a failed save, it takes {str(damage)} damage of one of the following damage types (your choice): acid, cold, fire, lightning, or poison. On a successful save, it takes half as much damage. Once this action is used, it can\'t be used again until the next dawn." '
        
        )
else:
    cc_use = 0
    return_string = (
        f' -title "{name} fails to use {ability_name}!" '
        f' -desc "No {cc_name} remaining." '
        )
cc_current = cc_str(cc_name)
return_string += (
    f' -f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    f' -footer "{ctx.prefix}{ctx.alias}" '
    )
return return_string
</drac2>