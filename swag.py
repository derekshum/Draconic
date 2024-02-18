!alias swag tembed
<drac2>
dc_set = False
dc = 0
bonus = ""
for input in &ARGS&:
    if input.isnumeric() and not dc_set:
        dc = int(input)
        dc_set = True
    else:
        bonus += input
    

roll_string = "1d20" + ("+" + bonus if len(bonus) > 0 else "") 
r = vroll(roll_string)
if r.total >= dc:
    return_string = (
        f' -f "Roll|{r} >= {dc}|inline" '
        f' -f "d10 roll|{vroll("1d10")}|inline" '
    )
else:
    return_string = f' -f "Roll|{r} < {dc}|inline" '
return return_string
</drac2>