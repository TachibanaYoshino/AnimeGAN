import argparse
import os
import tkinter as tk
from tkinter import filedialog

import cv2
from tqdm import tqdm
import numpy as np
import tensorflow as tf

from net import generator
from utils import preprocessing

def parse_args():
    desc = "Tensorflow implementation of AnimeGAN"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--video', type=str, default=None,
                        help='video file or number for webcam')
    parser.add_argument('--checkpoint_dir', type=str, default='checkpoint/net_model',
                        help='Directory name to save the checkpoints')
    parser.add_argument('--output', type=str, default=None,
                        help='output path')
    parser.add_argument('--output_format', type=str, default='XVID',
                        help='codec used in VideoWriter when saving video to file')

    return parser.parse_args()
    
def getfileloc(initialdir='/', method='open', title='Please select a file', filetypes=(("video files", ".mkv .avi .mp4"), ("all files","*.*"))):
    root = tk.Tk()
    if method == 'open':
        fileloc = filedialog.askopenfilename(parent=root, initialdir=initialdir, title=title, filetypes=filetypes)
    elif method == 'save':
        fileloc = filedialog.asksaveasfilename(parent=root, initialdir=initialdir, initialfile='out.avi', title=title, filetypes=filetypes)
    root.withdraw()
    return fileloc

def convert_image(img, img_size):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = preprocessing(img, img_size)
    img = np.expand_dims(img, axis=0)
    img = np.asarray(img)
    return img
    
def inverse_image(img):
    img = (img.squeeze()+1.) / 2 * 255
    img = img.astype(np.uint8)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def stats_graph(graph):
    flops = tf.compat.v1.profiler.profile(graph, options=tf.compat.v1.profiler.ProfileOptionBuilder.float_operation())
    # params = tf.profiler.profile(graph, options=tf.profiler.ProfileOptionBuilder.trainable_variables_parameter())
    print('FLOPs: {}'.format(flops.total_float_ops))

def cvt2anime_video(video, output, checkpoint_dir, output_format='MP4V', show_stats=False, img_size=(256,256)):
    '''
    output_format: 4-letter code that specify codec to use for specific video type. e.g. for mp4 support use "H264", "MP4V", or "X264"
    '''
    # tf.reset_default_graph()
    # check_folder(result_dir)
    # gpu_stat = bool(len(tf.config.experimental.list_physical_devices('GPU')))
    # if gpu_stat:
    os.environ["CUDA_VISIBLE_DEVICES"] = "0"
    gpu_options = tf.compat.v1.GPUOptions(allow_growth=True)
    
    test_real = tf.compat.v1.placeholder(tf.float32, [1, None, None, 3], name='test')

    with tf.compat.v1.variable_scope("generator", reuse=False):
        test_generated = generator.G_net(test_real).fake
    
    # load video
    try:
        vid = cv2.VideoCapture(int(video))
    except:
        vid = cv2.VideoCapture(video)

    #width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
    #height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(vid.get(cv2.CAP_PROP_FPS))
    # codec = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
    codec = cv2.VideoWriter_fourcc(*output_format)
    
    tfconfig = tf.compat.v1.ConfigProto(allow_soft_placement=True, gpu_options=gpu_options)
    with tf.compat.v1.Session(config=tfconfig) as sess:
        # tf.global_variables_initializer().run()
        # load model
        ckpt = tf.train.get_checkpoint_state(checkpoint_dir)  # checkpoint file information
        saver = tf.compat.v1.train.Saver()
        if ckpt and ckpt.model_checkpoint_path:
            ckpt_name = os.path.basename(ckpt.model_checkpoint_path)  # first line
            saver.restore(sess, os.path.join(checkpoint_dir, ckpt_name))
            print(" [*] Success to read {}".format(ckpt_name))
        else:
            print(" [*] Failed to find a checkpoint")
            return
        
        # FLOPs
        if show_stats:
            stats_graph(tf.compat.v1.get_default_graph())
        
        # determine output width and height
        ret, img = vid.read()
        if img is None:
            print('Error! Failed to determine frame size: frame empty.')
            return         
        img = convert_image(img, img_size)
        fake_img = sess.run(test_generated, feed_dict={test_real: img})
        fake_img = inverse_image(fake_img)
        height, width = fake_img.shape[:2]
        out = cv2.VideoWriter(output, codec, fps, (width, height))

        pbar = tqdm(total=total)
        vid.set(cv2.CAP_PROP_POS_FRAMES, 0)
        while ret:
            ret, img = vid.read()
            if img is None:
                print('Warning: got empty frame.')
                continue
            
            img = convert_image(img, img_size)
            fake_img = sess.run(test_generated, feed_dict={test_real: img})
            fake_img = inverse_image(fake_img)
            # cv2.imwrite(f'results/cut_{i:03}.jpg', fake_img)
            out.write(fake_img)
            pbar.update(1)
            # cv2.imshow('output', fake_img)
            if cv2.waitKey(1) == ord('q'):
                break
        pbar.close()
        vid.release()
        cv2.destroyAllWindows()
        
if __name__ == '__main__':
    arg = parse_args()
    if not arg.video:
        arg.video = getfileloc(initialdir='input/')
    if not arg.output:
        arg.output = getfileloc(initialdir='output/', method='save')
    cvt2anime_video(arg.video, arg.output, arg.checkpoint_dir, output_format=arg.output_format)