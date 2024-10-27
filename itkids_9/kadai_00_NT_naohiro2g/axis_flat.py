import sys
from time import sleep

import param_MCJE as param
from mcje.minecraft import Minecraft
from param_MCJE import PLAYER_ORIGIN as po

# axis parameters
AXIS_BLOCK_X = param.DIAMOND_BLOCK
AXIS_BLOCK_Y = param.SEA_LANTERN_BLOCK
AXIS_BLOCK_Z = param.GOLD_BLOCK
AXIS_BLOCK_TOP = param.GLOWSTONE

def draw_XYZ_axis(mc, wait=0.5):
    mc.postToChat("Drawing x-axis from negative to positive region")
    for x in range(-param.AXIS_WIDTH, param.AXIS_WIDTH + 1):
        block_type = AXIS_BLOCK_X if x >= 0 else (param.AIR if x % 2 == 0 else AXIS_BLOCK_X)
        mc.setBlock(x, param.AXIS_Y_V_ORG, 0, block_type)
        sleep(wait)

    mc.postToChat("Drawing y-axis from bottom to top")
    for y in range(param.AXIS_BOTTOM, param.AXIS_TOP + 1):
        block_type = AXIS_BLOCK_Y if y >= param.AXIS_Y_V_ORG else (param.AIR if y % 2 == 0 else AXIS_BLOCK_Y)
        mc.setBlock(0, y, 0, block_type)
        sleep(wait)

    mc.postToChat("Drawing z-axis from negative to positive region")
    for z in range(-param.AXIS_WIDTH, param.AXIS_WIDTH + 1):
        block_type = AXIS_BLOCK_Z if z >= 0 else (param.AIR if z % 2 == 0 else AXIS_BLOCK_Z)
        mc.setBlock(0, param.AXIS_Y_V_ORG, z, block_type)
        sleep(wait)

def clear_XYZ_axis(mc, wait=0.5):
    mc.postToChat("Clearing x-axis from negative to positive region")
    for x in range(-param.AXIS_WIDTH, param.AXIS_WIDTH + 1):
        mc.setBlock(x, param.air, 0, debug=True)
        sleep(wait)

    mc.postToChat("Clearing y-axis from bottom to top")
    for y in range(param.AXIS_BOTTOM, param.AXIS_TOP + 1):
        mc.setBlock(x, param.air, 0, debug=True)
        sleep(wait)

    mc.postToChat("Clearing z-axis from negative to positive region")
    for z in range(-param.AXIS_WIDTH, param.AXIS_WIDTH + 1):
        mc.setBlock(x, param.air, 0, debug=True)
        sleep(wait)

def reset_minecraft_world(mc, width=48):
    mc.setBlocks(-width, param.Y_SEA + 1, -width, width, param.AXIS_TOP, width, param.AIR)
    sleep(1)
    mc.setBlocks(-width, param.Y_SEA, -width, width, param.Y_SEA, width, param.GRASS_BLOCK)
    sleep(1)

if __name__ == "__main__":
    # Connect to minecraft and open a session as player with origin location
    mc = Minecraft.create(address=param.ADRS_MCR, port=param.PORT_MCR)
    result = mc.setPlayer(param.PLAYER_NAME, po.x, po.y, po.z)
    if ("Error" in result):
        sys.exit(result)
    else:
        print(result)

    mc.postToChat("axis_flat.py")
    reset_minecraft_world(mc, width=48)
    # draw_XYZ_axis(mc)
    # clear_XYZ_axis(mc, wait=0.05)
    draw_XYZ_axis(mc, wait=0.25)
