from sys import argv
import zbar
import Image

class barcode_reader:

    @staticmethod
    def get_image(file_name):
        in_img = None
        try:
            in_img = Image.open(file_name).convert('L')
        except Exception as e:
            print str(e)
        return in_img

    @staticmethod
    def wrap_image(in_img):
        width, height = in_img.size
        raw = in_img.tostring()
        image = zbar.Image(width, height, 'Y800', raw)
        return image



    @staticmethod
    def scan_image(image):
        scanner = zbar.ImageScanner()
        scanner.parse_config('enable')
        scanner.scan(image)

    @staticmethod
    def get_info(image):
        for symbol in image:
            #print ' ** Decoded', symbol.type, "symbol" , '"%s"' %symbol.data
            if str(symbol.type) == "CODE128":
                return str(symbol.data)




def main(image_url):
    obj = barcode_reader()
    input_image = obj.get_image(image_url)
    barcode_value = []
    if input_image:
        image = obj.wrap_image(input_image)
        obj.scan_image(image)
        barcode_value = obj.get_info(image)

    return barcode_value

# if '__name__' == '__main__':
#     obj = barcode_reader()
#     input_image = obj.get_image(argv[0])
#     image = obj.wrap_image(input_image)
#     obj.scan_image(image)
#     obj.get_info(image)