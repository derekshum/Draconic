!alias blink tembed
<drac2>
r = vroll("1d20")
return_string = (f' -desc "{str(r)}"')
if r.total >= 11:
    return_string += (f' -title "{name} blinks out!"')
else:
    return_string += (f' -title "{name} is still there!"')
return_string += (f' -footer "{ctx.prefix}{ctx.alias}"')
return return_string
</drac2>