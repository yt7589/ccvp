#
from apps.stp.stp_app import StpApp

MODE_1 = 101 # 车辆细粒度识别应用

def run_stp_app(args={}):
    app = StpApp()
    app.startup(args)

def main(args):
    print('综合计算视觉平台 v0.0.1')
    mode = MODE_1
    if MODE_1 == mode:
        run_stp_app(args)
    
if '__main__' == __name__:
    main({})