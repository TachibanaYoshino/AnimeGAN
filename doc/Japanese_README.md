# AnimeGAN   
このAnimeGANは写真をアニメに素早く変換するために使用できます!  
論文は[ここ](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/doc/Chen2020_Chapter_AnimeGAN.pdf) あるいはこの[サイト](https://link.springer.com/chapter/10.1007/978-981-15-5577-0_18) からアクセスできます。    
  
[**AnimeGANの改良版である AnimeGANv2.**](https://github.com/TachibanaYoshino/AnimeGANv2)  
**オンラインアクセス**：  このオンラインサイトを開発してくれた[@TonyLianLong](https://github.com/TonyLianLong/AnimeGAN.js) のおかげで、何もインストールしなくてもブラウザから直接アクセスできます。[ここをクリックして試してみてください！](https://animegan.js.org/)   
**Pytorch version**:  [pytorch-animeGAN](https://github.com/ptran1203/pytorch-animeGAN).   

-----    
**いくつかのアドバイス**   
1. 訓練セットの真実の写真は風景写真ですので、人物を主体として写真を様式化するなら、トレーニングセットに少なくとも3000人の写真を追加して、新たなモデルを獲得するようにトレーニングしてください。  
2. より良い顔アニメーション効果を得るために、2枚の画像をデータとして使ってトレーニングする場合、写真の顔とアニメスタイルデータの中の顔は性別においてできるだけ一致するようにすることをおすすめします。  
3. 生成された画風化画像は、スタイルデータの全体的な輝度と色調の影響を受けるので、できるだけ夜のアニメ画像をスタイルデータとして選択しないでください。また、全体のスタイルデータに対して露出補償を行う必要があります。全体のスタイルデータの明暗一致を促進します。  
  
**新しいニュース**：  
&ensp;&ensp;&ensp;&ensp;&ensp;  **AnimeGANv2** がリリースされ、[**ここ**](https://github.com/TachibanaYoshino/AnimeGANv2)からアクセスできます。  
```yaml
AnimeGANv2 の改善方針には、主に以下の4点があります。
```  
&ensp;&ensp; 1. 生成された画像の高周波アーティファクトの問題を解決する。  
&ensp;&ensp; 2. トレーニングが簡単で、論文の効果を直接達成できます。  
&ensp;&ensp; 3. ジェネレーターネットワークのパラメーターの数をさらに減らします。  
&ensp;&ensp; 4. 可能な限りBDムービーからの新しい高品質スタイルデータを使用します。  
  
___  
  
## インストール依存項  
- python 3.7  
- tensorflow-gpu 1.15.0 (ubuntu, GPU 2080Ti, cuda 10.0.130, cudnn 7.6.0)  
- opencv  
- tqdm  
- numpy  
- glob  
- argparse  
  
## 使い方  
### 1. テスト  
  e.g. `python test.py --checkpoint_dir checkpoint/generator_Hayao_weight --test_dir dataset/test/real --style_name H`  
  
### 2. ビデオをアニメに変換します   
  e.g. `python video2anime.py  --video video/input/お花見.mp4  --checkpoint_dir  ./checkpoint/generator_Hayao_weight`  
    
### 3.トレーニング
#### 1. vgg 19あるいは予備トレーニングのモデルをダウンロードします  
> [vgg19.npy](https://github.com/TachibanaYoshino/AnimeGAN/releases/tag/vgg16%2F19.npy)  
  
> [Pretrained model](https://github.com/TachibanaYoshino/AnimeGAN/releases/tag/Haoyao-style_v1.0)  
  
#### 2. データセットをダウンロード  
> [Link](https://github.com/TachibanaYoshino/AnimeGAN/releases/tag/dataset-1)  
  
#### 3. エッジブラーを実行する  
  e.g. `python edge_smooth.py --dataset Hayao --img_size 256`  
  
#### 4. トレーニング  
  e.g. `python train.py --dataset Hayao  --epoch 101 --init_epoch 5`  
  
#### 5. ジェネレーターのパラメーターを抽出する  
  e.g. `python get_generator_ckpt.py --checkpoint_dir  ../checkpoint/AnimeGAN_Hayao_lsgan_300_300_1_1_10  --style_name Hayao`  
    
____  
## 結果  
:blush:  論文からの画像。  
  
![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/doc/sota.png)  
![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/doc/e2.png)  
![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/doc/e3.png)  
![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/doc/e4.png)  
  
:heart_eyes:  写真は宮崎さんのアニメスタイルになります。  
  
![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/result/Hayao/photo/AE86.png) ![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/result/Hayao/photo_result/AE86.png)  
![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/result/Hayao/photo/%2037.jpg) ![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/result/Hayao/photo_result/%2037.jpg)  
![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/result/Hayao/photo/%201.jpg) ![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/result/Hayao/photo_result/%201.jpg)  
![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/result/Hayao/photo/%2031.jpg) ![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/result/Hayao/photo_result/%2031.jpg)  
![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/result/Hayao/photo/%2021.jpg) ![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/result/Hayao/photo_result/%2021.jpg)  
![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/result/Hayao/photo/%2022.jpg) ![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/result/Hayao/photo_result/%2022.jpg)  
![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/result/Hayao/photo/%2024.jpg) ![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/result/Hayao/photo_result/%2024.jpg)  
![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/result/Hayao/photo/%2046.jpg) ![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/result/Hayao/photo_result/%2046.jpg)  
![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/result/Hayao/photo/%2030.jpg) ![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/result/Hayao/photo_result/%2030.jpg)  
![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/result/Hayao/photo/%2028.jpg) ![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/result/Hayao/photo_result/%2028.jpg)  
![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/result/Hayao/photo/%2044.jpg) ![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/result/Hayao/photo_result/%2044.jpg)  
_____  
## ライセンス  
このレポは、学術研究、教育、科学出版物などの非営利目的で、学術団体および非学術団体が自由に利用できるようになっています。 
私のライセンス条項に同意すると、AnimeGANの使用が許可されます。 商用利用のリクエストについては、承認書を入手するためにメールでご連絡ください。
## 著者   
Xin Chen, Gang Liu, Jie Chen   
## 感謝  
このコードは[CartoonGAN-Tensorflow](https://github.com/taki0112/CartoonGAN-Tensorflow/blob/master/CartoonGAN.py) と [Anime-Sketch-Coloring-with-Swish-Gated-Residual-UNet](https://github.com/pradeeplam/Anime-Sketch-Coloring-with-Swish-Gated-Residual-UNet) に基づいています。彼らの貢献に感謝します。  

