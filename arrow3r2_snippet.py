!snippet a3r2 tembed
<drac2>
num = 2
bonus = 3
cc_name = "+" + bonus +" Arrows"
cc_value = character().get_cc(cc_name)
n = min(cc_value, num)
return_string = f'-rr {num}'
cc_use = n
character().mod_cc(cc_name, -cc_use)
if n == 0:  
    return_string += f' -f "No {cc_name} Left|This attack was made with a mundane ammunition." '
else:
    return_string += f' -b{n} {bonus} -d{n} {bonus}'
    if n < num:
        return_string += f' -f "Not Enough {cc_name} Left|These attacks were made with {n} {cc_name} and {num - n} pieces of mundane ammo. The mundane ammo damage will be incorrect if any of the {cc_name} missed." '
cc_current = character().cc_str(cc_name)
return_string += f' -f "{cc_name} (-{cc_use})| {cc_current}|inline"'
return return_string
</drac2>