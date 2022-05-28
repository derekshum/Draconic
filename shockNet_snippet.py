!snippet snet tembed
<drac2>
num = 1
cc_name = "Shock-Nets"
cc_value = character().get_cc(cc_name)
if cc_value >= num:
    cc_use = num
    character().mod_cc(cc_name, -cc_use)
    return_string = (
        f' -d{num} 3d4[lightning] '
        f' -f "Shock|On a hit, this weapon deals 3d4 thunder damage, and the target must succeed on a **DC 10 Constitution saving throw** or be stunned until the end of its next turn. On a miss, the net returns to the thrower\'s hand." '
        )
else:
    cc_use = 0
    return_string = f' -f "No {cc_name}|CC {cc_name} is currently at 0."'
cc_current = character().cc_str(cc_name)
return_string += f' -f "{cc_name} (-{cc_use})| {cc_current}|inline"'
return return_string
</drac2>

!alias snet a net snet c20

!cc create "Shock-Nets" -min 0 -max 1 -reset long -type bubble -desc "On a hit, the net deals 3d4 thunder damage, and the target must succeed on a DC 10 Constitution saving throw or be stunned until the end of its next turn. On a miss, the net returns to the thrower's hand.

Dealing 5 slashing damage (AC10) to the shock net frees the creature without harming it, damaging the net. The net may be repaired by spending one downtime day to do so, or by casting the Mending spell. The Shock-Net otherwise follows all usual rules for nets.

Once the Shock-Net deals thunder damage to a target, the weapon loses its ability to deal thunder damage and its ability to stun a target. These properties return after the net spends at least one 1 hour inside an elemental air node."

f' -f "Net|A Large or smaller creature hit by a net is restrained until it is freed. A net has no effect on creatures that are formless, or creatures that are Huge or larger. A creature can use its action to make a DC 10 Strength check, freeing itself or another creature within its reach on a success. Dealing 5 slashing damage to the net (AC 10) also frees the creature without harming it, ending the effect and destroying the net.\n\nWhen you use an action, bonus action, or reaction to attack with a net, you can make only one attack regardless of the number of attacks you can normally make." '