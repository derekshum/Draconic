#For the Level 11 Way of the Kensei feature Sharpen the Blade

#Sharpen the Blade
#At 11th level, you gain the ability to augment your weapons further with your ki. As a bonus action, you can expend up to 3 ki points to grant one kensei weapon you touch a bonus to attack and damage rolls when you attack with it. The bonus equals the number of ki points you spent. This bonus lasts for 1 minute or until you use this feature again. This feature has no effect on a magic weapon that already has a bonus to attack and damage rolls.

!alias sharpen tembed
<drac2>
args = &ARGS& # Stores any arguments passed in a list so you can use them later
cc_name = "Ki Points"
character().create_cc_nx(cc_name, MINVALUE, MAXVALUE, RESET, DISPLAYTYPE) # reset can be either "long", "short" or "none", dispalytime is either "bubble" or None, all args except the name are optional.
cc_value = character().get_cc(cc_name)
return_string = ""

#Here we check if there are any uses left remaining
if cc_value >= 1:
    character().mod_cc(cc_name, -1) # use up one use of the CC
    cc_value = character().get_cc(cc_name) # updates the value for the changed CC

    # Add any effects the ability has here, some common examples are included here, just delete the # before them to enable them.
    # dice_roll = vroll("XdY+Z") # rolls some dice


    # Just add a new line of f'' if you want to add another field, make sure to include a space at the end. Some common examples are given.
    return_string = (
        f'-title "{name} uses ABILITY NAME!" '
        f'-f "ABILITY DESCRIPTION" '
        #f'-f "ROLL RESULT | {dice_roll.result}" ' # Displays the result of the roll
        #f'-f "DC | {character().spellbook.dc}" ' # Displays the Spell DC
        )
else:
    # put anything you want to be displayed on a failure here, same principle as above
    return_string = (
        f'-title "{name} fails to use ABILITY NAME!" '
        )

# Put anything you want to happen wether or not you have enough uses left here

remaining_uses = '◉'*cc_value + '〇'*(character().get_cc_max(cc_name)-cc_value) # this generates a string of bubbles to display how many uses are remaining
# same as above, add any fields you want always displayed in here
return_string += (
    f'-f "Remaining Uses | {remaining_uses}" '
    f'-footer "SOURCE | {"@"+"USERNAME"}" '
    f'-thumb {image} '
    )
return return_string
</drac2>