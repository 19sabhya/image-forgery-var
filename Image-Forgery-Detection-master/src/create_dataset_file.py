import numpy as np
import sys
import os
import random


def create_dataset_file(myDir):
	data_csv_file = open("../images/tpImages.csv", "w")
	format_ = ['.JPG' , '.jpg', 'jpeg', '.png', '.tiff', '.TIFF', '.Tiff', '.Tif', '.TIF', '.tif', '.bmp']
	
	for root, dirs, files in os.walk(myDir, topdown=False):
		for name in files:
			for type_ in format_:
				if name.endswith(type_):
					fullName = os.path.join(root, name)
          print('f: ', fullName)
					data_csv_file.write("%s\n" % (fullName))
					break
  			
	data_csv_file.close()
