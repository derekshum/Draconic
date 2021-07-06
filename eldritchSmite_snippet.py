!snippet elsm tembed
<drac2>
warlock_slot = int(WarlockLevel/2)+1
cc_value = get_slots(warlock_slot)
if cc_value >= 1:
    use_slot(warlock_slot)
    return_string = (f' -d1 "{str(warlock_slot + 1)}d8[force]"'
        f' -f "Eldritch Smite|Once per turn when you hit a creature with your pact weapon, you can expend a warlock spell slot to deal an extra 1d8 force damage to the target, plus another 1d8 per level of the spell slot, and you can knock the target prone if it is Huge or smaller."'
        f' -f "Spell Slots (-1)| {slots_str(warlock_slot)}"'
        )
else:
    return_string = (
        f' -f "No more warlock spell slots|Take a short rest."'
        f' -f "Spell Slots (-0)| {slots_str(warlock_slot)}"'
        )
return return_string
</drac2>