import scipy as sci

def sliding_window(image_matrix, window_row, window_col):
	image_row = image_matrix.shape[0]
	image_col = image_matrix.shape[1]

	for row in range(0, image_row - window_row):
		for col in range(0, image_col - window_col):
			sub_image_matrix = image_matrix[row:row + window_row, col:col + window_col]
			file_name = "output//row_" + str(row).zfill(3) + "_col_" + str(col).zfill(3) + ".png"
			sci.misc.imsave(file_name, sub_image_matrix)
			







