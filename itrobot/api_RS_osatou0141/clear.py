from mcje.minecraft import Minecraft
import param_MCJE as param

mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat('Will all clear after this !')
mc.postToChat('And, make a GLASS field !')

mc.setBlocks(-80, 63, -80,   80, 128, 80,   param.AIR)
mc.setBlocks(-80, 62, -80,   80, 62, 80,   param.GRASS_BLOCK)

mc.postToChat('Finish Now !!')