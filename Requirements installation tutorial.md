1. Linux os (Ubuntu 16.04 or 18.04), Nvidia GPU (1080ti, Titan xp) , Install GPU Driver  
2. Use Anaconda or Miniconda to build python environment. The Miniconda version I used can be downloaded [here](https://github.com/TachibanaYoshino/AnimeGAN/releases/tag/Miniconda).  
3. Install CUDA in conda command window : `conda install cudatoolkit=9.0` , Then install cudnn : `conda install cudnn=7.1.3`  
4. Install other requirements by pip command, such as `pip install tensorflow-gpu==1.8.0`, `pip install tqdm`, `pip install glob` and so on.  
5. Place the downloaded dataset in the corresponding directory, and then perform training and testing.  

