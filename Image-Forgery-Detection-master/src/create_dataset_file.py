import numpy as np
import sys
import os

import detect
import subprocess

if __name__ == '__main__':
  
  data_csv_file = open("../images/tpImages.csv", "w")
  format_ = ['.JPG' , '.jpg', 'jpeg', '.png', '.tiff', '.TIFF', '.Tiff', '.Tif', '.TIF', '.tif', '.bmp']
  print('hi')
  for root, dirs, files in os.walk('..//images//', topdown=False):
    for name in files:
      for type_ in format_:
        if name.endswith(type_):
          fullName = os.path.join(root, name)
          data_csv_file.write("%s\n" % (fullName))
          break
  
  data_csv_file.close()
  tpImagePaths = open('..//images//tpImages.csv', 'r').readlines()
  tpImagePaths = sorted(tpImagePaths)
  for imagePath in tpImagePaths:
    a = imagePath.strip().rsplit('//', 1)
    subprocess.check_output(['python', 'detect.py', str(a[1])])
