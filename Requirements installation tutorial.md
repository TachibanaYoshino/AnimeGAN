1. Linux os (Ubuntu 18.04 or 20.04), Nvidia GPU (e.g. 2080ti) , Install GPU Driver  
2. Use Anaconda or Miniconda to build python environment. The Miniconda version I used can be downloaded [here](https://repo.anaconda.com/miniconda/Miniconda3-py37_4.9.2-Linux-x86_64.sh).  
3. Install CUDA in conda command window : `conda install cudatoolkit=10` , Then install cudnn : `conda install cudnn=7.6.0`  
4. Install other requirements by pip command, such as `pip install tensorflow-gpu==1.15.0`, `pip install tqdm`, `pip install glob` and so on.  
5. Place the downloaded dataset in the corresponding directory, and then perform training and testing.  

