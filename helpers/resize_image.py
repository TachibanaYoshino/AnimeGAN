import numpy as np
import cv2, os, argparse
from tqdm import tqdm

def parse_args():
    desc = "Resize images in folder"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--image_dir', type=str, default='', help='imagedir')
    parser.add_argument('--save_dir', type=str, default=None, help='save dir')
    parser.add_argument('--img_size', type=int, default=256, help='The size of image')
    parser.add_argument('--four_frames', type=bool, default=False)

    return parser.parse_args()

def get_four_cropped_frames(bgr_img,img_size):
    height, width, channels = bgr_img.shape

    if(height == width):
        frame_1 = bgr_img[0 : int(height/2),  0 : int(width/2)]
        frame_2 = bgr_img[0 : int(height/2), int(width/2) : height]
        frame_3 = bgr_img[int(height/2)  : height, 0 : int(width/2)]
        frame_4 = bgr_img[int(height/2) : height, int(width/2) : width]
        return [frame_1,frame_2,frame_3,frame_4]
    else:
        print("Error frame is not square")
        exit()

def resize(image_dir, save_dir, img_size, four_frames=False) :
    for f in os.listdir(image_dir) :
        file_name = os.path.splitext(os.path.basename(f))[0]
        if(os.path.isfile(os.path.join(image_dir, f))):
            bgr_img = cv2.imread(os.path.join(image_dir, f))
            if bgr_img is None:
                print("No image opened")
                continue

            height, width, channels = bgr_img.shape
            max_size = min(height,width)
            if(max_size == height): #horizontal image
                mid_width = width / 2
                upper_left = (int(mid_width - (max_size/2)), 0)
                bottom_right = (int(mid_width + (max_size/2)), max_size)
            else:
                mid_height = height / 2
                upper_left = (0, int(mid_height - (max_size/2)))
                bottom_right = (max_size, int(mid_height + (max_size/2)))
            bgr_img = bgr_img[upper_left[1] : bottom_right[1], upper_left[0] : bottom_right[0]]

            if(four_frames):
                frames = get_four_cropped_frames(bgr_img,img_size)
                for i,bgr_img in enumerate(frames):
                    output_name = file_name + "_" + str(i) + ".jpg"
                    bgr_img = cv2.resize(bgr_img, (img_size, img_size))
                    cv2.imwrite(os.path.join(save_dir, output_name), bgr_img)
            else:
                output_name = file_name + "_" + str(img_size) + ".jpg"
                bgr_img = cv2.resize(bgr_img, (img_size, img_size))
                cv2.imwrite(os.path.join(save_dir, output_name), bgr_img)


if __name__ == '__main__':
    # parse arguments
    args = parse_args()
    if args is None:
        print("error")
        exit()
    if args.image_dir is None:
        print("Error, no image folder")
    if args.save_dir is None:
        args.save_dir = os.path.join(args.image_dir, "resized")
        if not os.path.exists(args.save_dir): os.makedirs(args.save_dir)
    resize(args.image_dir, args.save_dir, args.img_size,args.four_frames)
