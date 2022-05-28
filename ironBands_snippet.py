!snippet iron tembed
<drac2>
num = 1
cc_name = "Iron Bands of Binding"
cc_value = character().get_cc(cc_name)
if cc_value >= num:
    cc_use = num
    character().mod_cc(cc_name, -cc_use)
    return_string = f' -f "Iron Bands of Binding|This rusty iron sphere measures 3 inches in diameter and weighs 1 pound. You can use an action to speak the command word and throw the sphere at a Huge or smaller creature you can see within 60 feet of you. As the sphere moves through the air, it opens into a tangle of metal bands.\n\nMake a ranged attack roll with an attack bonus equal to your Dexterity modifier plus your proficiency bonus. On a hit, the target is restrained until you take a bonus action to speak the command word again to release it. Doing so, or missing with the attack, causes the bands to contract and become a sphere once more.\n\nA creature, including the one restrained, can use an action to make a DC 20 Strength check to break the iron bands. On a success, the item is destroyed, and the restrained creature is freed. If the check fails, any further attempts made by that creature automatically fail until 24 hours have elapsed."'
else:
    cc_use = 0
    return_string = f' -f "Iron Bands of Binding have already been used|Once the bands are used, they can\'t be used again until the next dawn." '
cc_current = character().cc_str(cc_name)
return_string += f' -f "{cc_name} (-{cc_use})| {cc_current}|inline" '
return return_string
</drac2>