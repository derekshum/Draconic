!snippet fob {{cc="Ki Points"}}
{{c=get_cc(cc)}}
{{' -rr 2' if c else ''}}
{{mod_cc(cc, -1) if c else ''}} -f "{{f'Flurry of Blows|Immediately after you take the Attack action on your turn, you can spend 1 ki point to make two unarmed strikes as a bonus action.\n\n**{cc} (-1)** {cc_str(cc)}' if c else f'Not enough {cc} for Flurry of Blows.\n\n**{cc}** {cc_str(cc)}'}}"