#

class CodisApp(object):
    def __init__(self):
        self.refl = 'apps.codis.CodisApp'

    def startup(self, args={}):
        print('综合视觉平台：Resnet+FPN+MultiTask')