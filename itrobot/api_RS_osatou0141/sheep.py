from mcje.minecraft import Minecraft
import param_MCJE as param

mc = Minecraft.create(port=param.PORT_MC)


def leg(x, y, z):
    mc.setBlocks(x, y, z, x + 7, y + 1, z + 7, param.BROWN_TERRACOTTA)
    mc.setBlocks(x + 2, y, z + 2, x + 7, y + 1, z + 5, param.WHITE_TERRACOTTA)
    mc.setBlocks(x, y + 2, z, x, y + 11, z + 7, param.WHITE_TERRACOTTA)
    mc.setBlocks(x, y + 2, z, x + 7, y + 11, z, param.WHITE_TERRACOTTA)
    mc.setBlocks(x + 7, y + 2, z, x + 7, y + 11, z + 7, param.WHITE_TERRACOTTA)
    mc.setBlocks(x, y + 2, z + 7, x + 7, y + 11, z + 7, param.WHITE_TERRACOTTA)
    mc.setBlocks(x - 1, y + 12, z - 1, x - 1, y + 21, z + 8, param.WHITE_WOOL)
    mc.setBlocks(x + 8, y + 12, z - 1, x + 8, y + 21, z + 8, param.WHITE_WOOL)
    mc.setBlocks(x - 1, y + 12, z - 1, x + 8, y + 21, z - 1, param.WHITE_WOOL)
    mc.setBlocks(x - 1, y + 12, z + 8, x + 8, y + 21, z + 8, param.WHITE_WOOL)


def body(x, y, z):
    mc.setBlocks(x - 6, y + 22, z - 2, x + 33, y + 22, z + 21, param.WHITE_WOOL)
    mc.setBlocks(x - 6, y + 39, z - 2, x + 33, y + 39, z + 21, param.WHITE_WOOL)
    mc.setBlocks(x - 6, y + 22, z - 2, x + 33, y + 39, z - 2, param.WHITE_WOOL)
    mc.setBlocks(x - 6, y + 22, z + 21, x + 33, y + 39, z + 21, param.WHITE_WOOL)
    mc.setBlocks(x - 6, y + 22, z - 2, x - 6, y + 39, z + 21, param.WHITE_WOOL)
    mc.setBlocks(x + 33, y + 22, z - 2, x + 33, y + 39, z + 21, param.WHITE_WOOL)


def head(x, y, z):
    mc.setBlocks(x + 1, y + 32, z + 3, x + 1, y + 45, z + 16, param.WHITE_WOOL)
    mc.setBlocks(x + 1, y + 32, z + 3, x - 12, y + 45, z + 3, param.WHITE_WOOL)
    mc.setBlocks(x + 1, y + 32, z + 16, x - 12, y + 45, z + 16, param.WHITE_WOOL)
    mc.setBlocks(x + 1, y + 32, z + 3, x - 12, y + 32, z + 16, param.WHITE_WOOL)
    mc.setBlocks(x + 1, y + 45, z + 3, x - 12, y + 45, z + 16, param.WHITE_WOOL)


def face(x, y, z):
    mc.setBlocks(x - 14, y + 33, z + 4, x - 13, y + 44, z + 15, param.WHITE_WOOL)
    mc.setBlocks(x - 14, y + 37, z + 4, x - 13, y + 42, z + 15, param.WHITE_TERRACOTTA)
    mc.setBlocks(x - 14, y + 33, z + 6, x - 13, y + 36, z + 13, param.WHITE_TERRACOTTA)
    mc.setBlocks(x - 14, y + 33, z + 8, x - 14, y + 36, z + 11, param.PINK_CONCRETE)
    mc.setBlocks(x - 14, y + 39, z + 4, x - 14, y + 40, z + 5, param.BLACK_CONCRETE)
    mc.setBlocks(x - 14, y + 39, z + 14, x - 14, y + 40, z + 15, param.BLACK_CONCRETE)
    mc.setBlocks(x - 14, y + 39, z + 6, x - 13, y + 40, z + 7, param.WHITE_CONCRETE)
    mc.setBlocks(x - 14, y + 39, z + 12, x - 13, y + 40, z + 13, param.WHITE_CONCRETE)


def makesheep(x=0, y=63, z=0):
    mc.postToChat('spawn sheep')
    leg(x, y, z)             # 右前足
    leg(x, y, z + 12)        # 左前足
    leg(x + 24, y, z)        # 右後足
    leg(x + 24, y, z + 12)   # 左後足
    body(x, y, z)
    head(x, y, z)
    face(x, y, z)


makesheep()
