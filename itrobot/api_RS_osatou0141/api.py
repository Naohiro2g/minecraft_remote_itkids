from mcje.minecraft import Minecraft
import param_MCJE as param

mc = Minecraft.create(port=param.PORT_MC)

stertX = 0
stertZ = 0


def createsheepleg(x=0, y=0, z=0):
    mc.setBlocks(x, y, z, x + 7, y + 1, z + 7, param.BROWN_TERRACOTTA)
    mc.setBlocks(x + 2, y, z + 2, x + 7, y + 1, z + 5, param.WHITE_TERRACOTTA)
    mc.setBlocks(x, y + 2, z, x + 7, y + 11, z + 7, param.WHITE_TERRACOTTA)
    mc.setBlocks(x - 1, y + 12, z - 1, x + 8, y + 21, z + 8, param.WHITE_WOOL)


createsheepleg(x=stertX, y=63, z=stertZ)
createsheepleg(x=stertX, y=63, z=stertZ + 12)
createsheepleg(x=stertX + 24, y=63, z=stertZ)
createsheepleg(x=stertX + 24, y=63, z=stertZ + 12)
