import cv2
import numpy as np

###############
## FUNCTION ###
###############

# create a function based on a CV2 Event (right button click)
def draw_circle(event, x, y, flags, param):
    
    # here we specify the event as the right button has been clicked down
    if event == cv2.EVENT_RBUTTONDOWN:
        # draw empty red circles
        cv2.circle(img, (x, y), 100, (0, 0, 255), 10)

# this names the window so we can reference it 
cv2.namedWindow(winname='my_drawing')

# connects the mouse button to our callback function
cv2.setMouseCallback('my_drawing',draw_circle)        
        
################################
## SHOWING IMAGE WITH OPENCV ###
################################

# read dog_backpack.png
img = cv2.imread('../DATA/dog_backpack.jpg')

while True: # runs forever until we break with Esc key on keyboard
    # shows the image window
    cv2.imshow('my_drawing',img)
    # wait for 20 ms and someone has hit the Esc key
    if cv2.waitKey(20) & 0xFF == 27:
        break
# once script is done, its usually good practice to call this line
# it closes all windows (just in case you have multiple windows called)
cv2.destroyAllWindows()