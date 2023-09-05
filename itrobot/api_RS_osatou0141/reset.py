from mcje.minecraft import Minecraft
import param_MCJE as param

mc = Minecraft.create(port=param.PORT_MC)


def reset(x=0, y=63, z=0):
    mc = Minecraft.create(port=param.PORT_MC)
    mc.postToChat('reset field')
    mc.setBlocks(x - 35, y, z - 35, x + 65, y + 100, z + 65, param.AIR)
    mc.setBlocks(x - 35, y - 1, z - 35, x + 65, y - 1, z + 65, param.GRASS_BLOCK)
    mc.postToChat('finish')


reset()
