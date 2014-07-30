from sys import argv
import os
import Image
from  numpy import matrix
from scipy import misc
import pdb

def image_to_matrix(file_name):
		img_matrix = matrix(Image.open(file_name).convert('L'))
		return img_matrix

def sliding_window(image_matrix,window_row, window_col, output_dir):
	image_row = image_matrix.shape[0]
	image_col = image_matrix.shape[1]
	#pdb.set_trace()
	os.mkdir("../data/"+ output_dir)

	for row in range(0, image_row - window_row):
		for col in range(0, image_col - window_col):
			sub_image_matrix = image_matrix[row:row + window_row, col:col + window_col]
			file_name = "../data/"+ output_dir + "/" + "row_"+ str(row).zfill(3) +"_col_" + str(col).zfill(3) + ".png"
			misc.imsave(file_name, sub_image_matrix)



	# for col in range(0, image_col - window_col):
	# 	sub_image_matrix = image_matrix[range(0,40), col:col + window_col]
	# 	file_name = "../data/"+ output_dir + "/" + "col_" + str(col).zfill(3) + ".png"
	# 	misc.imsave(file_name, sub_image_matrix)
		

def main(file_name):
	image_matrix = image_to_matrix("../data/images_rs11/" + file_name)
	sliding_window(image_matrix, window_row = 40, window_col = 25, output_dir = str.split(file_name, ".")[0])


if __name__ == "__main__":
	files_list = os.listdir("../data/images_rs11")
	for file in files_list:
		main(file)



