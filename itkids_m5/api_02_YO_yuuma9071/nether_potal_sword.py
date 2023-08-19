#ネザーゲートの剣を作る。

from mcje.minecraft import Minecraft
import param_MCJE as param
from time import sleep

mc = Minecraft.create(port=param.PORT_MC)
sleep(3)

mc.postToChat('3')
sleep(1)

mc.postToChat('2')
sleep(1)

mc.postToChat('1')

y = param.Y_SEA + 1
mc.setBlocks(-4, y, 2, 14, y + 30, 22, param.AIR)
sleep(1)

mc.postToChat('ネザーゲートソードを作成します。')
sleep(1)

#土台を作る。

mc.postToChat('土台')
sleep(0.5)

mc.postToChat('一段目')
x = 1
y = param.Y_SEA + 1
for _n in range(9):
    z = 7
    for _i in range(11):
        mc.setBlock(x, y, z,  param.QUARTZ_BLOCK)
        sleep(0.1)
        z += 1
    x += 1

sleep(0.5)

x, z = 1, 7
y = param.Y_SEA + 1
mc.setBlock(x + 1, y, z, param.AIR)
mc.setBlock(x + 7, y, z, param.AIR)
mc.setBlock(x + 1, y, z + 10, param.AIR)
mc.setBlock(x + 7, y, z + 10, param.AIR)
mc.setBlocks(x, y, z, x, y, z + 1, param.AIR)
mc.setBlocks(x + 8, y, z, x + 8, y, z + 1, param.AIR)
mc.setBlocks(x, y, z + 9, x, y, z + 10, param.AIR)
mc.setBlocks(x + 8, y, z + 9, x + 8, y, z + 10, param.AIR)

sleep(0.5)

mc.postToChat('二段目')
x = 2
y = param.Y_SEA + 2
for _n in range(7):
    z = 8
    for _i in range(9):
        mc.setBlock(x, y, z,  param.QUARTZ_BLOCK)
        sleep(0.1)
        z += 1
    x += 1

sleep(0.25)

y = param.Y_SEA + 2
mc.setBlock(2, y, 8, param.AIR)
mc.setBlock(8, y, 8, param.AIR)
mc.setBlock(2, y, 16, param.AIR)
mc.setBlock(8, y, 16, param.AIR)
y += 1

sleep(0.5)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#ネザーゲートを作る。

mc.postToChat('ネザーゲート')

x = 5
z = 10
y = param.Y_SEA + 1
for _i in range(5):
    mc.setBlock(x, y, z,  param.OBSIDIAN)
    mc.setBlock(x, y + 1, z, param.AIR)
    sleep(0.25)
    z += 1

sleep(0.5)

x, z = 5, 10
y = param.Y_SEA + 1
for _i in range(20):
    mc.setBlock(x, y, z,  param.OBSIDIAN)
    sleep(0.25)
    y += 1

sleep(0.5)

x, z = 5, 14
y = param.Y_SEA + 1
for _i in range(20):
    mc.setBlock(x, y, z,  param.OBSIDIAN)
    sleep(0.25)
    y += 1

sleep(0.5)

x = 5
z = 10
y = param.Y_NETHER
for _i in range(5):
    mc.setBlock(x, y, z,  param.OBSIDIAN)
    sleep(0.25)
    z += 1

sleep(0.5)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#刃を作る。

mc.postToChat('刃の装飾')
x, z = 4, 10
y = param.Y_SEA + 3
for _i in range(17):
    mc.setBlock(x, y, z,  param.DIORITE_WALL)
    mc.setBlock(x, y, z + 4, param.DIORITE_WALL)
    mc.setBlock(x + 2, y, z, param.DIORITE_WALL)
    mc.setBlock(x + 2, y, z + 4, param.DIORITE_WALL)
    sleep(0.05)
    y += 1

sleep(1)

y = param.Y_NETHER
mc.setBlock(5, y, 10, param.DIORITE)
mc.setBlock(5, y, 14, param.DIORITE)
y += 1

