from mcje.minecraft import Minecraft
import param_MCJE as param


class reset:
    mc = Minecraft.create(port=param.PORT_MC)
    mc.postToChat('clear and make pallete')
    mc.setBlocks(-50, 62, -50,   50, 150, 50,   param.AIR)
    mc.setBlocks(-50, 62, -50,   50, 62, 50,   param.GRASS_BLOCK)
    mc.postToChat('finish')
