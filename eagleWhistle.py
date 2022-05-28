!alias ew tembed
<drac2>
ability_name = "their Eagle Whistle"
cc_name = "Eagle Whistle"
cc_value = character().get_cc(cc_name)
return_string = ""
if cc_value >= 1:
    cc_use = 1
    character().mod_cc(cc_name, -cc_use)
    rounds = max(5 + 5 * constitutionMod, 1) # a number of rounds equal to 5 + five times your Constitution modifier (minimum of 1 round)
    return_string = (
        f'-title "{name} uses {ability_name}!" '
        f'-desc "While you blow an eagle whistle continuously, you can fly twice as fast as your walking speed. You can blow the whistle continuously for **{str(rounds)} rounds**  or until you talk, hold your breath, or start suffocating. A use of the whistle also ends if you land. If you are aloft when you stop blowing the whistle, you fall. The whistle has three uses. It regains expended uses daily at dawn." '
        )
else:
    cc_use = 0
    return_string = (
        f' -title "{name} fails to use {ability_name}!" '
        f' -desc "The whistle has three uses. It regains expended uses daily at dawn." '
        )
cc_current = character().cc_str(cc_name)
return_string += (
    f'-f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    f'-footer "{ctx.prefix}{ctx.alias}"'
    )
return return_string
</drac2>