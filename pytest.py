import cv2
import numpy as np

# img = np.zeros((3, 3), dtype=np.uint8)
#
# img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
#
# print(img)
# print(cv2.__file__)

img = cv2.imread('imgsource/wife.jpg')
# print(img.item(150, 120, 0))
#
# img.itemset((150, 120, 0), 255)
# print(img.item(150, 120, 0))

img[:, :, 0] = 0
img[:, :, 1] = 0
# img[:, :, 2] = 0

# img[0:800, 0:800, 1] = 0

my_roi = img[0:800, 0:800]
img[200:1000, 200:1000] = my_roi

# cv2.imshow('img', img)
# cv2.waitKey()
# cv2.destroyAllWindows()

# print(img.shape)
# print(img.size)
# print(img.dtype)

# cameraCap1 = cv2.VideoCapture(0)
# cameraCap2 = cv2.VideoCapture(1)
# # 这里的fps是猜的，不同设备一般不一样，后面想办法找到合适的fps
# fps = 15
# size = (
#     int(cameraCap1.get(cv2.CAP_PROP_FRAME_WIDTH)),
#     int(cameraCap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
# )
# videoWriter = cv2.VideoWriter(
#     'imgtarget/cam.m4v',
#     cv2.VideoWriter_fourcc('I', '4', '2', '0'),
#     fps,
#     size
# )
# # cv2.namedWindow('mywindow')
# success1, frame1 = cameraCap1.read()
# success2, frame2 = cameraCap2.read()
# while success1 and success2 and cv2.waitKey(1) == -1:
#     # 视频的每一帧也是图像，所以可以把它当图像处理，实现相应的效果
#     frame1[:, :, 1] = 0
#     frame1[0:frame2.shape[0], 0:frame2.shape[1]] = frame2
#     # 注意：这里写入的frame大小需要与videoWriter大小一致。当然我们可以将frame截取到相应大小后，再赋值
#     videoWriter.write(frame1)
#     cv2.imshow('mywindow', frame1)
#     success1, frame1 = cameraCap1.read()
#     success2, frame2 = cameraCap2.read()


cv2.imwrite('imgtarget/wife1.jpg', img)

