# # jo

from mcje.minecraft import Minecraft
import param_MCJE as param

import make_kansito 
import make_kaidan
import make_insidekaidan

mc = Minecraft.create(port=param.PORT_MC)  # MCJE:14712, MCPI:4711
mc.postToChat("demo3")
mc.postToChat("こんにちは！")

mc.player.setPos(0, 1, 0)

# mc.setBlocks(-50,1,-50,50,111,50,param.GLASS)


# mc.setBlocks(-49,0,-49,49,200,49,param.AIR)


make_kansito.make_honto(mc)

make_kansito.make_kaidow(mc)

# # y = 1
# # for j in range(5):
# #     x = 48
# #     z = -5
# #     for i in range(10):
# #         mc.setBlocks(-x,y,z,-(x - 4),y + 1,z - 3,param.GLASS)
# #         y += 1
# #         z -= 4

# #     for i in range(10):
# #         mc.setBlocks(-x,y,z,-(x - 4),y + 1,z - 3,param.GLASS)
# #         y += 1
# #         x -= 5

make_kaidan.make_outkaidan(mc)

mc.setBlocks(-3,2,-3,3,100,3,param.AIR)
mc.setBlocks(-2,100,-2,2,101,2,param.AIR)

# # x = -3
# # y = 1
# # z = -3

# # for j in range(4):
# #     for i in range(6):
# #         mc.setBlock(x, y, z, param.SEA_LANTERN_BLOCK)
# #         x += 1
# #         y += 1

# #     for i in range(6):
# #         mc.setBlock(x, y, z, param.SEA_LANTERN_BLOCK)
# #         z += 1
# #         y += 1

# #     for i in range(6):
# #         mc.setBlock(x, y, z, param.SEA_LANTERN_BLOCK)
# #         x -= 1
# #         y += 1

# #     for i in range(6):
# #         mc.setBlock(x, y, z, param.SEA_LANTERN_BLOCK)
# #         z -= 1
# #         y += 1

# # z += 1
# # x += 1

# # for i in range(5):
# #     mc.setBlock(x, y, z, param.SEA_LANTERN_BLOCK)
# #     x += 1
# #     y += 1


make_insidekaidan.make_insidekaidan_S(mc,)

make_insidekaidan.make_insidekaidan_E(mc,)

make_insidekaidan.make_insidekaidan_N(mc,)

make_insidekaidan.make_insidekaidan_W(mc,)

make_kansito.make_kannsito(mc, x= -16, z= -16)
make_kansito.make_kannsito(mc, x=28, z=28)
make_kansito.make_kannsito(mc, x= 28, z= -15)
make_kansito.make_kannsito(mc, x= -15, z= 28)