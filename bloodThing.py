!alias blood tembed
<drac2>
cc_request = 1
for input in &ARGS&:
   input = input.lower()
   length = len(input)
   if input.isnumeric():
       cc_request = int(input)
ability_name = "blood magic"
cc_name_1 = ability_name
cc_name_2 = "Sorcery Points"
return_string = ""

cc_1_boost = 2 * cc_request
cc_2_boost = cc_request
damage = 2 * cc_request

former_hp = character().hp

character().mod_cc(cc_name_1, cc_1_boost)
character().mod_cc(cc_name_2, cc_2_boost)
character().modify_hp(-damage)

cc_current_1 = character().cc_str(cc_name_1)
cc_current_2 = character().cc_str(cc_name_2)

return_string += (
    f' -title "{name} uses {ability_name}!" '
    f' -desc "Starting at 1st level, you can expend your hit points in place of Sorcery Points by spending two hit points for each Sorcery Point you would have spent. Both your current hit points and maximum hit points are reduced by the number of hit points you spend. This hit point reduction cannot be lessened in any way, and the reduction to your hit point maximum lasts until the end of your next long rest. You cannot spend more hit points each day than indicated on the Blood Magic Table." '
    f' -f "HP|{str(former_hp)} - {str(damage)} = {str(character().hp)}/{str(character().max_hp)}|inline" '
    f' -f "{cc_name_1} ({cc_1_boost})| {cc_current_1}|inline" '
    f' -f "{cc_name_2} ({cc_2_boost})| {cc_current_2}|inline" '
    f' -footer "{ctx.prefix}{ctx.alias} " '
    )
return return_string
</drac2>