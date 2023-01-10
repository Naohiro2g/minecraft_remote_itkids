from mcje.minecraft import Minecraft
import param_MCJE as param
from time import sleep

mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat('kadai #6  floor')

x = -10
y = param.Y_SEA + 1
for _n in range(8):
    z = 5
    for _i in range(10):
        mc.setBlock(x, y, z,  param.SEA_LANTERN_BLOCK)
        sleep(0.25)
        z += 1
    x += 1
