from mcje.minecraft import Minecraft
import param_MCJE as param

mc = Minecraft.create(port=param.PORT_MC)


def leg(x, y, z):
    mc.setBlocks(x + 15, y, z + 3, x + 22, y + 1, z + 10, param.BROWN_TERRACOTTA)
    mc.setBlocks(x + 17, y, z + 5, x + 22, y + 1, z + 8, param.WHITE_TERRACOTTA)
    mc.setBlocks(x + 15, y + 2, z + 3, x + 22, y + 11, z + 10, param.WHITE_TERRACOTTA)
    mc.setBlocks(x + 14, y + 12, z + 2, x + 23, y + 21, z + 11, param.WHITE_WOOL)


def body(x, y, z):
    mc.setBlocks(x + 9, y + 22, z + 1, x + 48, y + 39, z + 24, param.WHITE_WOOL)


def head(x, y, z):
    mc.setBlocks(x + 16, y + 32, z + 6, x + 3, y + 45, z + 19, param.WHITE_WOOL)
    mc.setBlocks(x + 1, y + 33, z + 7, x + 2, y + 44, z + 18, param.WHITE_WOOL)


def face(x, y, z):
    mc.setBlocks(x + 1, y + 37, z + 7, x + 2, y + 42, z + 18, param.WHITE_TERRACOTTA)
    mc.setBlocks(x + 1, y + 33, z + 9, x + 2, y + 36, z + 16, param.WHITE_TERRACOTTA)
    mc.setBlocks(x + 1, y + 33, z + 11, x + 1, y + 36, z + 14, param.PINK_CONCRETE)
    mc.setBlocks(x + 1, y + 39, z + 7, x + 1, y + 40, z + 8, param.BLACK_CONCRETE)
    mc.setBlocks(x + 1, y + 39, z + 17, x + 1, y + 40, z + 18, param.BLACK_CONCRETE)
    mc.setBlocks(x + 1, y + 39, z + 9, x + 2, y + 40, z + 10, param.WHITE_CONCRETE)
    mc.setBlocks(x + 1, y + 39, z + 15, x + 2, y + 40, z + 16, param.WHITE_CONCRETE)


def makesheep(x=0, y=64, z=0):
    mc.postToChat('spawn sheep')
    leg(x, y, z)            # 右前足
    leg(x, y, z + 12)        # 左前足
    leg(x + 24, y, z)        # 右後足
    leg(x + 24, y, z + 12)  # 左後足
    body(x, y, z)
    head(x, y, z)
    face(x, y, z)


makesheep()
