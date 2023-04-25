import cv2
vid = cv2.VideoCapture(0)
while(True):
    ref, frame = vid.read()
    image = cv2.putText(frame,'Welcome to AI ML class', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    cv2.imshow('Live Video', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("I am here")
        break
vid.release()
cv2.destroyAllWindows()
