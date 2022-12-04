from mcje.minecraft import Minecraft
import param_MCJE as param
import make_kaidan

def make_insidekaidan_S(mc,x=-3,y=1,z=-3,dansu=6,insideblock=param.SEA_LANTERN_BLOCK):
    blocktipe_insideblock=insideblock
    use_x = x
    use_y = y
    use_z = z
    for j in range(4):

        make_kaidan.make_insidekaidan_seihoukei_zyouhen(mc,x=use_x,y=use_y,z=use_z,dansu=dansu,insideblock_seihoukei_zyouhen=blocktipe_insideblock)

        use_x += dansu
        use_y += dansu

        make_kaidan.make_insidekaidan_seihoukei_migi(mc,x=use_x,y=use_y,z=use_z,dansu=dansu,insideblock_seihoukei_migi=blocktipe_insideblock)

        use_z += dansu
        use_y += dansu

        make_kaidan.make_insidekaidan_seihoukei_kahen(mc,x=use_x,y=use_y,z=use_z,dansu=dansu,insideblock_seihoukei_kahen=blocktipe_insideblock)

        use_x -= dansu
        use_y += dansu

        make_kaidan.make_insidekaidan_seihoukei_hidari(mc,x=use_x,y=use_y,z=use_z,dansu=dansu,insideblock_seihoukei_hidari=blocktipe_insideblock)

        use_z -= dansu
        use_y += dansu
    
    use_z += 1
    use_x += 1

    make_kaidan.make_insidekaidan_seihoukei_zyouhen(mc,x=use_x,y=use_y,z=use_z,dansu=dansu - 1,insideblock_seihoukei_zyouhen=insideblock)

def make_insidekaidan_E(mc,x=3,y=1,z=-3,dansu=6,insideblock=param.SEA_LANTERN_BLOCK):
    blocktipe_insideblock=insideblock
    use_x = x
    use_y = y
    use_z = z
    for l in range(4):

        make_kaidan.make_insidekaidan_seihoukei_migi(mc,x=use_x,y=use_y,z=use_z,dansu=dansu,insideblock_seihoukei_migi=blocktipe_insideblock)

        use_z += dansu
        use_y += dansu

        make_kaidan.make_insidekaidan_seihoukei_kahen(mc,x=use_x,y=use_y,z=use_z,dansu=dansu,insideblock_seihoukei_kahen=blocktipe_insideblock)

        use_x -= dansu
        use_y += dansu

        make_kaidan.make_insidekaidan_seihoukei_hidari(mc,x=use_x,y=use_y,z=use_z,dansu=dansu,insideblock_seihoukei_hidari=blocktipe_insideblock)

        use_z -= dansu
        use_y += dansu

        make_kaidan.make_insidekaidan_seihoukei_zyouhen(mc,x=use_x,y=use_y,z=use_z,dansu=dansu,insideblock_seihoukei_zyouhen=blocktipe_insideblock)

        use_x += dansu
        use_y += dansu
    
    use_z += 1
    use_x -= 1

    make_kaidan.make_insidekaidan_seihoukei_migi(mc,x=use_x,y=use_y,z=use_z,dansu=dansu - 1,insideblock_seihoukei_migi=blocktipe_insideblock)

def make_insidekaidan_N(mc,x=3,y=1,z=3,dansu=6,insideblock=param.SEA_LANTERN_BLOCK):
    blocktipe_insideblock=insideblock
    use_x = x
    use_y = y
    use_z = z
    for l in range(4):

        make_kaidan.make_insidekaidan_seihoukei_kahen(mc,x=use_x,y=use_y,z=use_z,dansu=dansu,insideblock_seihoukei_kahen=blocktipe_insideblock)

        use_x -= dansu
        use_y += dansu

        make_kaidan.make_insidekaidan_seihoukei_hidari(mc,x=use_x,y=use_y,z=use_z,dansu=dansu,insideblock_seihoukei_hidari=blocktipe_insideblock)

        use_z -= dansu
        use_y += dansu

        make_kaidan.make_insidekaidan_seihoukei_zyouhen(mc,x=use_x,y=use_y,z=use_z,dansu=dansu,insideblock_seihoukei_zyouhen=blocktipe_insideblock)

        use_x += dansu
        use_y += dansu

        make_kaidan.make_insidekaidan_seihoukei_migi(mc,x=use_x,y=use_y,z=use_z,dansu=dansu,insideblock_seihoukei_migi=blocktipe_insideblock)

        use_z += dansu
        use_y += dansu
    
    use_z -= 1
    use_x -= 1

    make_kaidan.make_insidekaidan_seihoukei_kahen(mc,x=use_x,y=use_y,z=use_z,dansu=dansu - 1,insideblock_seihoukei_kahen=blocktipe_insideblock)

def make_insidekaidan_W(mc,x= -3,y=1,z=3,dansu=6,insideblock=param.SEA_LANTERN_BLOCK):
    blocktipe_insideblock=insideblock
    use_x = x
    use_y = y
    use_z = z
    for l in range(4):

        make_kaidan.make_insidekaidan_seihoukei_hidari(mc,x=use_x,y=use_y,z=use_z,dansu=dansu,insideblock_seihoukei_hidari=blocktipe_insideblock)

        use_z -= dansu
        use_y += dansu

        make_kaidan.make_insidekaidan_seihoukei_zyouhen(mc,x=use_x,y=use_y,z=use_z,dansu=dansu,insideblock_seihoukei_zyouhen=blocktipe_insideblock)

        use_x += dansu
        use_y += dansu

        make_kaidan.make_insidekaidan_seihoukei_migi(mc,x=use_x,y=use_y,z=use_z,dansu=dansu,insideblock_seihoukei_migi=blocktipe_insideblock)

        use_z += dansu
        use_y += dansu

        make_kaidan.make_insidekaidan_seihoukei_kahen(mc,x=use_x,y=use_y,z=use_z,dansu=dansu,insideblock_seihoukei_kahen=blocktipe_insideblock)

        use_x -= dansu
        use_y += dansu

    use_z -= 1
    use_x += 1

    make_kaidan.make_insidekaidan_seihoukei_hidari(mc,x=use_x,y=use_y,z=use_z,dansu=dansu - 1,insideblock_seihoukei_hidari=blocktipe_insideblock)