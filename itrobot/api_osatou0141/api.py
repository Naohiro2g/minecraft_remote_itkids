from mcje.minecraft import Minecraft
import param_MCJE as param

mc = Minecraft.create(port=param.PORT_MC)

X = 0
Z = 0
Y = 63


def createsheepleg(x=X, y=Y, z=Z):
    mc.setBlocks(x, y, z, x + 8, y + 1, z + 8, param.BROWN_TERRACOTTA)
    mc.setBlocks(x + 2, y, z + 2, x + 8, y + 1, z + 6, param.WHITE_TERRACOTTA)


createsheepleg(x=X, y=Y, z=Z)
