!alias fm tembed
<drac2>
num_die = 1
crit_text = ""
is_resistant = False
is_vulnerable = False
for input in &ARGS&:
    input = input.lower()
    length = len(input)
    if input == "critical"[0:length]:
        num_die = 2
        crit_text = " (CRIT!)"
ability_name = "a Mobile Flourish"
cc_name = "Bardic Inspiration"
cc_value = character().get_cc(cc_name)
if cc_value >= 1:
    cc_use = 1
    character().mod_cc(cc_name, -cc_use)
    damage = vroll(str(num_die) + "d" + (int(BardLevel / 5 + 3) * 2))
    return_string = (
        f' -title "{name} uses {ability_name}!" '
        f' -desc "You can expend one use of your Bardic Inspiration to cause the weapon to deal extra damage to the target you hit. The damage equals the number you roll on the Bardic Inspiration die. You can also push the target up to 5 feet away from you, plus a number of feet equal to the number you roll on that die. You can then immediately use your reaction to move up to your walking speed to an unoccupied space within 5 feet of the target." '
        f' -f "Damage{crit_text}|{str(damage)}|inline" '
        f' -f "Max Push Distance|{str(5 + damage.total)} feet (rounds to {str(5 + int((damage.total + 2) / 5) * 5)} feet)|inline" '
        )
else:
    cc_use = 0
    return_string = (
        f' -title "{name} fails to use {ability_name}!" '
        f' -desc "No {cc_name} remaining." '
        )
cc_current = character().cc_str(cc_name)
return_string += (
    f'-f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    f'-footer "{ctx.prefix}{ctx.alias} [crit]" '
    )
return return_string
</drac2>