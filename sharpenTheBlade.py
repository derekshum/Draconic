!alias sharpen tembed
<drac2>
if len(&ARGS&) > 0:
    args = &ARGS&
    cc_request = int(args[0][0]) #ki points to spend
else:
    cc_request = 3
cc_name = "Ki Points"
cc_value = character().get_cc(cc_name)
return_string = ""
if cc_value >= cc_request:
    cc_use = cc_request
    character().mod_cc(cc_name, -cc_request)
    return_string = (
        f'-title "{name} uses Sharpen the Blade!" '
        f'-desc "As a bonus action, you can expend up to 3 ki points to grant one kensei weapon you touch a bonus to attack and damage rolls when you attack with it. The bonus equals the number of ki points you spent. This bonus lasts for 1 minute or until you use this feature again. This feature has no effect on a magic weapon that already has a bonus to attack and damage rolls." '
        f'-f "Weapon Bonus | +{cc_request}|inline" '
        )
else:
    cc_use = 0
    return_string = (
        f'-title "{name} fails to use Sharpen the Blade!" '
        )
cc_current = cc_str(cc_name)
return_string += (
    f'-f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    f'-footer "{ctx.prefix}{ctx.alias} [# ki (optional, default 3)]"'
    #f'-footer "SOURCE | {"@"+"USERNAME"}" '
    #f'-thumb {image} '
    )
return return_string
</drac2>