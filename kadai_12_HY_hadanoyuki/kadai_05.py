from mcje.minecraft import Minecraft
import param_MCJE as param
from time import sleep

mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat('kadai #5  bar on the ground')

x = 0
z = 5
y = param.Y_SEA + 1
for _i in range(10):
    mc.setBlock(x, y, z,  param.DIAMOND_BLOCK)
    sleep(0.25)
    z += 1
