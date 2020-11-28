import os

from PIL import Image
import qrcode
from qrcode.image.pure import PymagingImage

class Zion_QrCode:

    def __init__(self):
        '''
        Bibliotecas necessárias:
        pip install qrcode
        pip install pillow
        pip install git+git://github.com/ojii/pymaging.git#egg=pymaging
        pip install git+git://github.com/ojii/pymaging-png.git#egg=pymaging-png
        '''

        self.Qr = None

    def createQrCode(self):
        _qrText = ''
        _file = 'qrCode.txt'

        if not os.path.exists(_file):
            return

        with open(_file, 'r') as fi:
            _qrText = fi.read()
            fi.close()

        self.Qr = qrcode.QRCode(
            version = 1,
            error_correction = qrcode.constants.ERROR_CORRECT_H,
            box_size = 10,
            border = 4
        )

        self.Qr.add_data(_qrText)
        self.Qr.make()

        img = self.Qr.make_image()

        _file = 'qrImage.png'
        img.save(_file)

        return _file

    def resizeImage(self, imageFile):
        _newFile = 'newQrCode.png'

        if os.path.exists(_newFile):
            os.remove(_newFile)

        _image = Image.open(imageFile)

        hsize = int((float(_image.size[1])*.25))
        wsize = int((float(_image.size[0])*.25))

        _shrinkImage =  _image.resize((wsize, hsize), Image.ANTIALIAS)
        _shrinkImage.save(_newFile)

        os.remove(imageFile)

qr = Zion_QrCode()
_imgFile = qr.createQrCode()
qr.resizeImage(_imgFile)
