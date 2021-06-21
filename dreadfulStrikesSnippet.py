!snippet ds tembed
<drac2>
d = "1d4"
if RangerLevel >= 11:
    d = "1d6"
return_string = (
    f' -d1 {d}[psychic]'
    f' -f "Dreadful Strikes|...When you hit a creature with a weapon, you can deal an extra **{d}** psychic damage to the target, which can take this extra damage only once per turn."'
    )
return return_string
</drac2>