#!cc create "Aberrant Dragonmark: Shield" -max 1 -min 0 -type bubble -reset short -title "Aberrant Dragonmark: Shield" -desc "Once you cast [this spell], you must finish a short or long rest before you can cast it again through the mark. Constitution is your spellcasting ability for these spells.
#
#When you cast the 1st-level spell through your mark, you can expend one of your Hit Dice and roll it. If you roll an even number, you gain a number of temporary hit points equal to the number rolled. If you roll an odd number, one random creature within 30 feet of you (not including you) takes force damage equal to the number rolled. If no other creatures are in range, you take the damage."

# input declaration
# if len(&ARGS&) > 0:
    # args = &ARGS&
    # input = args[0].lower()
    # #TODO

!alias ads tembed
<drac2>
ability_name = "their Aberrant Dragonmark to cast Shield"
cc_name = "Aberrant Dragonmark: Shield"
cc_value = character().get_cc(cc_name)
return_string = ""
if cc_value >= 1:
    cc_use = 1
    character().mod_cc(cc_name, -cc_use)
    return_string = (
        f'-title "{name} uses {ability_name}!" '
        f'-desc "**Casting Time:** 1 reaction, which you take when you are hit by an attack or targeted by the magic missile spell\n**Range:** Self\n**Components:** V, S\n**Duration:** 1 round\n**Description**\nAn invisible barrier of magical force appears and protects you. Until the start of your next turn, you have a +5 bonus to AC, including against the triggering attack, and you take no damage from magic missile." '    #TODO
        # TODO f' -f "Damage{crit_text}|{str(damage)}|inline" '
        )
else:
    cc_use = 0
    return_string = (
        f' -title "{name} fails to use {ability_name}!" '
        f' -desc "Take a short or long rest." '
        )
cc_current = cc_str(cc_name)
return_string += (
    f'-f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    f'-footer "{ctx.prefix}{ctx.alias}"'    #TODO: add any additional inputs
    )
return return_string
</drac2>