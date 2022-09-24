<drac2>
# !alias rmt 
spells={"Invisibility": 2, "Lightning Bolt": 5, "Telekinesis": 5, "Web": 2, "Enlarge/Reduce": 0}

# create the cc
cc='Reduced Magi Tool'
ch=character()

# parse arguments
alias=ctx.prefix+ctx.alias
syntax=f'{alias} "<spell>" [cast arguments][-i]'
a=&ARGS&
if not a or a[0].lower() in ['?','help']:
  return f'echo Use: {syntax}. Charges: {ch.cc_str(cc)}\nSupported spells: {", ".join(spells.keys())}.'
cast_args="""&*&"""

# match the spell name
spell=a[0]
match=[sn for sn in spells.keys() if spell.lower() in sn.lower()]
if not match:
  return f'echo Use: {syntax}. Charges: {ch.cc_str(cc)}\nSupported spells: {", ".join(spells.keys())}.\nCase insensitive and partial name is supported.'
if len(match)>1:
  return f'echo Multiple spells match {spell}: {", ".join(match)}.'
match=match[0]
cost=spells[match]

# set level for casting
if match.lower()=="lightning bolt":
  lvl_phrase = f'-l 5 -phrase "Cast at level 5 with their {cc}"'
else:
  lvl_phrase = f'-phrase "Cast with their {cc}"'

# no charges used
if argparse(a).last('i') or cost==0:
  fields=f'-f  "{cc}|{ch.cc_str(cc)} No charges used|inline" '
else:
  # remove the charges
  if cost>ch.get_cc(cc):
    return f'echo Not enough charges [{cost}] on your {cc} to cast {match} : {ch.cc_str(cc)}'
  remaining = ch.mod_cc(cc,-cost)
  fields=f''' -f "{cc} (-{cost})|{ch.cc_str(cc)}|inline" '''

#output alias
return f'cast "{match}" {lvl_phrase} {cast_args} -i {fields}'
</drac2>