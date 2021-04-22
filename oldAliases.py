!alias balm embed 
{{cc = "Channel Divinity"}}
{{counterExists=cc_exists(cc)}}
{{currentCC = get_cc(cc) if counterExists else 0}}
{{sufficientCC = currentCC >= 1}}
{{set("heal", vroll("2d6 + " + str(wisdomMod)))}}
{{mod_cc(cc, -1) if sufficientCC else ''}}
-title {{'"You do not have a counter set up for {cc}."' if not counterExists else f''' -title "{name} uses Balm of Peace!" -desc "As an action, you can move up to your speed, without provoking opportunity attacks, and when you move within 5 feet of any other creature during this action, you can restore a number of hit points to that creature equal to 2d6 + your Wisdom modifier ({wisdomMod}). A creature can receive this healing only once whenever you take this action." -f "Healing (rolled once for simplicity)|{str(heal)}|inline" ''' if sufficientCC else f''' -title "{name} tried to use Balm of Peace" -desc "You do not have any remaining uses of {cc}. Take a short rest." '''}}
-f "{{cc}} ({{1 if sufficientCC else 0}} used)| {{cc_str(cc) if counterExists else f'No {cc} counter.'}}|inline"
-footer "{{ctx.prefix}}{{ctx.alias}}"

!alias bardic tembed 
<drac2>
cc_name = "Bardic Inspired"
character().create_cc_nx(cc_name, 0, 1, "none", "bubble")
cc_value = character().get_cc(cc_name)
return_string = ""
args =  &ARGS&
die_size = "d" + str(args[0]) if len(args)>0 else "d6"
original_result = str(args[1]) if len(args)>1 else "no roll"


if cc_value >= 1:
    character().mod_cc(cc_name, -1)
    cc_value = cc_value - 1

    inspiration_roll = vroll(original_result + "+ 1" +die_size) if original_result != "no roll" else vroll("+ 1" +die_size)
    return_string = (
        f'-title "{name} feels inspired!" '
        f'-f "Once within the next 10 minutes, the creature can roll the die and add the number rolled to one ability check, attack roll, or saving throw it makes. The creature can wait until after it rolls the d20 before deciding to use the Bardic Inspiration die, but must decide before the DM says whether the roll succeeds or fails. Once the Bardic Inspiration die is rolled, it is lost. A creature can have only one Bardic Inspiration die at a time." '
        f'-f "Roll | {inspiration_roll}" '
    )

else:
    return_string = (
        f'-title "{name} is not inspired" '
        f'-desc "Use `!cc bard 1` to gain bardic inspiration" '
    )
return_string += f'-thumb {image} '
return_string += f'-footer "{ctx.prefix}{ctx.alias} [bardic die (optional, default to 6)][roll (optional if bardic filled, defaults to 0)]"'
return return_string
</drac2>

!alias deft embed
{{args = "%1%%"}}{{args=args[:args.index("%")]}}
{{crit = "crit" in args or "c" in args}}
{{cc = "Ki Points"}}
{{kiCounterExists = cc_exists(cc)}}
{{currentKi = get_cc(cc) if kiCounterExists else 0}}
{{sufficientKi = currentKi >= 1}}
{{mod_cc(cc, -1) if sufficientKi else ''}}
{{set("num", 2 if crit else 1)}}
{{set("die",4+int((MonkLevel+1)/6)*2)}}
{{set("rol",str(num)+"d"+str(die))}}
{{set("dmg",vroll(rol))}}
{{f''' -title "{name} uses Deft Strike!" -desc "When you hit a target with a kensei weapon, you can spend 1 ki point to cause the weapon to deal extra damage to the target equal to your Martial Arts die. You can use this feature only once on each of your turns." -f "Damage {"(CRIT!)" if crit else ""}| {str(dmg)}" ''' if sufficientKi else f''' -title "{name} tries to use Deft Strike" -desc "{'Insufficient ' if kiCounterExists else 'No '} {cc}! {'Take a short or long rest to regain ' if kiCounterExists else 'Create a CC for '} {cc}." ''' }}
-f "{{cc}} ({{1 if sufficientKi else 0}} used)| {{cc_str(cc) if kiCounterExists else f'No {cc} counter.'}}|inline"
-footer "{{ctx.prefix}}{{ctx.alias}} [crit (or c) if crit]"

