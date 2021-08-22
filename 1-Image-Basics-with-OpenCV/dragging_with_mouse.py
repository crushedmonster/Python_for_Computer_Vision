import cv2
import numpy as np


# VARIABLES
# True while mouse button down, False while button up
drawing = False
ix, iy = -1, -1

# FUNCTION
# create a function to draw a rectangle from one point
# and it's going to keep drawing until we drag and release the mouse
def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        # when we click down with left mouse button drawing is set to True
        drawing = True
        # then we take note of where that mouse was located
        ix, iy = x, y
        
    elif event == cv2.EVENT_MOUSEMOVE:
        # now the mouse is moving
        if drawing == True:
            # if drawing is True, it means we've already clicked on the left mouse button
            # we draw a rectangle from the previous position to the x, y where the mouse is
            # draw a filled in green rectangle
            cv2.rectangle(img, (ix, iy), (x, y),(0, 255, 0), -1)
           
    elif event == cv2.EVENT_LBUTTONUP:
        # once we lift up (release) the mouse button, drawing is set to False
        drawing = False
        # we've completed drawing the rectangle
        cv2.rectangle(img, (ix, iy), (x, y),(0, 255, 0), -1)
        

# create a black image
img = np.zeros(shape = (512,512,3))
# this names the window so we can reference it 
cv2.namedWindow(winname = 'my_drawing')
# connects the mouse button to our callback function
cv2.setMouseCallback('my_drawing', draw_rectangle)


while True:# runs forever until we break with Esc key on keyboard
    # shows the image window
    cv2.imshow('my_drawing',img)
    # EXPLANATION FOR THIS LINE OF CODE:
    # https://stackoverflow.com/questions/35372700/whats-0xff-for-in-cv2-waitkey1/39201163
    
    # check to see if the ESC key was pressed on keyboard
    if cv2.waitKey(1) & 0xFF == 27:
        break
# once script is done, its usually good practice to call this line
# it closes all windows (just in case you have multiple windows called)
cv2.destroyAllWindows()