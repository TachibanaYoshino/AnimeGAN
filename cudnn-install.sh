#!/bin/bash
# CREDITS: https://medium.com/@yifanguo1129/install-cuda-9-0-and-cudnn-7-2-on-ubuntu-18-04-d9a7aeb89105
# install cuDNN v7.6.4
# NB: change this if you use a different version
CUDNN_TAR_FILE="cudnn-9.0-linux-x64-v7.6.4.38.tgz"
tar -xzvf ${CUDNN_TAR_FILE}
# copy the following files into the cuda toolkit directory.
sudo cp -P cuda/include/cudnn.h /usr/local/cuda-9.0/include
sudo cp -P cuda/lib64/libcudnn* /usr/local/cuda-9.0/lib64/
sudo chmod a+r /usr/local/cuda-9.0/lib64/libcudnn*
