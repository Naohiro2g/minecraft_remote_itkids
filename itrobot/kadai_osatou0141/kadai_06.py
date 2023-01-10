from mcje.minecraft import Minecraft
import param_MCJE as param

from time import sleep

mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat("kadai6")

x = 10
y = 63
z = 5

param.GLASS = "1"
param.SEA_LANTERN_BLOCK = "2"


for n in range(8):
    for i in range(10):
        mc.setBlock(x, y, z, param.SEA_LANTERN_BLOCK)
        sleep(0.1)
        z += 1
    sleep(0.1)
    x += 1
    z = 5