sleep(1)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#鍔を作る。

mc.postToChat('鍔')

x = 5
z = 6
y = param.Y_NETHER + 2
for _i in range(13):
    mc.setBlock(x, y, z,  param.DIORITE_WALL)
    sleep(0.25)
    z += 1

sleep(0.25)

x, z = 5, 11
y = param.Y_NETHER + 1
for _i in range(3):
    mc.setBlock(x, y, z,  param.DIORITE)
    mc.setBlock(x, y, z + 2, param.DIORITE)
    mc.setBlock(x, y, z + 1, param.DIAMOND_BLOCK)
    mc.setBlock(x, y, z - 1, param.POLISHED_DIORITE)
    mc.setBlock(x, y, z + 3, param.POLISHED_DIORITE)
    sleep(0.25)
    y += 1

sleep(0.25)

x, z = 4, 10
y = param.Y_NETHER
mc.setBlock(x, y, z, param.POLISHED_DIORITE)
sleep(0.25)
mc.setBlock(x, y, z + 1, param.DIORITE)
sleep(0.25)
mc.setBlock(x, y, z + 2, param.POLISHED_DIORITE)
sleep(0.25)
mc.setBlock(x, y, z + 3, param.DIORITE)
sleep(0.25)
mc.setBlock(x, y, z + 4, param.POLISHED_DIORITE)
sleep(0.25)

x, z = 6, 14
y = param.Y_NETHER
mc.setBlock(x, y, z, param.POLISHED_DIORITE)
sleep(0.25)
mc.setBlock(x, y, z - 1, param.DIORITE)
sleep(0.25)
mc.setBlock(x, y, z - 2, param.POLISHED_DIORITE)
sleep(0.25)
mc.setBlock(x, y, z - 3, param.DIORITE)
sleep(0.25)
mc.setBlock(x, y, z - 4, param.POLISHED_DIORITE)
sleep(0.25)

sleep(0.5)

x = 5
y = param.Y_NETHER + 2
z = 9
for _n in range(3):
    mc.setBlock(x, y, z,  param.DIORITE)
    sleep(0.25)
    z -= 1

x = 5
y = param.Y_NETHER + 2
z = 15
for _n in range(3):
    mc.setBlock(x, y, z, param.DIORITE)
    sleep(0.25)
    z += 1

sleep(0.5)

x, z = 5, 9
y = param.Y_NETHER + 1
mc.setBlock(x, y, z, param.POLISHED_DIORITE)
mc.setBlock(x, y, z + 6, param.POLISHED_DIORITE)
sleep(0.5)
mc.setBlock(x, y + 1, z + 8, param.POLISHED_DIORITE)
mc.setBlock(x, y + 1, z - 2, param.POLISHED_DIORITE)

sleep(0.25)

x, z = 5,7
y = param.Y_NETHER + 3
mc.setBlock(x, y, z, param.DIORITE_SLAB)
mc.setBlock(x, y, z + 2, param.DIORITE_SLAB)
mc.setBlock(x, y, z + 8, param.DIORITE_SLAB)
mc.setBlock(x, y, z + 10, param.DIORITE_SLAB)

sleep(0.5)

x, z = 4, 11
y = param.Y_NETHER + 1
for _i in range(2):
    mc.setBlock(x, y, z,  param.DIORITE_WALL)
    mc.setBlock(x, y, z + 2, param.DIORITE_WALL)
    mc.setBlock(x + 2, y, z,  param.DIORITE_WALL)
    mc.setBlock(x + 2, y, z + 2, param.DIORITE_WALL)
    sleep(0.5)
    y += 1

sleep(0.25)

x, z = 4, 11
y = param.Y_NETHER
mc.setBlock(x, y + 3, z, param.DIORITE_SLAB)
mc.setBlock(x + 2, y + 3, z, param.DIORITE_SLAB)
mc.setBlock(x, y + 3, z + 2, param.DIORITE_SLAB)
mc.setBlock(x + 2, y + 3, z + 2, param.DIORITE_SLAB)

