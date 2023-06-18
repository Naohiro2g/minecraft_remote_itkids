# コードの概要はそれぞれどんな感じなの？
### axis_flat.py
アクシズフラットは指定位置をフラットにした後、XYZ軸を作ってくれます。フラットにする範囲は変更可能。XYZ軸の生成は時間がすごくかかります。

範囲を変更したいときの手順
１.このプログラムを探してください。
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
２.このプログラムの中の、
```reset_minecraft_world(mc, width=50)```をいじります。width,つまり幅を変えることで、フラットにする範囲を変更することができます。


### creeper_test3.py
クリーパーの顔を生成することができるプログラムです。
アレンジして遊びたい方は、こちらのプログラムを複製してそれを改良することをお勧めします。
詳しいことは<a href= "https://github.com/harimanjuu/minecraft_remote_itkids/blob/main/itkids_m5/api_06_RS_Harimanjuu/README_JAPANESE.md" target="_blank">README_JAPANESE.md</a>をご覧ください。

### demo_1.py
axis_flat.pyのXYZ軸を作らないバージョンです。
つまり、ただ地形をフラットにするだけのプログラムです。
axis_flat.pyと同様に、地形をフラットにする範囲は変更可能です。あまり範囲を大きくしすぎるとパソコンが唸るのでやめましょう。そこまでフラットにしなくても、大抵の場合はどうにかなります。

フラットにする範囲を変更したい場合は、
```axis_flat.reset_minecraft_world(mc, width=50)```
のwidth（幅）を変えましょう。




### param_MCJE.py
クリーパーやXYZ軸を作るときに利用されます。基本いじらないほうが吉ですが、creeper_test3.pyやaxis_flat.pyを実行したときに使うことができるブロックの編集をすることができます。
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
「=」の前にはプログラム内で使いたいブロックの名前、(どんな名前でもOKです！)「=」の後ろには、<a href="https://n5v.net/command/block-item-id/" target="_blank">こちらのサイト</a>の「JE」を参考にしてブロックの「本当の」名前を書いてください。
※このプログラム単体では全く動きません。