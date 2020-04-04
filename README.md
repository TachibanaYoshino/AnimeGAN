# AnimeGAN
A Tensorflow implementation of AnimeGAN for fast photo animation  !!!

-----
This is the Open source of the paper <AnimeGAN: a novel lightweight GAN for photo animation>, which uses the GAN framwork to transform real-world photos into anime images.  

**Some suggestions:** since the real photos in the training set are all landscape photos, if you want to stylize the photos with people as the main body, you may as well add at least 3000 photos of people in the training set and retrain to obtain a new model.  

The code has been tested with Python 3.6.8 and CUDA 9.0 on Ubuntu 18.04 LTS.

___

## Requirements  
```
numpy
scipy
opencv-python
tensorflow-gpu==1.8
tqdm
```

## CUDA 9.0 Installation

Credits to [this post](https://medium.com/@yifanguo1129/install-cuda-9-0-and-cudnn-7-2-on-ubuntu-18-04-d9a7aeb89105) of [Yifan Guo](https://medium.com/@yifanguo1129). The script is only slightly modified.

1. Verify that your GPU is CUDA enabled with `lspci | grep -i nvidia`. 

2. Check that you have `gcc` installed with `gcc --version`. If it is not installed, run `sudo apt install gcc`.

3. Run `cuda-install.sh`. Pay attention, you will be asked some questions after you have accepted the EULA.

4. Reply `y` to the question 

   ```
   # You are attempting to install on an unsupported configuration. Do you wish to continue? 
   ```

   **Reply `n` to the question**

   ```
   # Install NVIDIA Accelerated Graphics Driver for Linux-x86_64 384.81?
   ```

   Reply `y` to the question

   ```
   Install the CUDA 9.0 Toolkit?
   ```

5. After `CUDA INSTALLATION DONE` is printed on the screen, run the following lines in the terminal:

   ```
   source ~/.bashrc
   echo 'export PATH=/usr/local/cuda-9.0/bin:$PATH' >> ~/.bashrc
   echo 'export LD_LIBRARY_PATH=/usr/local/cuda-9.0/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc
   ```

6. Download cuDNN: in order to do this, you have to register [here](https://developer.nvidia.com/developer-program/signup) and then download cuDNN. In our case we can use cuDNN v7.6.4.  The downloaded file should be named `cudnn-9.0-linux-x64-v7.6.4.38.tgz`. Put the file you downloaded in the `AnimeGAN` folder.

7. Run `cudnn-install.sh`

8. Reboot the machine with `sudo reboot`

9. Verify the installation by running:

   ```
   nvidia-smi
   nvcc -V
   ```

## Usage  

### 1. Download vgg19 or Pretrained model  
> [vgg19.npy](https://github.com/TachibanaYoshino/AnimeGAN/releases/tag/vgg16%2F19.npy)  

> [Pretrained model](https://github.com/TachibanaYoshino/AnimeGAN/releases/tag/Haoyao-style_V1.0)  

### 2. Download dataset  
> [Link](https://github.com/TachibanaYoshino/AnimeGAN/releases/tag/dataset-1)  

### 3. Do edge_smooth  
  eg. `python edge_smooth.py --dataset Haoyao --img_size 256`  

### 3. Train  
  eg. `python main.py --phase train --dataset Haoyao --epoch 101 --init_epoch 1`  

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
## Process your own images

1. Download the pretrained model with `wget https://github.com/TachibanaYoshino/AnimeGAN/releases/download/Haoyao-style_V1.0/Haoyao-style.zip`
2. Create a folder named checkpoint `mkdir checkpoint` and unzip the `Haoyao-style.zip` there.
3. Create a folder called `mypics` inside the `dataset/test` folder and put the images you want to process there.
4. Run `python3 test.py --checkpoint_dir checkpoint/ --test_dir dataset/test/mypics --style_name H`



## Acknowledgment  

This code is based on the [CartoonGAN-Tensorflow](https://github.com/taki0112/CartoonGAN-Tensorflow/blob/master/CartoonGAN.py) and [Anime-Sketch-Coloring-with-Swish-Gated-Residual-UNet](https://github.com/pradeeplam/Anime-Sketch-Coloring-with-Swish-Gated-Residual-UNet). Thanks to the contributors of this project.  

