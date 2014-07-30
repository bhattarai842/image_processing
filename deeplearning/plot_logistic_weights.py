import cPickle
import gzip
import pylab
'''
Created on Jul 14, 2014

@author: bhattarai
'''
class plot_logistic_weight:
    @staticmethod
    def unzip_file(file_name):
        print("Loading..........")
        f = gzip.open(file_name, 'rb')
        return cPickle.load(f)
    
    @staticmethod
    def plot_weights(data_tuple, col_index = 0):
        weight, bias = data_tuple
        weight = weight.eval()[:,col_index]
        weight_to_plot = weight.reshape((40, 25))
        pylab.imshow(weight_to_plot)
        pylab.gray()
        pylab.axis("off")
        pylab.show()
        
    @staticmethod
    def plot():
        datasets = plot_logistic_weight.unzip_file('../data/digit_id_weights.pkl.gz')
        plot_logistic_weight.plot_weights(datasets, 0)

      
if __name__ == "__main__":
    plot_logistic_weight.plot()

       
    