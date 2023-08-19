from mcje.minecraft import Minecraft
import param_MCJE1122 as param
import time

mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat('demo3')

from MyApi import make_blocks
make_blocks(0,1,0,0,param.GOLD_BLOCK,1)