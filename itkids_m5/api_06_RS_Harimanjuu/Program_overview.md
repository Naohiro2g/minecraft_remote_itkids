# Let me introduce My Programs!!!
### axis_flat.py
You can make XYZ axis after flattening the specified range.
You can change the area to be flattened.
But making XYZ axis need many time.

If you want to change that, you do this. 
１. Find this program.
``` python
if __name__ == "__main__":
    # his computer
    # mc = Minecraft.create(address='nao2g005.local', port=param.PORT_MC)
    # your computer
    mc = Minecraft.create(port=param.PORT_MC)

    mc.postToChat("axis_flat module main part")

    # if MCJE 1.12.2 or earlier
    # mc.player.setPos(0,100,0)
    # mc.setBlocks(-80, 60, -80,   80, 120, 80,   0)

    reset_minecraft_world(mc, width=50)
    # draw_XYZ_axis(mc, wait=0.2)
    # clear_XYZ_axis(mc, wait=0)
    draw_XYZ_axis(mc, wait=0.3)
```
２.You change ```reset_minecraft_world(mc, width=50)```
When you change "width", this program changes the area to be flattened.

### creeper_test3.py
This program can make creeper's face by this program.
If you want to arange, I recommend copying it and aranging it.

For more information "<a href="https://github.com/harimanjuu/minecraft_remote_itkids/blob/main/itkids_m5/api_06_RS_Harimanjuu/README.md" target="_blank">README.md</a>"

### demo_1.py
This program can flatten the specified range. But this program doesn't make XYZ-axis.
Others are the same as "axis_flat.py".

You change ```reset_minecraft_world(mc, width=50)```.
When you change "width", this program changes the area to be flattened.

### param_MCJE.py
This program is used when you will make creeper's face and XYZ-axis. You don't need to change this program. But you can edit "Block" for running creeper_test3.py and axis_flat.py.
```PYTHON
AIR = "air"
STONE = "stone"
GRASS_BLOCK = "grass_block"
GOLD_BLOCK = "gold_block"
IRON_BLOCK = "iron_block"
LIME_WOOL_BLOCK = "lime_wool"
BLACK_WOOL_BLOCK ="black_wool"
GLOWSTONE = "glowstone"
SEA_LANTERN_BLOCK = "sea_lantern" 
```
You need to white the name of the block you want to use before the "=". (You can give a favorite name!!) And white the real name of the block you want to use behind of "=". (please reter to <a href="https://mcreator.net/wiki/minecraft-block-and-item-list-registry-and-code-names" target="_blank">this website</a>.)
※You can not run this program.
