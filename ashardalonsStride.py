!alias ash tembed
<drac2>
num_d6 = 1
damage_type = "fire"
for input in &ARGS&:
    input = input.lower()
    length = len(input)
    if input[0].isdigit():
        args = &ARGS&
        num_d6 = int(input)
    elif length == 3 and input[0:2] == "lv":
        num_d6 = int(input[2]) - 2
    else:
        damage_type = input
level = num_d6 + 2
movement_bonus = 15 + 5 * num_d6    
ability_name = "Ashardalon's Stride"
damage = vroll(num_d6 + "d6[" + damage_type + "]")
return_string = (
    f' -title "{name} uses {ability_name} at level {level}!"'
    f' -f "Damage (rolled once per turn for simplicity)|{str(damage)}|inline"'
    f' -f "Movement Bonus|+{movement_bonus} feet|inline"'
    f' -footer "{ctx.prefix}{ctx.alias}"'
    )
return return_string
</drac2>