sleep(0.25)

x, z = 4, 10
y = param.Y_NETHER
mc.setBlock(x, y + 1, z, param.DIORITE_WALL)
mc.setBlock(x, y + 1, z + 4, param.DIORITE_WALL)
mc.setBlock(x + 2, y + 1, z, param.DIORITE_WALL)
mc.setBlock(x + 2, y + 1, z + 4, param.DIORITE_WALL)
mc.setBlock(x, y + 2, z, param.DIORITE_SLAB)
mc.setBlock(x, y + 2, z + 4, param.DIORITE_SLAB)
mc.setBlock(x + 2, y + 2, z, param.DIORITE_SLAB)
mc.setBlock(x + 2, y + 2, z + 4, param.DIORITE_SLAB)

sleep(0.25)

x, z = 4, 7
y = param.Y_NETHER
mc.setBlocks(x, y + 2, z, x, y + 2, z + 2, param.DIORITE_WALL)
mc.setBlocks(x, y + 2, z + 8, x, y + 2, z + 10, param.DIORITE_WALL)

sleep(0.25)

x, z = 6, 7
y = param.Y_NETHER
mc.setBlocks(x, y + 2, z, x, y + 2, z + 2, param.DIORITE_WALL)
mc.setBlocks(x, y + 2, z + 8, x, y + 2, z + 10, param.DIORITE_WALL)

y = param.Y_NETHER
mc.setBlock(4, y + 3, 12, param.POLISHED_DIORITE)
mc.setBlock(6, y + 3, 12, param.POLISHED_DIORITE)
sleep(0.5)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#柄を作る。
mc.postToChat('柄')

x = 5
y = param.Y_NETHER + 4
z = 11
for _n in range(3):
    mc.setBlock(x, y, z, param.DIORITE_WALL)
    sleep(0.25)
    z += 1

x = 4
y = param.Y_NETHER + 4
z = 12
for _n in range(3):
    mc.setBlock(x, y, z, param.DIORITE)
    sleep(0.25)
    x += 1

x = 4
y = param.Y_NETHER + 5
z = 12
for _n in range(3):
    mc.setBlock(x, y, z, param.DIORITE_WALL)
    sleep(0.25)
    x += 1

x = 5
y = param.Y_NETHER + 5
z = 11
for _n in range(3):
    mc.setBlock(x, y, z, param.DIORITE)
    sleep(0.25)
    z += 1

sleep(0.5)

x = 4
y = param.Y_NETHER + 10
z = 12
for _n in range(3):
    mc.setBlock(x, y, z, param.DIORITE_WALL)
    sleep(0.25)
    x += 1

x = 5
y = param.Y_NETHER + 10
z = 11
for _n in range(3):
    mc.setBlock(x, y, z, param.DIORITE_WALL)
    sleep(0.25)
    z += 1

sleep(0.25)

y = param.Y_NETHER + 6
mc.setBlock(5, y, 12, param.POLISHED_DIORITE)
sleep(0.25)
mc.setBlock(5, y + 1, 12, param.DIORITE)
sleep(0.25)
mc.setBlock(5, y + 2, 12, param.POLISHED_DIORITE)
sleep(0.25)
mc.setBlock(5, y + 3, 12, param.REDSTONE_BLOCK)
sleep(0.25)
mc.setBlock(5, y + 4, 12, param.POLISHED_DIORITE)
sleep(0.25)
mc.setBlock(5, y + 5, 12, param.DIORITE)

sleep(0.5)

x, z = 4, 12
y = param.Y_NETHER - 1
mc.setBlock(x, y, z, param.DIORITE)
mc.setBlock(x + 2, y, z, param.DIORITE)
mc.setBlock(x, y - 1, z, param.DIORITE_WALL)
mc.setBlock(x + 2, y - 1, z, param.DIORITE_WALL)

sleep(1)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#ネザーゲートを開く。
mc.postToChat('ゲート開通！')

sleep(1)

y = param.Y_SEA + 2
mc.setBlock(5, y, 12, param.FIRE)
