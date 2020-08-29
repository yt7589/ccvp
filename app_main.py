#
from apps.stp.fgvc.fgvc_app import FgvcApp

MODE_1 = 101 # 车辆细粒度识别应用

def run_fgvc_app(args={}):
    app = FgvcApp()
    app.startup()

def main(args):
    print('综合计算视觉平台 v0.0.1')
    mode = MODE_1
    if MODE_1 == mode:
        run_fgvc_app(args)
    
if '__main__' == __name__:
    main({})