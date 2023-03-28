from mcje.minecraft import Minecraft
import param_MCJE as param


def reset(x=0, y=63, z=0):
    mc = Minecraft.create(port=param.PORT_MC)
    mc.postToChat('clear and make pallete')
    mc.setBlocks(x - 50, y, z - 50,   x + 50, y + 87, z + 50,   param.AIR)
    mc.setBlocks(x - 50, y - 1, z - 50,   x + 50, y - 1, z + 50,   param.GRASS_BLOCK)
    mc.postToChat('finish')
