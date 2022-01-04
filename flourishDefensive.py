!alias fd tembed
<drac2>
ac_bonus = 0
ac_bonus_set = False
num_die = 1
crit_text = ""
is_resistant = False
is_vulnerable = False
for input in &ARGS&:
    input = input.lower()
    length = len(input)
    if input.isnumeric():
        ac_bonus = int(input)
        ac_bonus_set = True
    elif input == "critical"[0:length]:
        num_die = 2
        crit_text = " (CRIT!)"
ability_name = "a Defensive Flourish"
cc_name = "Bardic Inspiration"
cc_value = character().get_cc(cc_name)
if cc_value >= 1:
    cc_use = 1
    character().mod_cc(cc_name, -cc_use)
    damage = vroll(str(num_die) + "d" + (int(BardLevel / 5 + 3) * 2))
    return_string = (
        f' -title "{name} uses {ability_name}!" '
        f' -desc "You can expend one use of your Bardic Inspiration to cause the weapon to deal extra damage to the target you hit. The damage equals the number you roll on the Bardic Inspiration die. You also add the number rolled to your AC until the start of your next turn." '
        f' -f "Damage/AC Boost{crit_text}|{str(damage)}|inline" '
        )
    if ac_bonus_set:
        ac_bonus_text = ""
        if ac_bonus != 0:
             ac_bonus_text = f' + {ac_bonus}'
        return_string += f' -f "New AC|{character().ac} {ac_bonus_text} + {damage.total} = {character().ac + ac_bonus + damage.total}|inline" '
else:
    cc_use = 0
    return_string = (
        f' -title "{name} fails to use {ability_name}!" '
        f' -desc "No {cc_name} remaining." '
        )
cc_current = cc_str(cc_name)
return_string += (
    f'-f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    f'-footer "{ctx.prefix}{ctx.alias} [AC bonus] [crit]" '
    )
return return_string
</drac2>