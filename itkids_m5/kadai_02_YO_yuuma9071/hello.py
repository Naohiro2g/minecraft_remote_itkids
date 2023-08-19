# Hello World for Minecraft Java Edition 1.16.5
# mcje, MCJE: Minecraft Java Edition
from mcje.minecraft import Minecraft
import param_MCJE as param
# import axis_flat

mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat('Hello Minecraft Java Edition 1.16.5')

# axis_flat.reset_minecraft_world(mc, width=40)
# axis_flat.clear_XYZ_axis(mc, wait=0)
# axis_flat.draw_XYZ_axis(mc, wait=0.3)

mc.setBlocks(-5, 63, 5,  -5, 127, 5,  param.GOLD_BLOCK)
