!alias ash tembed
<drac2>
num_d6 = 1
damage_type = "fire"
movement = -1
for input in &ARGS&:
    input = input.lower()
    length = len(input)
    if length == 3 and input[0:2] == "lv":
        num_d6 = int(input[2]) - 2
    elif length > 2 and input[length - 2: length] == "ft":
        movement = int(input[0:length - 2])
    elif length > 4 and input[length - 4: length] == "feet":
        movement = int(input[0:length - 4])
    elif input[0].isdigit():
        args = &ARGS&
        num_d6 = int(input)
    else:
        damage_type = input
level = num_d6 + 2  
ability_name = "Ashardalon's Stride"
damage = vroll(num_d6 + "d6[" + damage_type + "]")
return_string = (
    f' -title "{name} uses {ability_name} at level {level}!"'
    f' -f "Damage (rolled once per turn for simplicity)|{str(damage)}|inline"'
    f' -footer "{ctx.prefix}{ctx.alias}"'
    )
if movement != -1:
    return_string += f' -f "Total Movement|{movement} feet|inline"'
else:
    return_string += f' -f "Movement Bonus|+{15 + 5 * num_d6 } feet|inline"'
return return_string
</drac2>