!alias embolden embed {{cc = "Emboldening Bond"}}{{counterExists=cc_exists(cc)}}{{currentCC = get_cc(cc) if counterExists else 0}}{{sufficientCC = currentCC >= 1}}{{'cc "Emboldening Bond" -1' if sufficientCC else ''}}
{{mod_cc(cc, -1) if sufficientCC else ''}}
-title {{'"You do not have a counter set up for {cc}."' if not counterExists else f''' -title "{name} uses Emboldening Bond!" -desc "As an action, you choose a number of willing creatures within 30 feet of you (this can include yourself) equal to your proficiency bonus ({proficiencyBonus}). You create a magical bond among them for 10 minutes or until you use this feature again. While any bonded creature is within 30 feet of another, the creature can roll a d4 and add the number rolled to an attack roll, an ability check, or a saving throw it makes. Each creature can add the d4 no more than once per turn." ''' if sufficientCC else f''' -title "{name} tried to use Emboldening Bond" -desc "You do not have any remaining uses of {cc}. Take a long rest." '''}}
-f "{{cc}} ({{1 if sufficientCC else 0}} used)| {{cc_str(cc) if counterExists else f'No {cc} counter.'}}|inline"
-footer "{{ctx.prefix}}{{ctx.alias}}"

!alias focused embed 
{{args = "%1%%"}}
{{args=args[:args.index("%")]}}
{{args=''.join([i for i in args if i.isdigit()])}}
{{kiSpend = int(args) if args.isdigit() else 1}}
{{outOfKiRange = (kiSpend < 1 or kiSpend > 3)}}
{{cc = "Ki Points"}}
{{kiCounterExists = cc_exists(cc)}}
{{currentKi = get_cc(cc) if kiCounterExists else 0}}
{{legalKi = not outOfKiRange and currentKi >= kiSpend}}
{{mod_cc(cc, -kiSpend) if legalKi else ''}}
{{f''' -title "Focused Aim must use 1 to 3 {cc} " -desc "Enter a number of {cc} between 1 and 3." ''' if outOfKiRange else f''' -title "{name} uses Focused Aim!" -desc "When you miss with an attack roll, you can spend 1 to 3 ki points to increase your attack roll by 2 for each of these ki points you spend, potentially turning the miss into a hit." -f "Attack Bonus|+{kiSpend * 2}|inline" ''' if legalKi else f''' -title "{name} tries to use Focused Aim" -desc "{'Insufficient ' if kiCounterExists else 'No '} {cc}! {'Take a short or long rest to regain ' if kiCounterExists else 'Create a CC for '} {cc}." -f "Attempted {cc} Use|{kiSpend}|inline" ''' }}
-f "{{cc}} ({{kiSpend if legalKi else 0}} used)| {{cc_str(cc) if kiCounterExists else f'No {cc} counter.'}}|inline"
-footer "{{ctx.prefix}}{{ctx.alias}} [(Optional) # of Ki]"

