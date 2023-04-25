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
muki = 0
kx = -10
ky = 63
kz = -20
ue = 0
migi = 0
sita = 0
hidari = 0


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


def kaidan(kx, y, kz):
    mc.setBlocks(kx, y, kz, kx - 4, y, kz - 4, param.SMOOTH_STONE)


def clear(kx, ky, kz):
    mc.setBlocks(kx - 15, ky, kz - 15, kx + 15, ky + 5, kz + 15, param.AIR)


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
clear(kx, ky, kz)

for m in range(5):
    kaidan(kx, y, kz)
    y += 1
    muki = rd.randint(1, 4)
    if muki == 1 & ue == 0:
        kz += -5
        ue = 0
        migi = 0
        sita = 1
        hidari = 0
    elif muki == 2 & migi == 0:
        kx += 5
        ue = 0
        migi = 0
        sita = 0
        hidari = 1
    elif muki == 3:
        kz += 5
        ue = 1
        migi = 0
        sita = 0
        hidari = 0
    else:
        kx += -5
        ue = 0
        migi = 1
        sita = 0
        hidari = 0
    sleep(0.1)
    mc.postToChat("階段置いた！！！！！")
