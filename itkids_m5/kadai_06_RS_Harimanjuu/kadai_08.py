from mcje.minecraft import Minecraft
import param_MCJE as param
from time import sleep

mc = Minecraft.create(port=param.PORT_MC)


def setPyramid(mc=mc, x=0, z=0, size=3, y=param.Y_SEA + 1, blockTypeId=param.GOLD_BLOCK):
    while size > 0:
        mc.setBlocks(x, y, z, x + size - 1, y, z + size - 1, blockTypeId)
        x += 1
        z += 1
        size -= 2
        y += 1
        sleep(0.01)


def clearField(mc=mc):
    """ remove blocks to make space """
    mc.setBlocks(-50, param.Y_SEA + 1, -50, 50, param.Y_SEA + 20, 50, 0)


if __name__ == "__main__":
    mc = Minecraft.create(port=param.PORT_MC)
    mc.postToChat('kadai #8  pyramids ')

    # clearField()
    sleep(1)
    setPyramid(x=10, z=-20, y=param.Y_SEA + 1, size=21)
    sleep(2)
    setPyramid(x=-5, z=-35, size=15, blockTypeId=param.IRON_BLOCK)
