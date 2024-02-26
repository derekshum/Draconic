!alias font tembed
<drac2>
slot_level = 0
for input in &ARGS&:
    input = input.lower()
    length = len(input)
    if input.isnumeric():
        slot_level = int(input)
if character().spellbook.get_slots(slot_level) < 1:
    return f' -title "{name} doesn\'t have enough level {slot_level} spell slots remaining!" -desc "Spell Slots (-0)| {character().spellbook.slots_str(slot_level)}"'
cn1 = "Sorcery Points"
cm1 = 0

if character().cc_exists(cn1):
    cm1 = character().get_cc_max(cn1) - character().get_cc(cn1)
character().spellbook.use_slot(slot_level)

rs = (
    f'-title "{name} consumes a spell slot to restore Sorcery and Metamagic points" '
    f'-desc "Spell Slots (-1)| {character().spellbook.slots_str(slot_level)}" '    
)

recovery = slot_level
cr1 = recovery if cm1 >= recovery else cm1
recovery -= cr1
character().mod_cc(cn1, cr1)
rs += f'-f "{cn1} (+{cr1})|{character().cc_str(cn1)}|inline" '

cn2 = "Metamagic Points"
cm2 = 0
if character().cc_exists(cn2):
    cm2 = character().get_cc_max(cn2) - character().get_cc(cn2)
    cr2 = recovery if cm2 >= recovery else cm2
    recovery -= cr2
    character().mod_cc(cn2, cr2)
    rs += f'-f "{cn2} (+{cr2})|{character().cc_str(cn2)}|inline" '

if recovery > 0:
    rs += f' -f "Unused Recovery|{recovery} points|inline" '

rs += f'-footer "{ctx.prefix}{ctx.alias} " '
return rs
</drac2>