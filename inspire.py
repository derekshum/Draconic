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
cc_current = character().cc_str(cc_name)
return_string += (
    f' -f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    f' -footer "{ctx.prefix}{ctx.alias} [uses]" '
    )
return return_string
</drac2>

tembed
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
    r = vroll("d19").total
    match r:
        case 1:
            q = "Nobody can make you feel inferior without your permission."
        case 2:
            q = "You can never plan the future by the past."
        case 3:
            q = "Those who have a why to live can bear almost any how."
        case 4:
            q = "Take into account that great love and great achievements involve great risk."
        case 5:
            q = "Lost time is never found again."
        case 6:
            q = "Those that respect themselves are safe from others."
        case 7:
            q = "Common sense is genius dressed in its working clothes."
        case 8:
            q = "In three words I can sum up everything I’ve learned about life: it goes on."
        case 9:
            q = "It is the province of knowledge to speak, and it is the privilege of wisdom to listen."
        case 10:
            q = "Don’t take life too seriously. You’ll never get out of it alive."
        case 11:
            q = "If you talk to a person in a language they understand, that goes to their head. If you talk to them in their language, that goes to their heart."
        case 12:
            q = "Nothing that you have not given away will ever be really yours."
        case 13:
            q = "Singleness of purpose is one of the chief essentials for success in life, no matter what may be one’s aim."
        case 14:
            q = "The two most important days in your life are the day you are born and the day you find out why."
        case 15:
            q = "Educating the mind without educating the heart is no education at all."
        case 16:
            q = "There are many ways of going forward, but only one way of standing still."
        case 17:
            q = "When a thing is done, it’s done. Don’t look back. Look forward to your next objective."
        case 18:
            q = "Use what talents you possess; the woods would be very silent if no birds sang there except those that sang best."
        case 19:
            q = "In the end, it’s not the years in your life that count. It’s the life in your years."
    return_string = (
        f' -title "{name} inspires!" '
        f' -desc "You can inspire others through stirring words or music. To do so, you use a bonus action on your turn to choose one creature other than yourself within 60 feet of you who can hear you. That creature gains one Bardic Inspiration die, a **d{str(6 + 2 * int (BardLevel / 5))}**.\n\nOnce within the next 10 minutes, the creature can roll the die and add the number rolled to one ability check, attack roll, or saving throw it makes. The creature can wait until after it rolls the d20 before deciding to use the Bardic Inspiration die, but must decide before the DM says whether the roll succeeds or fails. Once the Bardic Inspiration die is rolled, it is lost. A creature can have only one Bardic Inspiration die at a time." '
        f' -f "{name} says|\"{q}\"|inline" '
        )
else:
    cc_use = 0
    return_string = (
        f' -title "{name} cannot mechanically inspire!" '
        f' -desc "No {cc_name} remaining." '
        )
cc_current = character().cc_str(cc_name)
return_string += (
    f' -f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    f' -footer "{ctx.prefix}{ctx.alias} [uses]" '
    )
return return_string
</drac2>