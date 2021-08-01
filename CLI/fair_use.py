from time import perf_counter
from cliutils import type_writer_anim
import cv2
import numpy as np
import sys

class ImageChecker():
    def __init__(self, one:str, two:str):
        self.one = one.strip().rstrip()
        self.two = two.strip().rstrip()
        print(type(self.one), self.one)
    def checkTwoVid(self):
        good_matches = []
        one = []
        two = []
        cap = cv2.VideoCapture(self.one)
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                print('here')
                one.append(frame)
            else:
                break
        cap.release()
        cap = cv2.VideoCapture(self.two)
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                two.append(frame)
            else:
                break
        cap.release()
                


        def checkTwoImages(original, image_to_compare):
            same = 0
            diff = []
            # good_matches = []
            if original.shape == image_to_compare.shape:
                # print("The images have same size and channels")
                difference = cv2.subtract(original, image_to_compare)
                b, g, r = cv2.split(difference)

                if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
                    # print("The images are completely Equal")
                    same+=1
                else:
                    diff.append(original)

            # 2) Check for similarities between the 2 images
            sift = cv2.xfeatures2d.SIFT_create()
            kp_1, desc_1 = sift.detectAndCompute(original, None)
            kp_2, desc_2 = sift.detectAndCompute(image_to_compare, None)

            index_params = dict(algorithm=0, trees=5)
            search_params = dict()
            flann = cv2.FlannBasedMatcher(index_params, search_params)

            matches = flann.knnMatch(desc_1, desc_2, k=2)

            good_points = []
            for m, n in matches:
                if m.distance < 0.6*n.distance:
                    good_points.append(m)

            # Define how similar they are
            number_keypoints = 0
            if len(kp_1) <= len(kp_2):
                number_keypoints = len(kp_1)
            else:
                number_keypoints = len(kp_2)



            good_matches.append(len(good_points) / number_keypoints * 100)

            
        x = len(one) if len(one)<len(two) else len(two)
            
        for i in range(x):
            # print("here")
            checkTwoImages(one[i], two[i])
            print('done' + str(i))

        match_percent = (len([x for x in good_matches if x >= 50])/len(one))*100
        

        if match_percent<=50:
            print()
            type_writer_anim("Your Video Falls under Fair use. You have nothing to worry The {x} of the copyrighted material found is {per} \n".format(x = '%', per = match_percent))
        else:
            print()
            type_writer_anim("You should reduce the amount of copyrighted content from your video.\n The {x} of the copyrighted material found is {per} \n".format(x = '%', per = match_percent))



# cap = cv2.VideoCapture('ex.avi')
# one = []
# two = []


# while(cap.isOpened()):
#     ret, frame = cap.read()
#     if ret == True:
#         one.append(frame)
#     else:
#         break
# cap.release()
# two = one
# good_matches = []


