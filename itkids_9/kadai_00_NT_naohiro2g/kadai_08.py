import sys
from time import sleep

from mcje.minecraft import Minecraft
import param_MCJE as param
from param_MCJE import PLAYER_ORIGIN as po


def setPyramid(mc, x=0, z=0, size=3, y=param.Y_SEA + 1, blockTypeId=param.GOLD_BLOCK):
    while size > 0:
        mc.setBlocks(x, y, z, x + size - 1, y, z + size - 1, blockTypeId)
        x += 1
        z += 1
        size -= 2
        y += 1
        sleep(0.01)


def clearField(mc):
    """ remove blocks to make space """
    mc.setBlocks(-50, param.Y_SEA + 1, -50, 50, param.Y_SEA + 20, 50, 0)


if __name__ == "__main__":
    # Connect to minecraft and open a session as player with origin location
    mc = Minecraft.create(address=param.ADRS_MCR, port=param.PORT_MCR)
    result = mc.setPlayer(param.PLAYER_NAME, po.x, po.y, po.z)
    if ("Error" in result):
        sys.exit(result)
    else:
        print(result)


    mc.postToChat('kadai #8  pyramids ')

    # clearField()
    sleep(1)
    setPyramid(mc, x=10, z=-20, y=param.Y_SEA + 1, size=21)
    sleep(2)
    setPyramid(mc, x=-5, z=-35, size=15, blockTypeId=param.IRON_BLOCK)
