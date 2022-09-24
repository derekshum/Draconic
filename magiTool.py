<drac2>
# !alias mt 
ab="absorb"
spells={"Conjure Elemental": 7, "Dispel Magic": 3, "Fireball": 7, "Flaming Sphere": 2, "Ice Storm": 4, "Invisibility": 2, "Knock": 2, "Lightning Bolt": 7, "Passwall": 5, "Plane Shift": 7, "Telekinesis": 5, "Wall of Fire": 4, "Web": 2, "Arcane Lock":0, "Detect Magic": 0, "Enlarge/Reduce": 0, "Light":0, "Mage Hand": 0, "Protect from Evil and Good": 0, ab: 0}

# create the cc
cc='Magi Tool'
ch=character()

# parse arguments
alias=ctx.prefix+ctx.alias
syntax=f'{alias} "<spell>" [cast arguments][-i] or {alias} absorb <amount>'
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

if match==ab:
  if len(a)>1 and a[1].strip('-+').isdigit():
    recharge = int(a[1].strip('-+'))
    ch.mod_cc(cc,recharge)
    ab_field = f''' -f "{cc} (+{recharge})|{ch.cc_str(cc)}|inline" '''
  else:
    return f'''echo A spell level is required to use the {cc} for {ab}.  {alias} "{ab}" <level absorbed>'''

# set level for casting
if match.lower()=="fireball" or match.lower()=="lightning bolt":
  lvl_phrase = f'-l 7 -phrase "Cast at level 7 with their {cc}"'
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
if match==ab:
  desc = '''-f "Spell Absorption|While holding the tool, you have advantage on saving throws against spells. In addition, you can use your reaction when another creature casts a spell that targets only you. If you do, the tool absorbs the magic of the spell, canceling its effect and gaining a number of charges equal to the absorbed spell's level. However, if doing so brings the tool's total number of charges above 50, the tool explodes as if you activated its retributive strike." '''
  return f'embed -title "{name} absorbs a spell with their {cc}!" {desc} {ab_field}'
else:
  return f'cast "{match}" {lvl_phrase} {cast_args} -i {fields}'
</drac2>