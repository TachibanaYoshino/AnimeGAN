# AnimeGAN
A Tensorflow implementation of AnimeGAN for fast photo animation  !!!
  
-----  
This is the Open source of the paper <AnimeGAN: a novel lightweight GAN for photo animation>, which uses the GAN framwork to transform real-world photos into anime images.  
  
**Some suggestions:** since the real photos in the training set are all landscape photos, if you want to stylize the photos with people as the main body, you may as well add at least 3000 photos of people in the training set and retrain to obtain a new model.  
  
**News:** AnimeGAN+ is expected to be released this summer. After some simple tricks were added to AnimeGAN, the obtained AnimeGAN+ has better animation effects. When I return to school to graduate, more pre-trained models and video animation test code will also be released in this repository.  

___  

## Requirements  
- python 3.6.8  
- tensorflow-gpu 1.8  
- opencv  
- tqdm  
- numpy  
- glob  
- argparse  
  
## Usage  
### 1. Download vgg19 or Pretrained model  
> [vgg19.npy](https://github.com/TachibanaYoshino/AnimeGAN/releases/tag/vgg16%2F19.npy)  
  
> [Pretrained model](https://github.com/TachibanaYoshino/AnimeGAN/releases/tag/Haoyao-style_V1.0)  

### 2. Download dataset  
> [Link](https://github.com/TachibanaYoshino/AnimeGAN/releases/tag/dataset-1)  

### 3. Do edge_smooth  
  eg. `python edge_smooth.py --dataset Hayao --img_size 256`  
  
### 3. Train  
  eg. `python main.py --phase train --dataset Hayao --epoch 101 --init_epoch 1`  
  
### 4. Test  
  eg. `python main.py --phase test --dataset Hayao`  
  or `python test.py --checkpoint_dir checkpoint/AnimeGAN_Hayao_lsgan_300_300_1_3_10 --test_dir dataset/test/real --style_name H`  
  
____  
## Results  
------> pictures from the paper 'AnimeGAN: a novel lightweight GAN for photo animation'  
![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/doc/sota.png)  
![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/doc/e2.png)  
![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/doc/e3.png)  
![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/doc/e4.png)  

------> Photo  to  Hayao  Style  
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
## Acknowledgment  
This code is based on the [CartoonGAN-Tensorflow](https://github.com/taki0112/CartoonGAN-Tensorflow/blob/master/CartoonGAN.py) and [Anime-Sketch-Coloring-with-Swish-Gated-Residual-UNet](https://github.com/pradeeplam/Anime-Sketch-Coloring-with-Swish-Gated-Residual-UNet). Thanks to the contributors of this project.  

