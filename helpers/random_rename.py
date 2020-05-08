import os 
import argparse
import uuid

def parse_args():
    desc = "Rename files to random uuid"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--dir', type=str, default='Paprika', help='dataset_name')

    return parser.parse_args()

if __name__ == '__main__':
    arg = parse_args()
    if not arg.dir:
        print("no directory specified")
    for filename in os.listdir(arg.dir):
        extension = os.path.splitext(filename)[1]
        new_filename = arg.dir + '/' + str(uuid.uuid4()) + extension
        os.rename(arg.dir + '/' + filename, new_filename)