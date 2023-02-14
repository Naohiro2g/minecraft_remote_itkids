from mcje.minecraft import Minecraft
import param_MCJE as param

from time import sleep

mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat("kadai5")

x = 0
z = 5
y = 63

for n in range(10):
    mc.setBlock(x, y, z, param.DIAMOND_BLOCK)
    sleep(0.1)
    z += 1
