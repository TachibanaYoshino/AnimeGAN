#!/bin/bash
# CREDITS: https://medium.com/@yifanguo1129/install-cuda-9-0-and-cudnn-7-2-on-ubuntu-18-04-d9a7aeb89105
## This gist contains step by step instructions to install cuda v9.0 and cudnn 7.2 in ubuntu 18.04
### steps ###
# verify the system has a cuda-capable gpu
# download and install the nvidia cuda toolkit and cudnn
# setup environmental variables
# verify the installation

# get the PPA repository driver
sudo add-apt-repository ppa:graphics-drivers/ppa
# install nvidia driver
sudo apt install nvidia-384 nvidia-384-dev
# install other import packages
sudo apt-get install g++ freeglut3-dev build-essential libx11-dev libxmu-dev libxi-dev libglu1-mesa libglu1-mesa-dev
# CUDA 9 requires gcc 6
sudo apt install gcc-6
sudo apt install g++-6
# download one of the "runfile (local)" installation packages from cuda toolkit archive
wget https://developer.nvidia.com/compute/cuda/9.0/Prod/local_installers/cuda_9.0.176_384.81_linux-run# make the download file executable
chmod +x cuda_9.0.176_384.81_linux-run 
sudo ./cuda_9.0.176_384.81_linux-run --override
# Answer following questions while installation begin
# You are attempting to install on an unsupported configuration. Do you wish to continue? y
# Install NVIDIA Accelerated Graphics Driver for Linux-x86_64 384.81? n
# Install the CUDA 9.0 Toolkit? y
# set up symlinks for gcc/g++
sudo ln -s /usr/bin/gcc-6 /usr/local/cuda/bin/gcc
sudo ln -s /usr/bin/g++-6 /usr/local/cuda/bin/g++
echo "CUDA INSTALLATION DONE"
