import cPickle
import gzip

def unzip_file(file_name):
	print("Loading..........")
	f = gzip.open(file_name, 'rb')
	return cPickle.load(f)


