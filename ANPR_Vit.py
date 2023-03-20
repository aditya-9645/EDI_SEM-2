import cv2

haarcascade = "C:/Users/Aditya Bhosale/PycharmProjects/pythonProject1/model/haarcascade_russian_plate_number.xml"

cap = cv2.VideoCapture(0);

cap.set(3, 640)  # width
cap.set(4, 480)  # height

min_area = 500
count = 0
while (cap.isOpened()):
    ret, frame = cap.read()

    plate_cascade = cv2.CascadeClassifier(haarcascade)
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

    for (x, y, w, h) in plates:
        area = w * h

        if area > min_area:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0),2)
            cv2.putText(frame,"Number Plate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,0),2)

            frame_roi = frame[y: y+h, x:x+w]
            cv2.imshow("ROI",frame_roi)


    cv2.imshow("Result",frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("Resources/scanned_frame_"+str(count)+".jpg",frame_roi)
        cv2.rectangle(frame,(390,410),(620,460),(0,255,0),cv2.FILLED)
        cv2.putText(frame,"Frame saved",(400,440),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255),2)
        cv2.imshow("Results",frame)
        cv2.waitKey(500)
        count += 1
