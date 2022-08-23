from cvlib.object_detection import YOLO
import cv2
from tkinter import filedialog
from tkinter import *
root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/home/pi/skripsi/Sekeripsi/data/images",title = "choose your file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
weights="best.weights"
config="yolov4-custom.cfg"
labels="obj.names"
img=cv2.imread(root.filename)
img=cv2.resize(img,(680,460))
yolo = YOLO(weights, config,labels)
bbox, label, conf = yolo.detect_objects(img)
img1=yolo.draw_bbox(img, bbox, label, conf)
cv2.imshow("img1",img)
cv2.waitKey(1)