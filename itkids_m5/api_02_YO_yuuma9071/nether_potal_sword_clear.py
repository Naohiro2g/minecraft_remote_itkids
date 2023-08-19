#ネザーゲートを壊す。

from mcje.minecraft import Minecraft
import param_MCJE as param
from time import sleep

mc = Minecraft.create(port=param.PORT_MC)
sleep(1)

mc.postToChat('ネザーゲートを破壊します。')
sleep(2)

y = param.Y_SEA + 1
for _n in range(31):
    x = 1
    for _n in range(9):
        z = 7
        for _i in range(13):
            mc.setBlock(x, y, z,  param.GLOWSTONE)
            sleep(0.005)
            z += 1
        x += 1
    y += 1

sleep(1)

y = param.Y_NETHER + 11
for _n in range(31):
    x = 0
    for _n in range(9):
        z = 7
        for _i in range(13):
            mc.setBlock(x, y, z,  param.AIR)
            sleep(0.005)
            z += 1
        x += 1
    y -= 1
