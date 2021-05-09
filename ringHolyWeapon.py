!alias rhw tembed
<drac2>
cc_request = 5
ability_name = "Holy Weapon"
cc_name = "Ring of Spell Storing"
cc_value = character().get_cc(cc_name)
return_string = ""
if cc_value < cc_request:
    cc_use = 0
    return_string = (
        f' -title "{name} fails to cast {ability_name} from their {cc_name}!" '
        f' -desc "Not enough {cc_name} charges. Perhaps {ability_name} is not stored in their {cc_name}. " '
        )
else:
    cc_use = cc_request
    character().mod_cc(cc_name, -cc_request)
    return_string = (
        f' -title "{name} casts {ability_name} from their {cc_name}!" '
        f' -desc "You imbue a weapon you touch with holy power. Until the spell ends, the weapon emits bright light in a 30-foot radius and dim light for an additional 30 feet. In addition, weapon attacks made with it deal an extra 2d8 radiant damage on a hit. If the weapon isn''t already a magic weapon, it becomes one for the duration..." '
        )
cc_current = cc_str(cc_name)
return_string += (
    f'-f "{cc_name} (-{cc_use})| {cc_current}|inline" '
    f'-footer "{ctx.prefix}{ctx.alias}"'
    )
return return_string
</drac2>