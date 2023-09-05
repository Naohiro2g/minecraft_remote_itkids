from mcje.minecraft import Minecraft
import param_MCJE as param
import random as rd

from time import sleep

mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat("kadai6")

x = 10
y = 63
z = 5
T = 0

for n in range(8):
    for i in range(10):
        T = rd.randint(1, 3)
        if T == 1:
            mc.setBlock(x, y, z, param.SEA_LANTERN_BLOCK)
        elif T == 2:
            mc.setBlock(x, y, z, param.GLOWSTONE)
        else:
            mc.setBlock(x, y, z, param.MAGMA_BLOCK)
        sleep(0.1)
        z += 1
    sleep(0.1)
    x += 1
    z = 5
