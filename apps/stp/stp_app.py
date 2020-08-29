# 车辆识别细分类问题
from apps.stp.fgvc.fgvc_app import FgvcApp

class StpApp(object):
    def __init__(self):
        self.refl = 'apps.stp.fgvc.StpApp'

    def startup(self, args={}):
        app = FgvcApp()
        app.startup(args)