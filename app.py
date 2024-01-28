import cv2

image_path_1 = "Face-1.jpg"
image_path_2 = "test-3.jpg"

image_1 = cv2.imread(image_path_1)
image_2 = cv2.imread(image_path_2)

gray_1 = cv2.cvtColor(image_1, cv2.COLOR_BGR2GRAY)
gray_2 = cv2.cvtColor(image_2, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

faces_1 = face_cascade.detectMultiScale(gray_1, scaleFactor=1.3, minNeighbors=5)
faces_2 = face_cascade.detectMultiScale(gray_2, scaleFactor=1.3, minNeighbors=5)

for (x, y, w, h) in faces_1:
    cv2.rectangle(image_1, (x, y), (x+w, y+h), (0, 255, 0), 2)

for (x, y, w, h) in faces_2:
    cv2.rectangle(image_2, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow('Image 1', image_1)
cv2.imshow('Image 2', image_2)
cv2.waitKey(0)
cv2.destroyAllWindows()

def compare_faces(face1, face2):

    return True

if len(faces_1) == 1 and len(faces_2) == 1:
    face_1 = gray_1[y:y+h, x:x+w]
    face_2 = gray_2[y:y+h, x:x+w]

    if compare_faces(face_1, face_2):
        print("Same")
    else:
        print("Not Same")
else:
    print("Number of faces detected is not one in either image.")
