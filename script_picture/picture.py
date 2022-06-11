import cv2
from datetime import datetime

# video capture source camera (Here webcam of laptop)

route = 1

cap = cv2.VideoCapture(1)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while(True):

    now = datetime.now()
    hour = now.strftime("%H")
    minute = now.strftime("%M")

    if hour == '18' and minute == '13':
        ret, frame = cap.read()  # return a single frame in variable `frame`
        cv2.imwrite(
            'D:/Universidad/S9/PdG/workspace/script_picture/images/cap'+str(route)+'.png', frame)
        route += 1
        cv2.destroyAllWindows()
        break

cap.release()
