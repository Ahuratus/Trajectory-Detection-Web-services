from time import sleep
from typing import BinaryIO
from tracker_module import TrajectoryEstimationModel
# from ..ai_models.tracker_module import TrajectoryEstimationModel
import base64,cv2
import numpy as np
if __name__ == '__main__':
    tem = TrajectoryEstimationModel(10)
    vid = cv2.VideoCapture(0)
    try:
        while True:
            check, frame = vid.read()
            cv2.imwrite(filename='test.jpg', img=frame)
            f = open('test.jpg','rb')
            im_bytes = f.read()
            b64frame = base64.b64encode(im_bytes)
            res,pts = tem.process(b64frame)
            im_bytes = base64.b64decode(res)
            print(pts)
            im_arr = np.frombuffer(im_bytes, dtype=np.uint8)  # im_arr is one-dim Numpy array
            img = cv2.imdecode(im_arr, flags=cv2.IMREAD_COLOR)
            cv2.imshow('im',img)
            cv2.waitKey(1) 
            if(ord('q') == 0xFF):
                break
    except KeyboardInterrupt as e:
        print(e)
    except Exception as e:
        print(e)