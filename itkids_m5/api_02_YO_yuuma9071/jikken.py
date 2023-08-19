from mcje.minecraft import Minecraft
import param_MCJE as param
from time import sleep

mc = Minecraft.create(port=param.PORT_MC)
sleep(1)

x, y, z = mc.player.getPos()
mc.setBlock(x, y + 2, z, param.DIAMOND_BLOCK)
