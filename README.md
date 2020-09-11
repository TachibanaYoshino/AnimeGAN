# AnimeGAN   
[**AnimeGANv2, the improved version of AnimeGAN.**](https://github.com/TachibanaYoshino/AnimeGANv2)  
A Tensorflow implementation of AnimeGAN for fast photo animation ! &ensp;&ensp;&ensp;&ensp;[日本語](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/doc/Japanese_README.md)  
The paper can be accessed [here](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/doc/Chen2020_Chapter_AnimeGAN.pdf) or on the [website](https://link.springer.com/chapter/10.1007/978-981-15-5577-0_18).  

**Update:**  
1. `data_mean.py` is used to calculate the three-channel(BGR) color difference of the entire style data, and these difference values are used to balance the effect of the tone of the style data on the generated image during the training process. For example, the overall tone of the Hayao style data is yellowish.   
2. `adjust_brightness.py` is used to adjust the brightness of the generated image, which is based on the brightness of the input photo.   
3. Some training hyperparameter changes.   

**Online access**:  Be grateful to [@TonyLianLong](https://github.com/TonyLianLong/AnimeGAN.js) for developing an online access project, you can implement photo animation through a browser without installing anything, [click here to have a try](https://animegan.js.org/).  
  
**Good news**:  tensorflow-1.15.0 is compatible with the code of this repository. In this version, you can run this code without any modification. [The premise is that the CUDA and cudnn corresponding to the tf version are correctly installed](https://tensorflow.google.cn/install/source#gpu). Maybe the versions between tf-1.8.0 and tf-1.15.0 are also supported and compatible with this repository, but I didn’t make too many extra attempts.  

  
-----  
  
**Some suggestions:**   
1. since the real photos in the training set are all landscape photos, if you want to stylize the photos with people as the main body, you may as well add at least 3000 photos of people in the training set and retrain to obtain a new model.  
2. In order to obtain a better face animation effect, when using 2 images as data pairs for training, it is suggested that the faces in the photos and the faces in the anime style data should be consistent in terms of gender as much as possible.  
3. The generated stylized images will be affected by the overall brightness and tone of the style data, so try not to select the anime images of night as the style data, and it is necessary to make an exposure compensation for the overall style data to promote the consistency of brightness and darkness of the entire style data.  

**News:**   
&ensp;&ensp;&ensp;&ensp;&ensp;  ***AnimeGANv2*** has been released and can be accessed [here](https://github.com/TachibanaYoshino/AnimeGANv2).  
```yaml
The improvement directions of AnimeGANv2 mainly include the following 4 points:  
```
&ensp;&ensp; 1. Solve the problem of high-frequency artifacts in the generated image.  
&ensp;&ensp; 2. It is easy to train and directly achieve the effects in the paper.  
&ensp;&ensp; 3. Further reduce the number of parameters of the generator network.  
&ensp;&ensp; 4. Use new high-quality style data, which come from BD movies as much as possible.  

___  

## Requirements  
- python 3.6  
- tensorflow-gpu 
   - tensorflow-gpu 1.8.0  (ubuntu, GPU 1080Ti or Titan xp, cuda 9.0, cudnn 7.1.3)  
   - tensorflow-gpu 1.15.0 (ubuntu, GPU 2080Ti, cuda 10.0.130, cudnn 7.6.0)  
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
  
### 4. Calculate the three-channel(BGR) color difference  
  eg. `python data_mean.py --dataset Hayao`  
  
### 5. Train  
  eg. `python main.py --phase train --dataset Hayao --data_mean [13.1360,-8.6698,-4.4661] --epoch 101 --init_epoch 1`  
  
### 6. Extract the weights of the generator  
  eg. `python get_generator_ckpt.py --checkpoint_dir  ../checkpoint/AnimeGAN_Hayao_lsgan_300_300_1_1_10  --style_name Hayao`  
    
### 7. Test  
  eg. `python main.py --phase test --dataset Hayao`  
  or `python test.py --checkpoint_dir  checkpoint/generator_Hayao_weight  --test_dir dataset/test/real --style_name H`  
  
### 8. Convert video to anime   
  eg. `python video2anime.py  --video video/input/お花見.mp4  --checkpoint_dir  ../checkpoint/generator_Hayao_weight`  
    
____  
## Results  
:blush:  pictures from the paper - *AnimeGAN: a novel lightweight GAN for photo animation*  
  
![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/doc/sota.png)  
![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/doc/e2.png)  
![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/doc/e3.png)  
![](https://github.com/TachibanaYoshino/AnimeGAN/blob/master/doc/e4.png)  
  
:heart_eyes:  Photo  to  Hayao  Style  
  
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
____  
## License   
This repo is made freely available to academic and non-academic entities for non-commercial purposes such as academic research, teaching, scientific publications. Permission is granted to use the AnimeGAN given that you agree to my license terms. Regarding the request for commercial use, please contact us via email to help you obtain the authorization letter.  
## Author  
Xin Chen, Gang Liu, Jie Chen  
## Acknowledgment  
This code is based on the [CartoonGAN-Tensorflow](https://github.com/taki0112/CartoonGAN-Tensorflow/blob/master/CartoonGAN.py) and [Anime-Sketch-Coloring-with-Swish-Gated-Residual-UNet](https://github.com/pradeeplam/Anime-Sketch-Coloring-with-Swish-Gated-Residual-UNet). Thanks to the contributors of this project.  

