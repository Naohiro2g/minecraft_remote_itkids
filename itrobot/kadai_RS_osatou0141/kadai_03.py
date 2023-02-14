from mcje.minecraft import Minecraft
import param_MCJE as param
import random as rd

from time import sleep

mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat("kadai3")

x = 5
z = 10
y = 63
A = rd.randint(1, 10)

for n in range(7):
    for m in range(A):
        mc.setBlock(x, y, z, param.IRON_BLOCK)
        sleep(0.1)
        y += 1
    sleep(0.1)
    y = 63
    z += 2
    A = rd.randint(1, 10)
