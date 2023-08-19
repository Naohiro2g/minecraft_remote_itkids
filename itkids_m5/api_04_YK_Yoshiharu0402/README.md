# itkids_m6/api_04_KY_Yoshiharu0402
ITkidsプロジェクトの卒業制作として作成されたリポジトリです。

## [MyApi.py](./MyApi.py)
自分の座標によってブロックが置き続けられます。時間指定も可能です。※まだ多少のバグが残っています。

#### 動作環境
[Minecraft Java Edition 1.12.2](./https://www.minecraft.net/ja-jp)

[forge 1.12.2](./https://files.minecraftforge.net/net/minecraftforge/forge/index_1.12.2.html)

[RemoteControllerMod-1.12.2 v0.02](./https://www.curseforge.com/minecraft/mc-mods/remote-controller/files/3242375)

#### 使い方
使うときは、関数 make_blocks を使います。

from MyApi import make_blocks で使用可能になります。

make_blocks(block_up, block_down, block_left, block_right, material, min)


ブロックの設置は自分の下半身が基準になります。0の時はブロックが置かれません。
- **block_up** 

自分の上に置くブロックの位置についてです。2なら自分の真上、3なら自分の一つ上にブロックが置かれます。1にすると自分の頭に重なるので注意が必要です。
- **block_down** 

自分の下に置くブロックの位置についてです。1なら自分の真下にブロックが置かれます。
- **block_left** 

自分の左に置くブロックの位置についてです。1なら自分の真左にブロックが置かれます。x座標、z座標どちらに視点を動かしても変わりません。また、x座標とz座標の間に視点を向けると左にブロックが置かれなくなります。
- **block_right** 

自分の右に置くブロックの位置についてです。1なら自分の真右にブロックが置かれます。x座標、z座標どちらに視点を動かしても変わりません。また、x座標とz座標の間に視点を向けると右にブロックが置かれなくなります。
- **material** 

置くブロックの種類についてです。[param_MCJE1122.py](./param_MCJE1122.py)で関数指定したブロックが使用可能です。ブロック一覧は[block.py](./block.py)にあります。param.使いたいブロック
- **min**

プログラムが実行される時間です。単位は分です。

#### サンプルプログラム

- 道を作るプログラム [Road.py](./Road.py)

make_blocks(0, 1, 0, 0, param.好きなブロック, 1)


名の通り、自分の歩いた場所のブロックを変えるプログラムです。海の上も歩くことが可能です。

[<img src="./images/ezgif-4-e5d04a153f.gif">](./images/ezgif-4-e5d04a153f.gif)

- 安全な通路を作るプログラム [SafetyRoad.py](./SafetyRoad.py)

make_blocks(2, 1, 1, 1, param.COBBLESTONE, 1)

自分の周りを丸石で囲むプログラムです。これなら夜もモンスターににおびえず安全に移動できますね。

[<img src="./images/ezgif-4-d1a8f823e5.gif">](./images/ezgif-4-d1a8f823e5.gif)

- 爆速ボート [IceBoat.py](./IceBoat.py)

make_blocks(0, 1, 0, 0, param.ICE, 1)

道を作るプログラムの素材を氷ブロックにしたものです。このプログラムはボートに乗っていても効果があるので、ボートに乗ってこのプログラムを動かすだけで高速に移動ができるボートが作れます。しかし、スペックの問題で処理速度が追い付かずに止まってしまうかもしれないです。また、理論上はトロッコとレールでもできるのですが、僕のプログラミングの技能がなくて作れなかったです。

[<img src="./images/ezgif-4-4bff1e4e4c.gif">](./images/ezgif-4-4bff1e4e4c.gif)
## [param_MCJE1122.py](./param_MCJE1122.py)
ここに使いたいブロックを書きます。ブロック一覧は[block.py](./block.py)で探します。

（例）

砂ブロックを使いたいとき、[block.py](./block.py)では、SAND = block(12)　と書いてあるので、[param.MCJE1122](./param.MCJE1122)に、SAND = 12　を追加する。
