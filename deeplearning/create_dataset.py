from numpy import matrix, array, int
from PIL import Image
from theano import shared, tensor
import random, pickle, gzip, theano


class dataset_creation:
	@staticmethod
	def create_dataset(image_matrix, window_row = 40, window_col = 25):
		image_row = image_matrix.shape[0]
		image_col = image_matrix.shape[1]
		train_set_x = []
		train_set_y = []
		y_true_row = range(17, 55)
		y_true_col = (15, 16, 17, 43, 44, 45, 71, 72, 73, 105, 106, 107, 136, 137, 138, 162, 163, 164, 196, 197, 198)
		
		for row in range(0, image_row - window_row):
			for col in range(0, image_col - window_col):
				sub_image_matrix = image_matrix[row:row + window_row, col:col + window_col]
			
				sub_img_list = dataset_creation.sub_image_to_list(sub_image_matrix)
				train_set_x.append(sub_img_list)
				y_append_bool = row in y_true_row and col in y_true_col
				train_set_y.append(y_append_bool if 1 else 0)
		
		dataset = dataset_creation.data_set_partation(train_set_x, train_set_y)
		return dataset	
		
	@staticmethod
	def image_to_matrix(file_name):
		img_matrix = matrix(Image.open(file_name).convert('L'))
		return img_matrix
	@staticmethod
	def sub_image_to_list(sub_image_matrix):
		return sub_image_matrix.reshape(-1).tolist().pop()
	@staticmethod
	def data_set_partation(dataset_x, dataset_y):
		dataset_size = len(dataset_x)
		index_shuffle = range(0,dataset_size)
		random.shuffle(index_shuffle)
		train_size =  int(0.6 * dataset_size)
		test_size = int(0.2 * dataset_size)
		validation_size = int(0.2 * dataset_size)
		
		
		train_dataset_x = dataset_creation.shuffle_data(dataset_x, index_shuffle, 
													start_index = 0, 
													end_index = train_size)
		test_dataset_x =  dataset_creation.shuffle_data(dataset_x, 
													index_shuffle, 
													start_index = train_size + 1, 
													end_index = train_size + test_size)
		validation_dataset_x = dataset_creation.shuffle_data(dataset_x, 
															index_shuffle, 
															start_index = train_size + test_size+ 1,
															 end_index = train_size + test_size + validation_size)
		
		train_dataset_y = dataset_creation.shuffle_data(dataset_y, index_shuffle, 
													start_index = 0, 
													end_index = train_size)
		test_dataset_y =  dataset_creation.shuffle_data(dataset_y, 
													index_shuffle, 
													start_index = train_size + 1, 
													end_index = train_size + test_size)
		validation_dataset_y = dataset_creation.shuffle_data(dataset_y, 
															index_shuffle, 
															start_index = train_size + test_size+ 1,
															end_index = train_size + test_size + validation_size)
		
		
		train_dataset = (train_dataset_x, train_dataset_y)
		test_dataset = (test_dataset_x, test_dataset_y)
		validation_dataset = (validation_dataset_x, validation_dataset_y)
		return (train_dataset, test_dataset, validation_dataset)
		
	
	@staticmethod
	def shuffle_data(dataset, index_shuffle, start_index, end_index):
		shuffle_list = [ dataset[index] for index in index_shuffle[start_index:end_index]]
		return shuffle_list
	
	@staticmethod
	def dataset_to_pickle(dataset):
		print("m")
		f = gzip.GzipFile(".//data//dataset_digit_sep.pkl.gz", 'wb')
		f.write(pickle.dumps(dataset, 0))
		f.close()
		