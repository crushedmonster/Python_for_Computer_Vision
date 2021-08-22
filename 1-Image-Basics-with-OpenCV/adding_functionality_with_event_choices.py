import cv2
import numpy as np

###############
## FUNCTION ###
###############

# create a function based on a CV2 Event (Left button click)
def draw_circle(event, x, y, flags, param):
    # x and y are automatically taken into effect by OpenCV
    # it basically says, ok, at what x position and what mouse position is the mouse set
    # event is what the mouse actually did
    # flags and parameters are also things that are passed in case there's additional parameters
    # or if there's warning flags that are necessary
    
    # here we specify the event as the left button has been clicked down
    if event == cv2.EVENT_LBUTTONDOWN:
        # note the x & y here is according to the mouse
        # make the colour totally green
        # create a filled in circle
        cv2.circle(img, (x, y), 100, (0, 255, 0), -1)
    
    # add another event 
    elif event == cv2.EVENT_RBUTTONDOWN:
        # make the colour totally blue
        # create a filled in circle
        # note: open cv reads colour channels as BGR
        cv2.circle(img, (x, y), 100, (255, 0, 0), -1)

# this names the window so we can reference it 
cv2.namedWindow(winname='my_drawing')

# connects the mouse button to our callback function
cv2.setMouseCallback('my_drawing',draw_circle)        
        
################################
## SHOWING IMAGE WITH OPENCV ###
################################

# create a black image
img = np.zeros((512,512,3), np.uint8)

while True: # runs forever until we break with Esc key on keyboard
    # shows the image window
    cv2.imshow('my_drawing',img)
    # EXPLANATION FOR THIS LINE OF CODE:
    # https://stackoverflow.com/questions/35372700/whats-0xff-for-in-cv2-waitkey1/39201163
    # wait for 20 ms and someone has hit the Esc key
    if cv2.waitKey(20) & 0xFF == 27:
        break
# once script is done, its usually good practice to call this line
# it closes all windows (just in case you have multiple windows called)
cv2.destroyAllWindows()