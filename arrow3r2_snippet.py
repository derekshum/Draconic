!snippet p3r2 tembed
<drac2>
num = 2
cc_name = "+3 Arrows"
cc_value = character().get_cc(cc_name)
n = min(cc_value, num)
return_string = f'-rr {num}'
cc_use = n
character().mod_cc(cc_name, -cc_use)
if n == 0:  
    return_string += f' -f "No +3 Arrows Left|All of these attack were made with mundane arrows." '
else:
    return_string += f' -b{n} 3 -d{n} 3'
    if n < num:
        p3 = ""
        if n > 1:
            p3 = "s"
        m = ""
        if num - n > 1:
            m = "s"
        return_string += f' -f "Not Enough +3 Arrows Left|These attacks were made with {n} +3 arrow{p3} and {num - n} mundane arrow{m}. The mundane arrow damage will be incorrect if any of the +3 arrows missed." '
cc_current = cc_str(cc_name)
return_string += f' -f "{cc_name} (-{cc_use})| {cc_current}|inline"'
return return_string
</drac2>