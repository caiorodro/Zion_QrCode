import os
from barcode import Code128
from barcode.writer import ImageWriter

from PIL import Image

class ZionBarCode:

    def __init__(self):
        '''
        Bibliotecas necessárias:
        pip install python-barcode
        '''
        pass

    def createBarCode(self):
        _file = 'barcode.txt'
        _barText = ''

        if not os.path.exists(_file):
            return

        with open(_file, 'r') as fi:
            _barText = fi.read()
            fi.close()

        _code128 = Code128(_barText, writer=ImageWriter())

        _imgFile = 'barCode.png'

        if os.path.exists(_imgFile):
            os.remove(_imgFile)

        _code128.save(
            _imgFile[0:_imgFile.find('.')],
            {
                "module_width":0.35, 
                "module_height": 5, 
                "font_size": 0, 
                "text_distance": 1, 
                "quiet_zone": 3
            })

        _image = Image.open(_imgFile)

        hsize = int((float(_image.size[1])*.35))
        wsize = int((float(_image.size[0])*.35))

        _shrinkImage =  _image.resize((wsize, hsize), Image.ANTIALIAS)
        _shrinkImage.save(_imgFile)

bc = ZionBarCode()
bc.createBarCode()
