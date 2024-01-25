import face_recognition
from PIL import Image, ImageDraw

image_path_1 = "Face-1.jpg"  
image_path_2 = "test-1.jpg"

image_1 = face_recognition.load_image_file(image_path_1)
image_2 = face_recognition.load_image_file(image_path_2)

face_locations_1 = face_recognition.face_locations(image_1)
face_locations_2 = face_recognition.face_locations(image_2)

image_1_draw = Image.fromarray(image_1)
image_2_draw = Image.fromarray(image_2)
draw = ImageDraw.Draw(image_1_draw)

for face_location in face_locations_1:
    top, right, bottom, left = face_location
    draw.rectangle([left, top, right, bottom], outline="red")

image_1_draw.show()

face_encoding_1 = face_recognition.face_encodings(image_1, face_locations_1)[0]
face_encoding_2 = face_recognition.face_encodings(image_2, face_locations_2)[0]

results = face_recognition.compare_faces([face_encoding_1], face_encoding_2)
if results[0]:
    print("The faces are a match.")
else:
    print("The faces are not a match.")