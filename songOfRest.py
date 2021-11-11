!alias sor tembed
<drac2>
ability_name = "Song of Rest"
if BardLevel < 9:
    die_size = 6
elif BardLevel < 13:
    die_size = 8
elif BardLevel < 17:
    die_size = 10
else:
    die_size = 12
healing = vroll("1d" + die_size)
return_string = (
    f'-title "{name} uses {ability_name}!" '
    f'-desc "Beginning at 2nd level, you can use soothing music or oration to help revitalize your wounded allies during a short rest. If you or any friendly creatures who can hear your performance regain hit points at the end of the short rest by spending one or more Hit Dice, each of those creatures regains an extra `1d{die_size}` hit points." '
    f' -f "Healing|{str(healing)}|inline" '    
    f'-footer "{ctx.prefix}{ctx.alias}" '
    )
return return_string
</drac2>