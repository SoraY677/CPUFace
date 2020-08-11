import time
import threading
from multiprocessing import Process,Value
import cv2
import sys

# 諸設定
delay = 1
window_name = 'frame'

# アニメーション関連
cap_list = [cv2.VideoCapture(str('Scene' + str(i+1) + '.mp4')) for i in range(2)]

# 動作しているアニメーション番号
ins = Value('i',-1)

for cap in cap_list:
  if not cap.isOpened():
      sys.exit()


def animation(ins):
    target_cap = cap_list[0]
    print(ins.value)

    while(True):
        ret, frame = target_cap.read()

        if ret:
            cv2.imshow(window_name, frame)
            if cv2.waitKey(delay) & 0xFF == ord('q'):
                break
        else:
          target_cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
          if ins.value != -1:
            target_cap = cap_list[ins.value]



if __name__ == '__main__':
    anim_thread = Process(target = animation,args=[ins])#threading.Thread(target= animation)
    anim_thread.start()
    while True:
      print("入力:")
      ins.value = int(input())

cv2.destroyWindow(window_name)