!alias harness1 embed 
{{cc1 = "Channel Divinity"}}
{{counterExists1 = cc_exists(cc1)}}
{{currentCC1 = get_cc(cc1) if counterExists1 else 0}}
{{sufficientCC1 = currentCC1 >= 1}}
{{cc2 = "Harness Divine Power"}}
{{counterExists2 = cc_exists(cc1)}}
{{currentCC2 = get_cc(cc2) if counterExists2 else 0}}
{{sufficientCC2= currentCC2 >= 1}}
{{go = sufficientCC1 and sufficientCC2 and get_slots(1) < get_slots_max(1)}}
{{mod_cc(cc1, -1) if go else ''}}
{{mod_cc(cc2, -1) if go else ''}}
{{set_slots(1,get_slots(1)+1) if go else ''}}
-title {{'"You do not have a counter set up for {cc1} and/or {cc2}."' if not counterExists1 and counterExists2 else f''' -title "{name} uses Harness Divine Power (1st level)!" -desc "You can expend a use of your Channel Divinity to fuel your spells. As a bonus action, you touch your holy symbol, utter a prayer, and regain one expended spell slot, the level of which can be no higher than half your proficiency bonus (rounded up)." ''' if go else f''' -title "{name} tried to use Harness Divine Power (1st level)" -desc "You do not have any first level spell slots to recover and/or you do not have any remaining uses of {cc1} and/or {cc2}." '''}}
{{slots=[slots_str(x) for x in range(1,10) if get_slots_max(x)]}}
{{change = 1 if go else 0}}
{{'-f "Spell Slots (+"' + str(change) + '" 1st)|'+'\n'.join(slots)+'"' if slots else ""}}
-f "{{cc1}} (-{{1 if go else 0}})|{{cc_str(cc1) if counterExists1 else f'No {cc1} counter.'}}|inline"
-f "{{cc2}} (-{{1 if go else 0}})|{{cc_str(cc2) if counterExists2 else f'No {cc2} counter.'}}|inline"
-footer "{{ctx.prefix}}{{ctx.alias}}"

!alias harness2 embed 
{{cc1 = "Channel Divinity"}}
{{counterExists1 = cc_exists(cc1)}}
{{currentCC1 = get_cc(cc1) if counterExists1 else 0}}
{{sufficientCC1 = currentCC1 >= 1}}
{{cc2 = "Harness Divine Power"}}
{{counterExists2 = cc_exists(cc1)}}
{{currentCC2 = get_cc(cc2) if counterExists2 else 0}}
{{sufficientCC2= currentCC2 >= 1}}
{{go = sufficientCC1 and sufficientCC2 and get_slots(2) < get_slots_max(2)}}
{{mod_cc(cc1, -1) if go else ''}}
{{mod_cc(cc2, -1) if go else ''}}
{{set_slots(2,get_slots(2)+1) if go else ''}}
-title {{'"You do not have a counter set up for {cc1} and/or {cc2}."' if not counterExists1 and counterExists2 else f''' -title "{name} uses Harness Divine Power 2nd level)!" -desc "You can expend a use of your Channel Divinity to fuel your spells. As a bonus action, you touch your holy symbol, utter a prayer, and regain one expended spell slot, the level of which can be no higher than half your proficiency bonus (rounded up)." ''' if go else f''' -title "{name} tried to use Harness Divine Power (2nd level)" -desc "You do not have any second level spell slots to recover and/or you do not have any remaining uses of {cc1} and/or {cc2}." '''}}
{{slots=[slots_str(x) for x in range(1,10) if get_slots_max(x)]}}
{{change = 1 if go else 0}}
{{'-f "Spell Slots (+"' + str(change) + '" 2nd)|'+'\n'.join(slots)+'"' if slots else ""}}
-f "{{cc1}} (-{{1 if go else 0}})|{{cc_str(cc1) if counterExists1 else f'No {cc1} counter.'}}|inline"
-f "{{cc2}} (-{{1 if go else 0}})|{{cc_str(cc2) if counterExists2 else f'No {cc2} counter.'}}|inline"
-footer "{{ctx.prefix}}{{ctx.alias}}"

