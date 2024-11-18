!alias deeem tembed
<drac2>
MIN = 0
MAX = 2000
cg = 35
ct = cg
rs = f'-footer "{ctx.prefix}{ctx.alias} [dm game xp (assumes 35)] [taken xp (if less than game xp)]" '
dn = "DM Games"
character().create_cc_nx(dn)
cn = "Experience"
character().create_cc_nx(cn)
if character().get_cc(cn) == 0:
    character().mod_cc(cn, 500)
cv = character().get_cc(cn)
a = &ARGS&
es = f' -title "Invalid input arguments" -desc "This alias only takes 0-2 integer inputs, each of which must be between {MIN} and {MAX}"'
if a:
    if len(a) > 2 or (len(a) > 1 and not a[1].lstrip('-').isdigit()) or (len(a) > 0 and not a[0].lstrip('-').isdigit()):
        rs += es
        return rs
    if len(a) > 0:
        cg = int(a[0])
        if cg < MIN or cg > MAX:
            rs += es
            return rs
    if len(a) > 1:
        ct = int(a[1])
        if ct < MIN or ct > MAX:
            rs += es
            return rs
        if ct > cg or ct < 0 or cg < 0:
            rs += f' -title "Invalid input arguments" -desc "The taken xp ({ct}) must be less than the game xp ({cg}) and both must be 0 or greater."'
            return rs
    else:
        ct = cg
cp = cv + cg
df = character().mod_cc(dn, 1)
cf = character().mod_cc(cn, ct)
rs += f' -title "From DM rewards, {name} gains {ct} xp{f" from a {cg} xp game" if ct != cg else ""}{f" and levels up" if int(cf / 100) > int(cv / 100) else ""}!"'
rs += f' -f "{dn} (+1)|{df}|inline"'
rs += f' -f "Current Experience|{cf}|inline"'
g = 0
if cg > 0:
    while cv < cp:
        if cv < 900 or cf < 900:
            g += 62.5
        elif cv < 1300 or cf < 1300:
            g += 125
        elif cv < 1700 or cf < 1700:
            g += 250
        else:
            g += 500
        cv += 1
if ct != cg:
    if ct / cg < 0.4:
        g *= 0.4
    else:
        g *= ct / cg
if g != 0:
    rs += f' -f "Gold Rewards|{round(g, 2)}|inline"'
return rs    
</drac2>
