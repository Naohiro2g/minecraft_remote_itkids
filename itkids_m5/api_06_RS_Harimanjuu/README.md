
# Development of original API　～Creepar's face～
#### [\日本語版はこちらから/](https://github.com/harimanjuu/minecraft_remote_itkids/blob/main/itkids_m5/api_06_RS_Harimanjuu/README_JAPANESE.md)
## 1. What this API can do

   **This API is specialized in making creeper's faces**
   - Specify the location of the creeper
   - Specifying the creeper's expression
   - Specify the number of creepers
   - Designation of creeper skin and face color
## 2. What this API can not do

   **There is not much that can be done yet. These are just some of the items that need to be improved in the future**
   * Specify creeper orientation
   * Building a creeper's body
   * Make something other than a creeper
   * Move installed creepers
  
## 3. Let's try!!
   
   In the meantime, let's try different things, referring to what can and cannot be done.
   If it's just a face, it's more flexible than you might think.
   So there are probably quite a few things you can do.  
   So let's go!


  Keep it clean. It is surprisingly important.
  (If you want to reset, run a "demo1.py".)

   ![](image/void.png)



   First, summon one normal creeper.


   ![](image/one.png)

   When placed on the ground, it looks like the item "creeper's head" like this.

   Let's put this side by side. You can connect them, but it is better to leave a little space between them because it is awkward.

   ![](image/three%20normalface.png)
   
   これは繰り返しの動作で成り立っています。リスト関数を使っているので、顔を変えたりなんかも出来ちゃいます。

   ![](image/three%20someface.png)

   随分表情豊かになりましたね。(左から、驚いた顔、ニッコリ、ノーマル。)

   遊んでいる最中に気づきました。横ができるなら、縦に並んだクリーパーもできちゃうんじゃない???って。

   ![](image/tate.png)

   予想通りだね。さっきはxを移動させていたけど、yを移動させてあげればいい、たったそれだけです。
   <br>てことはクリーパーを奥に並ばせることもできるけど...原理がわかってくれればいいので今回は割愛。

   最後に肌も変えてみましょう。

   ![](image/石クリーパー.png)

   肌の色も変えられるし、何なら顔のパーツの色も変えられます。

   いろいろ遊び放題ってことをわかってくれたらいいと思います。（体は作れないけどね :( ）

## 4. クリーパーの作り方
   クリーパーをいろいろやりたい場合は、一番下にある

   ```
    faces = ["normal"]
    x = 0

    for face in faces:
     set_creeper(mc, x=x, y=y, block_id="green_wool", face=face)
     mc.postToChat(face)
     x += 10 
   ```

   というプログラムをいじって見てください。
   
   ```faces = [...]```
   
   のところはかっこの中に生成したい順番で表情を書いてください。
   <br>上の方に「normal」「smile」などいろいろ載ってます。その言葉通りに入力しないと動作しません。

   x =...が書いてあるところにお好みの座標を入れてあげると、その通りに配置できます。（y,zは省いていますが、追加しても構いません。その場合は、「set_creeper」のカッコ内の「x=x,」の後に「y=y,」と書き足してください。(zも同様です。)）

   ```block_id="..."```　のところでblockの種類を変えることができます。param_MCJE.pyというプログラムから、どんなブロックがあるのか見れるので、そこから選んで```"..."``` の中に書き込んでください。

   ```x += 10``` では、複数クリーパーを作るときにどのくらい間隔をあけるか命令できます。この距離には、クリーパーの体の分も含まれているので、そこは注意しましょう。（クリーパーは8ブロック四方でできています。）

   
   ## 最後に

   このプログラムはマインクラフトをリモートで制御できる環境がある方でないと動かすことができません。<br>詳しくは、<a href="https://github.com/Naohiro2g/minecraft_remote" target="_blank">マインクラフトのリモート制御</a>を参照してください。

   ファイル内のプログラムの概要は[こちらから](https://github.com/harimanjuu/minecraft_remote_itkids/blob/main/itkids_m5/api_06_RS_Harimanjuu/test.md)

   