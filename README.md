# AnimeGAN
A Tensorflow implementation of AnimeGAN for fast photo animation  !!!
  
-----  
This is the Open source of the paper <AnimeGAN: >, which uses the GAN framwork to transform real-world photos into anime images.  
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
### 1. Download vgg19  
> [vgg19.npy](https://mega.nz/#!xZ8glS6J!MAnE91ND_WyfZ_8mvkuSa2YcA7q-1ehfSm-Q1fxOvvs)  

### 2. Download dataset  
> Link:  

### 3. Do edge_smooth  
  eg. `python edge_smooth.py --dataset Haoyao --img_size 256`  
  
### 3. Train  
  eg. `python main.py --phase train --dataset Haoyao --epoch 100 --init_epoch 1`  
  
### 4. Test  
  eg. `python main.py --phase test --dataset Hayao`  
  or `python test.py --checkpoint_dir checkpoint/NijigenGAN_Shinkai_lsgan_300_300_1_3_10 --test_dir dataset/test/real --style_name H`  
  
____  
## Results  
