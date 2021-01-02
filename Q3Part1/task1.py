import tabula
import matplotlib
import io

from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pytesseract
from skimage.morphology import binary_opening, square
from skimage.filters import threshold_minimum
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.filters import gaussian

# im = gaussian(rgb2gray(imread('lettersig.jpg')), sigma=2)
# thresh = threshold_minimum(im)
# im = im > thresh
# im = im.astype(np.bool)
# plt.figure(figsize=(20,20))
# im1 = binary_opening(im, square(3))
# plt.imshow(im1)
# plt.axis('off')
# plt.show()    

# def isDataTable(data, contour):
# 	print(data)
# 	data2 = pytesseract.image_to_string(ROI, lang='eng', config='-c preserve_interword_spaces=1x1 --psm  1 --oem 3')
# 	return True;
table = []
file_ = "sample.pdf"
from pdf2image import convert_from_path , convert_from_bytes
  
  
# Store Pdf with convert_from_path function 
images = convert_from_path(file_, poppler_path= r'C:\Users\ayush\Downloads\Release-20.12.1\poppler-20.12.1\Library\bin') 
for img in images: 
    img.save('sample7.jpg', 'JPEG')
file = "sample7.jpg";
im1 = cv2.imread(file, 0)
im = cv2.imread(file)

original = im.copy();
greymain = cv2.cvtColor(im,cv2.COLOR_RGB2GRAY)
# greymain = cv2.resize(greymain, (0, 0), fx = 5, fy = 5)
th2 = cv2.adaptiveThreshold(greymain,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY_INV,39,10)
kernel =  np.ones((18, 18),np.float32)/25
dilation = cv2.dilate(th2,kernel,iterations = 1)
contours,heirarchy = cv2.findContours(dilation,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
maxarea = 0
cnt = contours[0]

canny = cv2.Canny(dilation, 500, 500);
print(canny)

boxes = [];


dimension = canny.shape[:2]

height_of_image = dimension[0]/70;
print(height_of_image)
# plt.subplot(1, 1, 1);
# plt.imshow(canny);
# print(len(boxes))
# plt.show();
for contour in contours:
	box = cv2.boundingRect(contour)
	[x, y, w, h] = cv2.boundingRect(contour)
	cv2.rectangle(canny,(x,y),(x+w,y+h),(0,256,0),10)
	if (height_of_image <= box[3]):
		print("Ok")
		[x, y, w, h] = cv2.boundingRect(contour)
		cv2.rectangle(canny,(x,y),(x+w,y+h),(256,0,0),10)
		thresh = 255 - cv2.threshold(greymain, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

		x,y,w,h = box[0], box[1], box[2],box[3]  
		ROI = thresh[y:y+h,x:x+w]
		data = pytesseract.image_to_string(ROI, lang='eng', config='-c preserve_interword_spaces=1 --psm  6 --oem 3')
		data2 = pytesseract.image_to_string(ROI, lang='eng', config='--psm 6 1')
		if (data!= data2): 
			print("I see a table  :D QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ")
			table.append([box, repr(data)])

		print(repr(data))
		#print(repr(data2))
		print("Oye oye oye oye oye ooo aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
		print(data2)
		# boxes.append(box)
		# print(box)
	


plt.subplot(1, 1, 1);
plt.imshow(canny);
print(len(table))
plt.show();

# with tesserocr.PyTessBaseAPI() as api:
#     image = Image.open(io.BytesIO("sample.png"))
#     api.SetImage(image)
#     api.Recognize()  # required to get result from the next line
#     iterator = api.GetIterator()
#     print(iterator.WordFontAttributes())

# for entry in table:

original2 = im.copy();
greymain2 = cv2.cvtColor(original2,cv2.COLOR_RGB2GRAY)
# greymain = cv2.resize(greymain, (0, 0), fx = 5, fy = 5)
th4 = cv2.adaptiveThreshold(greymain2,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY_INV,39,10)
kernel2 =  np.ones((7, 7),np.float32)/25
dilation2 = cv2.dilate(th4,kernel2,iterations = 1)
contours2,heirarchy2 = cv2.findContours(dilation2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
maxarea2 = 0
cnt2 = contours2[0]

canny2 = cv2.Canny(dilation2, 500, 500);

hash_of_boxes_to_get_tables = {}

for contour in contours2:
	box = cv2.boundingRect(contour)
	[x, y, w, h] = cv2.boundingRect(contour)
	# for dubdub in boxes:
	# 	if dubdub[0] >= x and dubdub[1] >= y && dubdub[2] <= w && dubdub[3] <= h:
	# 		hash_of_boxes_to_get_tables[boxes] = []
	# 		hash_of_boxes_to_get_tables.append(dubdub);
	cv2.rectangle(canny2,(x,y),(x+w,y+h),(127, 128,0),10)
boxes = [];



plt.subplot(1, 1, 1);
plt.imshow(canny2);
plt.show();

#now that we have akk major boxes, we will process each box to detect if it si a table or not. if it is a table then do the mongo stuff. 
# for img in images: 
#     img.save('sample2.jpg', 'JPEG')
from pymongo import MongoClient 

myclient = MongoClient("mongodb://localhost:27017/")  
   
# database  
db = myclient["Q3_A"] 
tollection = db[file_[:len(file_) - 4]]   
print(table)
di = {}
i = 0; 
for k in table:
	di[str(i)] = k
	print("AJ")
	i += 1;

print("KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK")
rec = tollection.insert_one(di);
print(rec.inserted_id)