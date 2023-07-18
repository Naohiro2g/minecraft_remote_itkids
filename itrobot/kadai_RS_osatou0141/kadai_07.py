from mcje.minecraft import Minecraft
import param_MCJE as param
import random as rd

from time import sleep

mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat("kadai7")

head = 0
x = -26
y = 63
z = -3
kx = -15
ky = 63
kz = -10
muki = 0


def skull(x, y, z):
    mc.setBlocks(x, y, z, x, y + 7, z + 7, param.WHITE_WOOL)
    mc.setBlocks(x, y + 1, z + 1, x, y + 1, z + 6, param.GRAY_CONCRETE)
    mc.setBlocks(x, y + 3, z + 1, x, y + 3, z + 2, param.GRAY_CONCRETE)
    mc.setBlocks(x, y + 3, z + 5, x, y + 3, z + 6, param.GRAY_CONCRETE)
    mc.setBlocks(x, y + 2, z + 3, x, y + 2, z + 4, param.LIGHT_GRAY_CONCRETE)


def zombie(x, y, z):
    mc.setBlocks(x, y, z, x, y + 7, z + 7, param.GREEN_WOOL)
    mc.setBlocks(x, y + 3, z + 1, x, y + 3, z + 2, param.BLACK_CONCRETE)
    mc.setBlocks(x, y + 3, z + 5, x, y + 3, z + 6, param.BLACK_CONCRETE)


def creeper(x, y, z):
    mc.setBlocks(x, y, z, x, y + 7, z + 7, param.LIME_WOOL)
    mc.setBlocks(x, y, z + 2, x, y + 2, z + 5, param.BLACK_CONCRETE)
    mc.setBlocks(x, y, z + 3, x, y, z + 4, param.LIME_WOOL)
    mc.setBlocks(x, y + 3, z + 3, x, y + 3, z + 4, param.BLACK_CONCRETE)
    mc.setBlocks(x, y + 4, z + 1, x, y + 5, z + 2, param.BLACK_CONCRETE)
    mc.setBlocks(x, y + 4, z + 5, x, y + 5, z + 6, param.BLACK_CONCRETE)


def odoriba(kx, ky, kz):
    mc.setBlocks(kx, ky, kz - 6, kx + 5, ky, kz - 11, param.SMOOTH_STONE)


def maekaidan(kx, ky, kz):
    mc.setBlocks(kx, ky, kz, kx + 5, ky, kz - 1, param.SMOOTH_STONE)
    mc.setBlocks(kx, ky + 1, kz - 2, kx + 5, ky + 1, kz - 3, param.SMOOTH_STONE)
    mc.setBlocks(kx, ky + 2, kz - 4, kx + 5, ky + 2, kz - 5, param.SMOOTH_STONE)
    mc.setBlocks(kx, ky + 3, kz - 6, kx + 5, ky + 3, kz - 11, param.SMOOTH_STONE)


for n in range(3):
    head = rd.randint(1, 3)
    if head == 1:
        skull(x, y, z)
    elif head == 2:
        zombie(x, y, z)
    else:
        creeper(x, y, z)
    sleep(0.1)
    z += 8

mc.postToChat("壁作った！！！！！！")

maekaidan(kx, ky, kz)
ky += 4
kz -= 6
muki = rd.randint(1, 3)
if muki == 1:
    hidarikaidan()
elif muki == 2:
    maekaidan(kx, ky, kz)
else:
    migikaidan()

mc.postToChat("階段置いた！！！！！")
