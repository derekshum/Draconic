!cc create "Mirror Images" -min 0 -max 3 -type bubble -reset short -resetto 0

!snippet mi tembed 
<drac2> 
character().mod_cc("Mirror Images", 3) 
cc_name = "Mirror Images"
return_string = f'-f "{cc_name}|{cc_str(cc_name)}" '
return return_string
</drac2>

!alias miFill cast "Mirror Image" mi

!alias mi- cc "Mirror Image" -1

!alias mi tembed
<drac2>
#TODO: implement
#to_hit = 0
#if len(&ARGS&) > 0:
#    args = &ARGS&
#    to_hit = int(args[0])
cc_name = "Mirror Images"
cc_value = get_cc(cc_name)
if cc_value > 0:
    return_string = (
        f'-title "{name} has {cc_name}!" '
        f'-desc "A creature is unaffected by this spell if it can\'t see, if it relies on senses other than sight, such as blindsight, or if it can perceive illusions as false, as with truesight." '
        f'-f "{cc_name}|{cc_str(cc_name)}|inline" '
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
        return_string += (
            f'-f "Mirror Image Targetted|[{r}] >= {mi_val}|inline" '
            f'-f "Mirror Image AC|{ac}|inline" ' 
            )        
    else:
        return_string += f'-f "{name} Targetted|[{r}] < {mi_val} ({cc_value} images)|inline" '
else:
    cc_use = 0
    return_string = (
        f' -title "{name} has no {cc_name}!" '
        f' -desc "Perhaps you need to set the cc "Mirror Images"" '
        )
cc_current = cc_str(cc_name)
return_string += (
    f'-footer "{ctx.prefix}{ctx.alias}" ' #[atk roll]
    )
return return_string
</drac2>