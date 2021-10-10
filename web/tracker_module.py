#  I need to thank Adrian for his great tutorial on openCV trajectory estimation 
#  This is his website which contains tons and tons of Image Processing tutoria-
#  ls with openCV and python
#  www.pyimagesearch.com

# import the necessary packages
from ai_model import AImodel
from collections import deque
import numpy as np
import base64
# from app.config import *
import imutils
import cv2



class TrajectoryEstimationModel(AImodel):
	def __init__(self,buffer):
		self.frames = []
		self.pts =deque(maxlen=buffer)
	def process(self,input):
		try:
			if not input:
				self.pts.clear()
				return b'',[]
			self.frames.append(input)
			# construct the argument parse and parse the arguments
			args = {'frame':input}
			# define the lower and upper boundaries of the "green"
			# ball in the HSV color space, then initialize the
			# list of tracked points
			greenLower = (29, 86, 6)
			greenUpper = (64, 255, 255)
			
			im_bytes = base64.b64decode(input)
			im_arr = np.frombuffer(im_bytes, dtype=np.uint8)  # im_arr is one-dim Numpy array
			frame = cv2.imdecode(im_arr, flags=cv2.IMREAD_COLOR)

				# grab the current frame
				# frame = img
				# handle the frame from VideoCapture or VideoStream
				# frame = frame[1] if args.get("video", False) else frame
				# if we reached the end of the video
			# blur it, and convert it to the HSV
			# color space
			
			blurred = cv2.GaussianBlur(frame, (11, 11), 0)
			hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
			# construct a mask for the color "green", then perform
			# a series of dilations and erosions to remove any small
			# blobs left in the mask
			mask = cv2.inRange(hsv, greenLower, greenUpper)
			mask = cv2.erode(mask, None, iterations=2)
			mask = cv2.dilate(mask, None, iterations=2)
			# find contours in the mask and initialize the current
			# (x, y) center of the ball
			cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
				cv2.CHAIN_APPROX_SIMPLE)
			cnts = imutils.grab_contours(cnts)
			center = None

			# only proceed if at least one contour was found
			if len(cnts) > 0:
				# find the largest contour in the mask, then use
				# it to compute the minimum enclosing circle and
				# centroid
				c = max(cnts, key=cv2.contourArea)
				((x, y), radius) = cv2.minEnclosingCircle(c)
				M = cv2.moments(c)
				center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

				# only proceed if the radius meets a minimum size
				if radius > 10:
					# draw the circle and centroid on the frame,
					# then update the list of tracked points
					cv2.circle(frame, (int(x), int(y)), int(radius),
						(0, 255, 255), 2)
					cv2.circle(frame, center, 5, (0, 0, 255), -1)

			# update the points queue
			self.pts.appendleft(center)
			# loop over the set of tracked points
			for i in range(1, len(self.pts)):
				# if either of the tracked points are None, ignore
				# them
				if self.pts[i - 1] is None or self.pts[i] is None:
					continue
				
				# otherwise, compute the thickness of the line and
				# draw the connecting lines
				thickness = int(np.sqrt(self.pts.maxlen / float(i + 1)) * 2.5)
				cv2.line(frame, self.pts[i - 1], self.pts[i], (0, 0, 255), thickness)

			# show the frame to our screen
			_, im_arr = cv2.imencode('.jpg', frame)
			im_bytes = im_arr.tobytes()
			im_b64 = base64.b64encode(im_bytes)
			return im_b64,list(self.pts)
		except Exception as e:
			raise e