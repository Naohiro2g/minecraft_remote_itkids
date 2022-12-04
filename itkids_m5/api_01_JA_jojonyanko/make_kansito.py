from mcje.minecraft import Minecraft
import param_MCJE as param

def make_kannsito(mc, x=28, z=28, y=76, sityuublock=param.GLOWSTONE, kahenblock=param.GLOWSTONE, zyouhenblock=param.GLOWSTONE ):

    blocktipe_sityu = sityuublock
    blocktipe_kahen = kahenblock
    blocktipe_zyouhen = zyouhenblock
    kudow = param.AIR

    mc.setBlocks(x,1,z,x - 12,y-1,z - 12, blocktipe_sityu)
    mc.setBlocks(x + 1,y,z + 1,x - 13,y,z - 13, blocktipe_kahen)
    mc.setBlocks(x,y,z,x - 12,y,z - 12, kudow)
    mc.setBlocks(x + 2,y+1,z + 2,x - 14,y+1,z - 14, blocktipe_kahen)
    mc.setBlocks(x + 1,y+1,z + 1,x - 13,y+1,z - 13, kudow)
    mc.setBlocks(x + 2,y+4,z + 2,x - 14,y+4,z - 14, blocktipe_zyouhen)
    mc.setBlocks(x + 1,y+4,z  + 1,x - 13,y+4,z - 13, kudow)
    mc.setBlocks(x + 1,y+5,z + 1,x - 13,y+5,z - 13, blocktipe_zyouhen)
    mc.setBlocks(x,y+5,z,x - 12,y+5,z - 12, kudow)
    mc.setBlocks(x,y+6,z,x - 12,y+6,z - 12, blocktipe_zyouhen)

def make_honto(mc,x= 10,y=100,z= 10,tyusinblock=param.GOLD_BLOCK):
    blocktipe_tyuusin = tyusinblock

    mc.setBlocks(x,1,z,-x,y,-z,param.GLASS)
    mc.setBlocks(x-1,1,z-1,-(x-1),y-1,-(z-1),blocktipe_tyuusin)

def make_kaidow(mc,x=49,y=1,z=4,y_plas=20,kaidowblock=param.GLASS):
    blocktipe_kaidow=kaidowblock
    for i in range(6):
        
        mc.setBlocks(x, y ,-z,-x,y + 7,z,blocktipe_kaidow)
        mc.setBlocks(x, y + 1 ,-(z - 2),-x,y + 6,z - 2,param.AIR)

        mc.setBlocks(-z, y ,x,z,y + 7,-x,blocktipe_kaidow)
        mc.setBlocks(-(z - 2), y + 1 ,x,z - 2,y + 6,-x,param.AIR)
        mc.setBlocks(x, y + 1 ,-(z - 2),-x,y + 6,z - 2,param.AIR)

        y += y_plas