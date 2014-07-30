import pylab
import cPickle
import gzip
import numpy


'''
Created on Jul 15, 2014

@author: bhattarai
'''

class plot_mlp_weights:
    @staticmethod
    def unzip_file(file_name):
        print("Loading..........")
        f = gzip.open(file_name, 'rb')
        return cPickle.load(f)
    
    @staticmethod
    def plot_hidden_weight(dataset):
        hidden_weight, bias = dataset[0] 
        hidden_weight = hidden_weight.eval()
        
#         pylab.subplot((20, 5))
#         
#         for file_index in range(0, 5):
#             file_name = "..//output//mlp_hidden_" + str(file_index) + ".png"
#             base = 100 * file_index
#             pylab.gray()
#             pylab.figure(figsize = (10, 10))
#             pylab.subplots_adjust( left = None, bottom = None, right = None, top = None, wspace = None, hspace = None)
#             for index in range(0, 100):
#                 image_matrix = numpy.reshape(hidden_weight[:,(base + index)], (40 , 25))
#                 pylab.subplot(20,5, index)
#                 pylab.axis("off")
#                 pylab.imshow(image_matrix)
#                 print str(index +1) + " col image saved in "+ str(file_index) + " plot"
#                 
#             pylab.savefig(file_name)
#             pylab.close()
        for file_index in range(0, 500):
            file_name = "..//sundar_dai//mlp_hidden_" + str(file_index) + ".png"
            pylab.gray()
            image_matrix = numpy.reshape(hidden_weight[:,file_index], (40 , 25))
            pylab.axis("off")
            pylab.imshow(image_matrix)
            print str(file_index) + " image saved"
            pylab.savefig(file_name)
            pylab.close()
             
             
if __name__ == "__main__":
    file_name = '..//data//sundar_dai_mlp_weights.pkl.gz'
    dataset = plot_mlp_weights.unzip_file(file_name)
    plot_mlp_weights.plot_hidden_weight(dataset)
    print "Status Completed"
        
        
        