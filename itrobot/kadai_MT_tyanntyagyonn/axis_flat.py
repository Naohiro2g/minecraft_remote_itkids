"""
Draw x, y, z axis in the Minecraft world
    x: stone
    y: grass/dirt
    z: gold
Flatten the world
    width: Size of flat world to produce.
           x, z: from -widh to width
           y: from AXIS_BOTTOM to AXIS_TOP

mc: an instance of Minecraft must be created beforehand
"""

from mcje.minecraft import Minecraft
import param_MCJE as param

from time import sleep


def draw_XYZ_axis(mc, wait=0.1):
    """
    Draw xyz axis with some wait between placing each block.
    You must create mc or instance of Minecraft world beforehand.
    """
    blockTypeIdX = param.DIAMOND_BLOCK
    blockTypeIdY = param.SEA_LANTERN_BLOCK
    blockTypeIdZ = param.GOLD_BLOCK
    BLOCK_TOP_LIGHT = param.GLOWSTONE

    # x-axis
    mc.postToChat("x-axis from negative to positive region")
    x, y, z = -param.AXIS_WIDTH, param.AXIS_Y_V_ORG, 0
    while x <= param.AXIS_WIDTH:
        mc.setBlock(x, y, z, blockTypeIdX)
        if x < 0:
            x += 2
            sleep(wait * 2)
        else:
            x += 1
            sleep(wait)
    # y-axis
    mc.postToChat("y-axis from negative to positive region")
    x, y, z = 0, param.AXIS_BOTTOM, 0
    while y <= param.AXIS_TOP - 5:
        mc.setBlock(x, y, z, blockTypeIdY)
        if y < param.AXIS_Y_V_ORG:
            y += 2
            sleep(wait * 2)
        else:
            y += 1
            sleep(wait)
    while y <= param.AXIS_TOP:
        mc.setBlock(x, y, z, BLOCK_TOP_LIGHT)
        y += 1
        sleep(wait)
    # z-axis
    mc.postToChat("z-axis from negative to positive region")
    x, y, z = 0, param.AXIS_Y_V_ORG, -param.AXIS_WIDTH
    while z <= param.AXIS_WIDTH:
        mc.setBlock(x, y, z, blockTypeIdZ)
        if z < 0:
            z += 2
            sleep(wait * 2)
        else:
            z += 1
            sleep(wait)


def clear_XYZ_axis(mc, wait=0.5):
    mc.setBlocks(-param.AXIS_WIDTH, param.AXIS_Y_V_ORG, 0,   param.AXIS_WIDTH, param.AXIS_Y_V_ORG, 0,   param.AIR)  # x
    sleep(wait)
    mc.setBlocks(0, 0, 0,   0, param.AXIS_TOP, 0,   param.AIR)  # y
    sleep(wait)
    mc.setBlocks(0, param.AXIS_Y_V_ORG, -param.AXIS_WIDTH,   0, param.AXIS_Y_V_ORG, param.AXIS_WIDTH,   param.AIR)  # z
    sleep(wait)


def reset_minecraft_world(mc, width=80):
    mc.setBlocks(-width, param.Y_SEA + 1, -width,   width, param.AXIS_TOP,    width,    param.AIR)
    mc.setBlocks(-width, param.Y_SEA,     -width,   width, param.Y_SEA,       width,    param.GRASS_BLOCK)


if __name__ == "__main__":
    mc = Minecraft.create(port=param.PORT_MC)

    mc.postToChat("axis_flat module main part")

    reset_minecraft_world(mc, width=40)
    # draw_XYZ_axis(mc, wait=0.2)
    # clear_XYZ_axis(mc, wait=0)
    draw_XYZ_axis(mc, wait=0.2)
