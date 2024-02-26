!alias shards tembed
<drac2>
return_string = (
    f' -title "{name} uses Chaotic and Evil Shards!"'
    f' -desc "When you use a Metamagic option on a spell while you are holding or wearing the shard, you can use this property.\n\n**Chaotic.** Choose one creature who takes damage from the spell. That target has disadvantage on attack rolls and ability checks made before the start of your next turn.\n\n**Evil.** Choose one creature who takes damage from the spell. That target takes an extra {vroll("3d6")} necrotic damage."'
    f' -footer "{ctx.prefix}{ctx.alias}"'
    )
return return_string
</drac2>