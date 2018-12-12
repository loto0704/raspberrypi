import os

camera_shutter =os.system('raspistill -o raspi-camera-1.jpg') # 撮影を以下の名前で保存する．
check_camera = os.system('vcgencmd get_camera')

check_ls = os.system('ls')
print(type(check_ls))
