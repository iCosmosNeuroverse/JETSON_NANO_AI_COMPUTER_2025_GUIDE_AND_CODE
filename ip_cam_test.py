import cv2

url = "http://192.168.100.192:8080/video"  #Example, supply your own phone ip here, didn't parametrize the file unlike self_drive.py, self_drive_basic.py and manage_.py which I did parametrize to allow runtime argument.

cap = cv2.VideoCapture(url)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("No frame received")
        continue

    cv2.imshow("IP Webcam Test", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

