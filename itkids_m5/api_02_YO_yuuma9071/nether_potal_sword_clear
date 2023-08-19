#ネザーゲートを壊す。

from mcje.minecraft import Minecraft
import param_MCJE as param
from time import sleep

mc = Minecraft.create(port=param.PORT_MC)
sleep(1)

mc.postToChat('ネザーゲートを破壊します。')
sleep(2)

y = param.Y_SEA + 1
for _n in range(9):
    x = 1
    for _n in range(9):
        z = 18
        for _i in range(11):
            mc.setBlock(x, y, z,  param.QUARTZ_BLOCK)
            sleep(0.05)
            z += 1
        x += 1
    y += 1
