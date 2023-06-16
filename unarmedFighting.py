!alias uf tembed
<drac2>
damage = vroll("1d4")
return_string = (
    f' -title "{name}\'s Unarmed Fighting gives a grappled target a good shake!" '
    f' -desc "At the start of each of your turns, you can deal {damage} bludgeoning damage to one creature grappled by you." '
)
return_string += f' -footer "{ctx.prefix}{ctx.alias}" '
return return_string
</drac2>