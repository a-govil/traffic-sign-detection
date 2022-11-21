from keras.models import load_model
from imutils.video import VideoStream

#load model
model = load_model('model/TSR.h5')

#initialize video stream
print ('[INFO] starting video stream...')
vs=VideoStream(src=0).start()

