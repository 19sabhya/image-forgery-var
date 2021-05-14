import cv2
import sys
import time
import double_jpeg_compression
import copy_move_cfa
import copy_move_detection
import noise_variance
import ela_extractor
import create_dataset_file

from optparse import OptionParser

if __name__ == '__main__':
    
  create_dataset_file.create_dataset()
  tpImagePaths = open('..//images//tpImages.csv', 'r').readlines()
  tpImagePaths = sorted(tpImagePaths)
  for imagePath in tpImagePaths:
    a = imagePath.strip().rsplit('//', 1)
    
    startTimestamp = time.time()
    
    
    print('\nDouble jpeg compression: ')
    double_compressed = double_jpeg_compression.detect('..//images//' + a[1])

    if(double_compressed): print('\tTRUE')
    else: print('\tFALSE')
        
    print('\nELA: ')
    ela = ela_extractor.getELA('..//images//', a[1], '..//output//')

    print('\nNoise variance inconsistency: ')
    noise_forgery = noise_variance.detect('..//images//' + a[1])

    if(noise_forgery): print('\tTRUE')
    else: print('\tFALSE')

    
    print('\nCopy-move regions: ')
    count_cmf=0
    #if(not double_compressed):
    count_cmf = copy_move_detection.detect('..//images//', a[1], '..//output//', blockSize=32)
    print('\n\t', count_cmf, 'identical regions detected')

    if ((not double_compressed) and (not noise_forgery) and (count_cmf == 0)):
        print('\nNo forgeries were detected - this image has probably not been tampered with.')
    else:
        print('\nSome forgeries were detected - this image may have been tampered with.')

    timestampAfterImageCreation = time.time()
    totalRunningTimeInSecond = timestampAfterImageCreation - startTimestamp
    totalMinute, totalSecond = divmod(totalRunningTimeInSecond, 60)
    totalHour, totalMinute = divmod(totalMinute, 60)
    print("\tTotal time    : %d:%02d:%02d second" % (totalHour, totalMinute, totalSecond), '\n')

    double_compressed = False
    noise_forgery = False
    count_cmf = 0
        
