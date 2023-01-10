from mcje.minecraft import Minecraft
import param_MCJE as param

from time import sleep

mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat("kadai2")

x = 5
z = 10
y = 63

for n in range(10):
    mc.setBlock(x, y, z, param.GOLD_BLOCK)
    sleep(0.1)
    y += 1
