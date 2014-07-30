'''
Created on Jul 10, 2014

@author: bhattarai
'''

import Image;
from theano.tensor.nnet import conv, sigmoid
from theano import tensor, shared
import numpy
import theano

class convolution():
    
    def initalize_tensor_input(self):
        return tensor.tensor4(name = 'input')
    
    def transfrom_kernel_img(self,file_name, tensor_input):
        w_shp = (1,1,39,24)
        kernel_image = numpy.asarray(Image.open(file_name).convert('L'), dtype = tensor_input.dtype)
        kernel_image = numpy.reshape(kernel_image, w_shp)
        kernel_image = (kernel_image - 128) / 128
        return kernel_image
    
    def get_shared_kernel_img(self, kernel_image):
        return shared(kernel_image, name = 'W')
    
    def get_conv_kernel_img(self,tensor_input,W):
        return conv.conv2d(tensor_input, W)
    
    def get_sigmoid_kernel_img(self, conv_out):
        sigmoid(conv_out)
        
    def get_conv_filtered_image(self, tensor_object, conv_kernel):
        return theano.function([tensor_object], conv_kernel)
    
    def get_sigmoid_filtered_image(self, tensor_object, sigmoid_kernel):
        return theano.function([tensor_object], sigmoid_kernel)
        

        

