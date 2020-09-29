import cv2

vidcap = cv2.VideoCapture('LHS_0.mp4')
success,image = vidcap.read()
count = 210
framecount = 0
success = True
while success:
    vidcap.set(cv2.CAP_PROP_POS_MSEC,(framecount*10000))
    success,image = vidcap.read()
    print ('Read a new frame: ', success)
    cv2.imwrite("frames/%d.jpg" % count, image)     # save frame as JPEG file
    count = count + 1
    framecount = framecount + 1