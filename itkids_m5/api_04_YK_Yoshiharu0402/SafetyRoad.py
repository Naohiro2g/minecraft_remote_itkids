from mcje.minecraft import Minecraft
import param_MCJE1122 as param
import time

mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat('demo3')

from MyApi import make_blocks
make_blocks(2,1,1,1,param.COBBLESTONE,1)