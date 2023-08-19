from mcje.minecraft import Minecraft
import param_MCJE1122 as param
import time

mc = Minecraft.create(port=param.PORT_MC)
mc.postToChat('start my api')

def make_blocks(block_up, block_down, block_left, block_right, material, min):
    t_end = time.time() + 60*min
    while time.time() < t_end:
        (x,y,z) = mc.player.getTilePos()
        (angle) = mc.player.getRotation()
        print (angle)
    
        if block_up > 0:
            mc.setBlock(x,y+block_up,z,material)
        if block_down > 0:
            mc.setBlock(x,y-block_down,z,material)
        if 100 > angle > 80 and block_left > 0:
            mc.setBlocks(x,y,z+block_left,x,y+1,z+block_left,material)
        if 100 > angle > 80 and block_right > 0:
            mc.setBlocks(x,y,z-block_right,x,y+1,z-block_right,material)
        if -100 < angle < -80 and block_right > 0:
            mc.setBlocks(x,y,z+block_right,x,y+1,z+block_right,material)
        if -100 < angle < -80 and block_left > 0:
            mc.setBlocks(x,y,z-block_left,x,y+1,z-block_left,material)
        if -10 < angle < 10 and block_left > 0:
            mc.setBlocks(x+block_left,y,z,x+block_left,y+1,z,material)
        if -10 < angle < 10 and block_right > 0:
            mc.setBlocks(x-block_right,y,z,x-block_right,y+1,z,material)
        if 170 < angle or -170 > angle and block_right > 0:
            mc.setBlocks(x+block_right,y,z,x+block_right,y+1,z,material)
        if 170 < angle or -170 > angle and block_left > 0:
            mc.setBlocks(x-block_left,y,z,x-block_left,y+1,z,material)
            
if __name__ == "__main__":
    make_blocks(0,0,0,0,param.GOLD_BLOCK,0)
