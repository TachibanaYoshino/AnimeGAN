# AnimeGAN
このAnimeGANは写真をアニメに素早く変換するために使用できます!  
論文は[ここ](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/doc/Chen2020_Chapter_AnimeGAN.pdf)あるいはこの[サイト](https://link.springer.com/chapter/10.1007/978-981-15-5577-0_18)からアクセスできます。  
  
**オンラインアクセス**：  このオンラインサイトを開発してくれた[@TonyLianLong](https://github.com/TonyLianLong/AnimeGAN.js)のおかげで、何もインストールしなくてもブラウザから直接アクセスできます。[ここをクリックして試してみてください！](https://animegan.js.org/)  
  
**吉報**： Tensorflow-1.15.0はこのリポジトリのコードと互換性があります。このバージョンでは、変更せずにこのコードを実行することができます。[前提は、TFバージョンに対応するCUDAとCudnnが正しくインストールされていることです。](https://tensorflow.google.cn/install/source#gpu)。多分、TF-1.8.0とTF-1.15.0の間のバージョンも支持されて、この倉庫と互換性を持ちます、しかし、私はあまりに多くの余分の試みをしませんでした。
  
-----    
**いくつかのアドバイス**   
1. 訓練セットの真実の写真は風景写真ですので、人物を主体として写真を様式化するなら、トレーニングセットに少なくとも3000人の写真を追加して、新たなモデルを獲得するようにトレーニングしてください。  
2. より良い顔アニメーション効果を得るために、2枚の画像をデータとして使ってトレーニングする場合、写真の顔とアニメスタイルデータの中の顔は性別においてできるだけ一致するようにすることをおすすめします。  
3. 生成された画風化画像は、スタイルデータの全体的な輝度と色調の影響を受けるので、できるだけ夜のアニメ画像をスタイルデータとして選択しないでください。また、全体のスタイルデータに対して露出補償を行う必要があります。全体のスタイルデータの明暗一致を促進します。  
  
**新しいニュース**：  AnimeGAN+は今夏にリリースされる予定です。  
  
___  

## インストール依存項  
- python 3.6.8  
- tensorflow-gpu 1.8  
- opencv  
- tqdm  
- numpy  
- glob  
- argparse  
  
## 使い方  
### 1. vgg 19あるいは予備トレーニングのモデルをダウンロードします。  
> [vgg19.npy](https://github.com/TachibanaYoshino/AnimeGAN/releases/tag/vgg16%2F19.npy)  
  
> [Pretrained model](https://github.com/TachibanaYoshino/AnimeGAN/releases/tag/Haoyao-style_V1.0)  

### 2. データセットをダウンロード  
> [Link](https://github.com/TachibanaYoshino/AnimeGAN/releases/tag/dataset-1)  

### 3. エッジブラーを実行する  
  eg. `python edge_smooth.py --dataset Hayao --img_size 256`  
  
### 3. トレーニング  
  eg. `python main.py --phase train --dataset Hayao --epoch 101 --init_epoch 1`  
  
### 4. テスト  
  eg. `python main.py --phase test --dataset Hayao`  
  or `python test.py --checkpoint_dir checkpoint/AnimeGAN_Hayao_lsgan_300_300_1_3_10 --test_dir dataset/test/real --style_name H`  
  
____  
## 結果  
:blush:  論文からの画像。  
  
![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/doc/sota.png)  
![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/doc/e2.png)  
![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/doc/e3.png)  
![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/doc/e4.png)  
  
:heart_eyes:  写真は宮崎駿のアニメスタイルになります。  
  
![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/result/Hayao/photo/1%20(37).jpg)![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/result/Hayao/photo_result/1%20(37).jpg)  
![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/result/Hayao/photo/1%20(1).jpg)![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/result/Hayao/photo_result/1%20(1).jpg)  
![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/result/Hayao/photo/1%20(20).jpg) ![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/result/Hayao/photo_result/1%20(20).jpg)  
![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/result/Hayao/photo/1%20(21).jpg) ![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/result/Hayao/photo_result/1%20(21).jpg)  
![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/result/Hayao/photo/1%20(22).jpg) ![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/result/Hayao/photo_result/1%20(22).jpg)  
![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/result/Hayao/photo/1%20(23).jpg) ![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/result/Hayao/photo_result/1%20(23).jpg)  
![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/result/Hayao/photo/1%20(24).jpg) ![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/result/Hayao/photo_result/1%20(24).jpg)  
![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/result/Hayao/photo/1%20(46).jpg) ![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/result/Hayao/photo_result/1%20(46).jpg)  
![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/result/Hayao/photo/1%20(30).jpg) ![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/result/Hayao/photo_result/1%20(30).jpg)  
![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/result/Hayao/photo/1%20(28).jpg) ![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/result/Hayao/photo_result/1%20(28).jpg)  
![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/result/Hayao/photo/1%20(38).jpg) ![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/result/Hayao/photo_result/1%20(38).jpg)  
____  
## 感謝  
このコードは[CartoonGAN-Tensorflow](https://github.com/taki0112/CartoonGAN-Tensorflow/blob/master/CartoonGAN.py)と [Anime-Sketch-Coloring-with-Swish-Gated-Residual-UNet](https://github.com/pradeeplam/Anime-Sketch-Coloring-with-Swish-Gated-Residual-UNet)に基づいています。彼らの貢献に感謝します。  

