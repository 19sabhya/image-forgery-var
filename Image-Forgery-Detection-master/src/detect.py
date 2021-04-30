import cv2
import sys

import double_jpeg_compression
import copy_move_cfa
import copy_move_detection
import noise_variance

from optparse import OptionParser

if __name__ == '__main__':
    # copy-move parameters
    cmd = OptionParser("usage: %prog image_file [options]")
    cmd.add_option('', '--imauto', help='Automatically search identical regions. (default: %default)', default=1)
    cmd.add_option('', '--imblev',help='Blur level for degrading image details. (default: %default)', default=8)
    cmd.add_option('', '--impalred',help='Image palette reduction factor. (default: %default)', default=15)
    cmd.add_option('', '--rgsim', help='Region similarity threshold. (default: %default)', default=5)
    cmd.add_option('', '--rgsize',help='Region size threshold. (default: %default)', default=1.5)
    cmd.add_option('', '--blsim', help='Block similarity threshold. (default: %default)',default=200)
    cmd.add_option('', '--blcoldev', help='Block color deviation threshold. (default: %default)', default=0.2)
    cmd.add_option('', '--blint', help='Block intersection threshold. (default: %default)', default=0.2)
    opt, args = cmd.parse_args()
    if not args:
        cmd.print_help()
        sys.exit()
    im_str = args[0]
    
    print('\nRunning double jpeg compression detection...')
    cv2.imshow('img', im_str)
    
    
