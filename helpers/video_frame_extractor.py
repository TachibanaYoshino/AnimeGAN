import cv2
import argparse
import os
import math
def parse_args():
    desc = "Extract frames from video"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--video', type=str, default=None,
                       help='video file or number for webcam')
    parser.add_argument('--output', type=str, default='extracted_frames',
                        help='output path')
    parser.add_argument('--prefix', type=str, default='test',
                        help='output files name prefix')
    parser.add_argument('--interval', type=int, default=2,
                        help='screen capture interval')

    return parser.parse_args()


if __name__ == '__main__':
    arg = parse_args()
    output_folder = arg.output
    if not os.path.exists(output_folder): os.makedirs(output_folder)
    output_prefix = arg.prefix
    if not arg.video:
        print("Error : no video file")
        exit()
    if not arg.interval:
        print("Not screen cap interval set, default to 2 secs")
    # Opens the Video file
    cap = cv2.VideoCapture(arg.video)
    fps = math.ceil(cap.get(cv2.CAP_PROP_FPS))
    print(fps)
    success,frame = cap.read()
    i=0
    j=0
    while success:
        if i % (fps * arg.interval) == 0:
            print(i)
            ret, frame = cap.read()
            if ret == False:
                break
            laplacian_var = cv2.Laplacian(frame, cv2.CV_64F).var()
            cv2.imwrite(output_folder + '/' + output_prefix + "_" + str(j)+'.jpg',frame)
            j+=1
        success,frame = cap.read()
        i+=1
     
    cap.release()
    cv2.destroyAllWindows()