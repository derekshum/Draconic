!alias call tembed
<drac2>
result = vroll("1d4")
creature = "Gardox summons a "
match result.total:
    case 1:
        creature += "cursed."
    case 2:
        creature += "greater."
    case 3:
        creature += "belcher."
    case 4:
        creature += "despoiler."
return_string = (
    f' -title "Gardox summons his hordes!" '
    f' -f "Roll|{str(result)}|inline" '
    f' -desc "{creature}" '
)
return return_string
</drac2>