#!alias sop 

<drac2>
ab="absorb"
spells={"Cone of Cold": 5,"Fireball": 5,"Globe of Invulnerability": 6,"Hold Monster": 5,"Levitate": 2,"Lightning Bolt": 5,"Magic Missile": 1,"Ray of Enfeeblement": 2,"Wall of Force": 5}

# create the cc
cc='Shard of Power'
ch=character()
# ch.create_cc_nx(cc, 0, 20)

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
if match.lower()=="fireball" or match.lower()=="lightning bolt":
  lvl_phrase = f'-l 5 -phrase "at level 5 with their {cc}!"'
else:
  lvl_phrase = f'-phrase "with their {cc}!"'

# remove the charges
if cost>ch.get_cc(cc):
    return f'echo Not enough charges [{cost}] on your {cc} to cast {match} : {ch.cc_str(cc)}'
    
remaining = ch.mod_cc(cc,-cost)
fields=f''' -f "{cc} (-{cost})|{ch.cc_str(cc)}|inline" '''

#output alias
return f'cast "{match}" {lvl_phrase} {cast_args} -i {fields}'
</drac2>