from mcje.minecraft import Minecraft
import param_MCJE as param
from time import sleep

mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat('kadai #7  wall ')

x = -30
y = param.Y_SEA + 1
for _n in range(8):
    z = 25
    for _i in range(20):
        mc.setBlock(x, y, z,  param.GLOWSTONE)
        sleep(0.1)
        z -= 1
    y += 1

sleep(2)
mc.postToChat('kadai #7  stairs')
sleep(1)

z = -5
y = param.Y_SEA + 1
for _n in range(5):
    x = -30
    for _i in range(16):
        mc.setBlock(x, y, z,  param.GRASS_BLOCK)
        sleep(0.2)
        x += 1
    z -= 1
    y += 1
