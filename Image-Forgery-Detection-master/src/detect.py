import cv2
import sys
import time
import double_jpeg_compression
import copy_move_cfa
import copy_move_detection
import noise_variance
import ela_extractor

from optparse import OptionParser

def detect(cmf):
    cmf= 
    # copy-move parameters
    cmf = OptionParser("usage: %prog image_file [options]")
    cmf.add_option('', '--imauto', help='Automatically search identical regions. (default: %default)', default=1)
    cmf.add_option('', '--imblev',help='Blur level for degrading image details. (default: %default)', default=8)
    cmf.add_option('', '--impalred',help='Image palette reduction factor. (default: %default)', default=15)
    cmf.add_option('', '--rgsim', help='Region similarity threshold. (default: %default)', default=5)
    cmf.add_option('', '--rgsize',help='Region size threshold. (default: %default)', default=1.5)
    cmf.add_option('', '--blsim', help='Block similarity threshold. (default: %default)',default=200)
    cmf.add_option('', '--blcoldev', help='Block color deviation threshold. (default: %default)', default=0.2)
    cmf.add_option('', '--blint', help='Block intersection threshold. (default: %default)', default=0.2)
    opt, args = cmf.parse_args()
    if not args:
        cmf.print_help()
        sys.exit()
    im_str = args[0]
    print(im_str)
    
    startTimestamp = time.time()
    
    print('\nDouble jpeg compression: ')
    double_compressed = double_jpeg_compression.detect('..//images//' + im_str)

    print('\nELA: ')
    ela = ela_extractor.getELA('..//images//', im_str, '..//output//')


    if(double_compressed): print('\tTRUE')
    else: print('\tFALSE')
        
    print('\nCFA artifact count: ')
    identical_regions_cfa = copy_move_cfa.detect('..//images//' + im_str, opt, args)
    print('\t', identical_regions_cfa, 'CFA artifacts detected')

    print('\nNoise variance inconsistency: ')
    noise_forgery = noise_variance.detect('..//images//' + im_str)

    if(noise_forgery): print('\tTRUE')
    else: print('\tFALSE')

    
    print('\nCopy-move regions: ')
    count_cmf=0
    if(not double_compressed):
      count_cmf = copy_move_detection.detect('..//images//', im_str, '..//output//', blockSize=32)
    print('\n\t', count_cmf, 'identical regions detected')

    if ((not double_compressed) and (identical_regions_cfa == 0) and (not noise_forgery) and (count_cmf == 0)):
        print('\nNo forgeries were detected - this image has probably not been tampered with.')
    else:
        print('\nSome forgeries were detected - this image may have been tampered with.')

    timestampAfterImageCreation = time.time()
    totalRunningTimeInSecond = timestampAfterImageCreation - startTimestamp
    totalMinute, totalSecond = divmod(totalRunningTimeInSecond, 60)
    totalHour, totalMinute = divmod(totalMinute, 60)
    print("\tTotal time    : %d:%02d:%02d second" % (totalHour, totalMinute, totalSecond), '\n')
        
