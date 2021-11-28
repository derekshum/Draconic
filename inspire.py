!alias inspire tembed
<drac2>
cc_request = 1
for input in &ARGS&:
   input = input.lower()
   length = len(input)
   if input.isnumeric():
       cc_request = int(input)
cc_name = "Bardic Inspiration"
cc_value = character().get_cc(cc_name)
return_string = ""
if cc_value >= cc_request:
    cc_use = cc_request
    character().mod_cc(cc_name, -cc_use)
    return_string = (
        f' -title "{name} inspires!" '
        f' -desc "You can inspire others through stirring words or music. To do so, you use a bonus action on your turn to choose one creature other than yourself within 60 feet of you who can hear you. That creature gains one Bardic Inspiration die, a **d{str(6 + 2 * int (BardLevel / 5))}**.\n\nOnce within the next 10 minutes, the creature can roll the die and add the number rolled to one ability check, attack roll, or saving throw it makes. The creature can wait until after it rolls the d20 before deciding to use the Bardic Inspiration die, but must decide before the DM says whether the roll succeeds or fails. Once the Bardic Inspiration die is rolled, it is lost. A creature can have only one Bardic Inspiration die at a time." '
        )
else:
    cc_use = 0
    return_string = (
        f' -title "{name} cannot mechanically inspire!" '
        f' -desc "No {cc_name} remaining." '
        )
cc_current = cc_str(cc_name)
return_string += (
    f' -f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    f' -footer "{ctx.prefix}{ctx.alias} [uses]" '
    )
return return_string
</drac2>