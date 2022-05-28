!alias hmeteor tembed
<drac2>
cc_request = 1
spell_level = 9
cc1_name = "Sorcery Points"
cc2_name = "Channel Divinity"
ability_name = "casts Meteor Swarm"
cc1_val = character().get_cc(cc1_name)
cc2_val = character().get_cc(cc2_name)
return_string = ""
if character().spellbook.get_slots(current_level) >= 1 and cc1_val >= 1 and cc2_val >= 1:
    character().spellbook.use_slot(spell_level)
    if is_resistant and is_vulnerable:     
        return_string += f' -f "Calculation Uncertainty|Resisted and Vulnerable damage may have a lower total than displayed due to rounding down odds." '    
    roll_string = "120[lightning] + 20d6[bludgeoning] + 6"
    damage = vroll(roll_string)
    return_string = (
        f' -title "{name} {ability_name}!" '
        f' -desc "**Damage:**{str(damage)}\n**DC:**{int(character().spellbook.dc)}\nDEX Save" '
        f' -f "Effect|Each creature in a 40-foot-radius sphere centered on each point you choose must make a Dexterity saving throw. The sphere spreads around corners. A creature takes 20d6 fire damage and 20d6 bludgeoning damage on a failed save, or half as much damage on a successful one." '
        f' -f "Transmuted Spell|When you cast a spell that deals a type of damage from the following list, you can spend 1 sorcery point to change that damage type to one of the other listed types: acid, cold, fire, lightning, poison, thunder." '
        f' -f "Destructive Wrath|You can use your Channel Divinity to wield the power of the storm with unchecked ferocity. When you roll lightning or thunder damage, you can use your Channel Divinity to deal maximum damage, instead of rolling." '
        f' -f"Elemental Affinity|Starting at 6th level, when you cast a spell that deals damage of the type associated with your draconic ancestry, you can add your Charisma modifier to one damage roll of that spell. At the same time, you can spend 1 sorcery point to gain resistance to that damage type for 1 hour." '
        )
else:
    cc1_use = 0
    cc2_use = 0
    return_string = (
        f' -title "{name} fails to {ability_name}!" '
        f' -desc "One or more of the following is unavailable: level {spell_level} spell slot, {cc1_name}, or {cc2_name}." '
        )
cc1_current = character().cc_str(cc1_name)
cc2_current = character().cc_str(cc2_name)
return_string += (
    f'-f "{cc1_name} (-{cc1_use})| {cc1_current}|inline" '
    f'-f "{cc2_name} (-{cc2_use})| {cc2_current}|inline" '
    f' -f "{character().spellbook.slots_str(spell_level)} (-1)" '
    f' -footer "{ctx.prefix}{ctx.alias}" '
    )
return return_string
</drac2>