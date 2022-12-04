from mcje.minecraft import Minecraft
import param_MCJE as param

def make_outkaidan(mc,x=48,y=1,z=-5,outkaidanblock=param.GLASS):
    blocktipe_outkaidan=outkaidanblock
    use_y=y
    for j in range(5):
        use_x=x
        use_z=z
        for i in range(10):
            mc.setBlocks(-use_x,use_y,use_z,-(use_x - 4),use_y + 1,use_z - 3,blocktipe_outkaidan)
            use_y += 1
            use_z -= 4

        for i in range(10):
            mc.setBlocks(-use_x,use_y,use_z,-(use_x - 4),use_y + 1,use_z - 3,blocktipe_outkaidan)
            use_y += 1
            use_x -= 5

def make_insidekaidan_seihoukei_zyouhen(mc,x= -3,y=1,z= -3,dansu=6,insideblock_seihoukei_zyouhen=param.SEA_LANTERN_BLOCK):
    blocktipe_insideblock_seihoukei_zyouhen = insideblock_seihoukei_zyouhen
    use_x = x
    use_y = y
    use_z = z
    for i in range(dansu):
            mc.setBlock(use_x, use_y, use_z, blocktipe_insideblock_seihoukei_zyouhen)
            use_x += 1
            use_y += 1

def make_insidekaidan_seihoukei_migi(mc,x=3,y=7,z= -3,dansu=6,insideblock_seihoukei_migi=param.SEA_LANTERN_BLOCK):
    blocktipe_insideblock_seihoukei_migi = insideblock_seihoukei_migi
    use_x = x
    use_y = y
    use_z = z
    for i in range(dansu):
            mc.setBlock(use_x, use_y, use_z, blocktipe_insideblock_seihoukei_migi)
            use_z += 1
            use_y += 1

def make_insidekaidan_seihoukei_kahen(mc,x=3,y=13,z=3,dansu=6,insideblock_seihoukei_kahen=param.SEA_LANTERN_BLOCK):
    blocktipe_insideblock_seihoukei_kahen = insideblock_seihoukei_kahen
    use_x = x
    use_y = y
    use_z = z
    for i in range(dansu):
            mc.setBlock(use_x, use_y, use_z, blocktipe_insideblock_seihoukei_kahen)
            use_x -= 1
            use_y += 1

def make_insidekaidan_seihoukei_hidari(mc,x=-3,y=1,z=3,dansu=6,insideblock_seihoukei_hidari=param.SEA_LANTERN_BLOCK):
    blocktipe_insideblock_seihoukei_kahen = insideblock_seihoukei_hidari
    use_x = x
    use_y = y
    use_z = z
    for i in range(dansu):
            mc.setBlock(use_x, use_y, use_z, blocktipe_insideblock_seihoukei_kahen)
            use_z -= 1
            use_y += 1