!alias harness3 embed 
{{cc1 = "Channel Divinity"}}
{{counterExists1 = cc_exists(cc1)}}
{{currentCC1 = get_cc(cc1) if counterExists1 else 0}}
{{sufficientCC1 = currentCC1 >= 1}}
{{cc2 = "Harness Divine Power"}}
{{counterExists2 = cc_exists(cc1)}}
{{currentCC2 = get_cc(cc2) if counterExists2 else 0}}
{{sufficientCC2= currentCC2 >= 1}}
{{go = sufficientCC1 and sufficientCC2 and get_slots(3) < get_slots_max(3)}}
{{mod_cc(cc1, -1) if go else ''}}
{{mod_cc(cc2, -1) if go else ''}}
{{set_slots(3,get_slots(3)+1) if go else ''}}
-title {{'"You do not have a counter set up for {cc1} and/or {cc2}."' if not counterExists1 and counterExists2 else f''' -title "{name} uses Harness Divine Power (3rd level)!" -desc "You can expend a use of your Channel Divinity to fuel your spells. As a bonus action, you touch your holy symbol, utter a prayer, and regain one expended spell slot, the level of which can be no higher than half your proficiency bonus (rounded up)." ''' if go else f''' -title "{name} tried to use Harness Divine Power (3rd level)" -desc "You do not have any third level spell slots to recover and/or you do not have any remaining uses of {cc1} and/or {cc2}." '''}}
{{slots=[slots_str(x) for x in range(1,10) if get_slots_max(x)]}}
{{change = 1 if go else 0}}
{{'-f "Spell Slots (+"' + str(change) + '" 3rd)|'+'\n'.join(slots)+'"' if slots else ""}}
-f "{{cc1}} (-{{1 if go else 0}})|{{cc_str(cc1) if counterExists1 else f'No {cc1} counter.'}}|inline"
-f "{{cc2}} (-{{1 if go else 0}})|{{cc_str(cc2) if counterExists2 else f'No {cc2} counter.'}}|inline"
-footer "{{ctx.prefix}}{{ctx.alias}}"

!alias hhelm {{cc = "Helm of the Gods"}}{{counterExists=cc_exists(cc)}}{{currentCC = get_cc(cc) if counterExists else 0}}{{sufficientCC = currentCC >= 1}}{{'cast "hellish rebuke" -dc 13 -i' if sufficientCC else 'embed'}}
{{mod_cc(cc, -1) if sufficientCC else ''}}
-title {{'"You do not have a counter set up for your Helm of the Gods."' if not counterExists else f'''"{name} uses their Helm of the Gods to Cast Hellish Rebuke!"''' if sufficientCC else '''"You do not have any remaining uses of you Helm of the Gods. Take a long rest."'''}}
-f "{{cc}} ({{1 if sufficientCC else 0}} used)| {{cc_str(cc) if counterExists else f'No {cc} counter.'}}|inline"
-footer "{{ctx.prefix}}{{ctx.alias}}"

!alias quickened embed 
{{cc = "Ki Points"}}
{{kiCounterExists = cc_exists(cc)}}
{{currentKi = get_cc(cc) if kiCounterExists else 0}}
{{sufficientKi = currentKi >= 2}}
{{mod_cc(cc, -2) if sufficientKi else ''}}
{{initialHP = get_hp()}}
{{set("die",4+int((MonkLevel+1)/6)*2)}}
{{set("pb",proficiencyBonus)}}
{{set("rol","1d" + str(die) + " + " + str(pb))}}
{{set("heal", vroll(rol))}}
{{set_hp(get_hp()+heal.total)}}
{{f''' -title "{name} uses Quickened Healing!" -desc "As an action, you can spend 2 ki points and roll a Martial Arts die. You regain a number of hit points equal to the number rolled plus your proficiency bonus." -f "Healing |{str(heal)}|inline" -f "HP (+{get_hp()-initialHP})|{get_hp()}/{hp}|inline" ''' if sufficientKi else f''' -title "{name} tries to use Quickened Healing" -desc "{'Insufficient ' if kiCounterExists else 'No '} {cc}! {'Take a short or long rest to regain ' if kiCounterExists else 'Create a CC for '} {cc}." -f "Attempted {cc} Use|{2}|inline" ''' }}
-f "{{cc}} ({{2 if sufficientKi else 0}} used)| {{cc_str(cc) if kiCounterExists else f'No {cc} counter.'}}|inline"
-footer "{{ctx.prefix}}{{ctx.alias}}"

!alias wyvern embed 
{{set("poison", vroll("7d6"))}}
{{f''' -title "{name} uses Wyvern Poison!" -desc "A creature subjected to this poison must make a DC 15 Constitution saving throw, taking {str(poison)} poison damage on a failed save, or half as much ({str(int(poison.total/2))}) damage on a successful one." '''}}
-footer "{{ctx.prefix}}{{ctx.alias}}"

