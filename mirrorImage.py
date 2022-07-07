!cc create "Mirror Images" -min 0 -max 3 -type bubble -reset short -resetto 0

!snippet mi tembed 
<drac2> 
character().mod_cc("Mirror Images", 3) 
cc_name = "Mirror Images"
return_string = f'-f "{cc_name}|{character().cc_str(cc_name)}" '
return return_string
</drac2>

!alias miFill cast "Mirror Image" mi

!alias mi- cc "Mirror Image" -1

!alias mi 
tembed
<drac2>
to_hit = 0
to_hit_set = False
cc_txt = ""
if len(&ARGS&) > 0:
    args = &ARGS&
    to_hit = int(args[0])
    to_hit_set = True
    cc_txt = " (-0)"
cc_name = "Mirror Images"
cc_value = character().get_cc(cc_name)
if cc_value > 0:
    return_string = (
        f'-desc "A creature is unaffected by this spell if it can\'t see, if it relies on senses other than sight, such as blindsight, or if it can perceive illusions as false, as with truesight." '
        )
    r = vroll("d20")
    hit = False
    if cc_value == 1:
        mi_val = 11                            
    elif cc_value == 2:
        mi_val = 8
    else:
        mi_val = 6
    if r.total >= mi_val:
        ac = 10 + dexterityMod
        return_string += f'-f "Mirror Image Targetted|[{r}] >= {mi_val}|inline" '        
        if to_hit_set:
            if to_hit < ac:
                return_string += (
                    f'-title "A Mirror Image is Missed!" '
                    f'-f "Mirror Image Missed| AC {ac} > {to_hit} |inline" '
                    )
            else:
                return_string += (
                    f'-title "A Mirror Image is Hit!" '
                    f'-f "Mirror Image Hit| AC {ac} <= {to_hit} |inline" '           
                    )                
                character().mod_cc(cc_name, -1)
                cc_current = character().cc_str(cc_name)
                cc_txt = " (-1)"
        else:
            return_string += (
                f'-title "A Mirror Image is Targetted!" '
                f'-f "Mirror Image AC|{ac}|inline" '             
                )
    else:
        return_string += (
            f'-title "{name} is Targetted!" '
            f'-f "{name} Targetted|[{r}] < {mi_val}|inline" '
            )
else:
    cc_use = 0
    return_string = (
        f' -title "{name} has no {cc_name}!" '
        f' -desc "`!cmi` will cast the spell and fill the cc." '
        )
return_string += (
    f'-f "{cc_name}|{character().cc_str(cc_name)}{cc_txt}|inline" '
    f'-footer "{ctx.prefix}{ctx.alias} [atk roll]" '
    )
return return_string
</drac2>