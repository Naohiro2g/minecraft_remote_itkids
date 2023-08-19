from mcje.minecraft import Minecraft
import param_MCJE1122 as param
import time

mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat('Ice Boat')

from MyApi import make_blocks
make_blocks(0,1,0,0,param.ICE,1)