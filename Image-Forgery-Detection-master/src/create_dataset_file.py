import numpy as np
import sys
import os
import shlex

import detect
import subprocess

def create_dataset():
  
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
