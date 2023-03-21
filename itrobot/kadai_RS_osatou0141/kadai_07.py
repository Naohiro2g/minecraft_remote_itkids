from mcje.minecraft import Minecraft
import param_MCJE as param
import random as rd

mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat("kadai7")
