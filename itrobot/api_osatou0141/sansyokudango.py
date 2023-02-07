from mcje.minecraft import Minecraft
import param_MCJE as param
import random as rd

mc = Minecraft.create(port=param.PORT_MC)

x = 0
z = 0
y = 63

mc.setBlocks(x, y, z,  )