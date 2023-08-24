import face_recognition
import cv2


def show_landmark_location(image, isLocations=True, isLandmark=True):
    face_locations = face_recognition.face_locations(image)
    face_landmarks_list = face_recognition.face_landmarks(image)

    if isLandmark:
        for key, coors in face_landmarks_list[0].items():
            for coor in coors:
                image = cv2.circle(image, coor, 1, (0, 255, 0), 2)

    if isLocations:
        top, right, bottom, left = face_locations[0]
        image = cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)

    return image


def compare2face(im1_location, im2_location):
    # Load Image from Each Location
    known_image = face_recognition.load_image_file(im1_location)
    unknown_image = face_recognition.load_image_file(im2_location)

    # Encoding Process
    biden_encoding = face_recognition.face_encodings(known_image)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

    # Get Landmark Location such as location of eyes, nose, chin, etc
    known_image = show_landmark_location(known_image)
    unknown_image = show_landmark_location(unknown_image)

    # Compare 2 image
    results = face_recognition.compare_faces([biden_encoding], unknown_encoding)

    # Resize image for concatenate
    H, W, _ = unknown_image.shape
    known_image = cv2.resize(known_image, (W, H))

    # Horizontal concatenate
    concat_image = cv2.hconcat([known_image, unknown_image])

    H, W, _ = concat_image.shape

    x, y, w, h = W // 2, H // 2, 200, 50

    # Draw black background rectangle
    concat_image = cv2.rectangle(concat_image, (x - 200, y - 200), (x + w, y + h), (255, 255, 255), -1)

    # Add text
    concat_image = cv2.putText(concat_image, str(results[0]), (x - 200, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 0, 0),
                               2)

    concat_image = cv2.resize(concat_image, (960, 540))
    cv2.imshow("Image", concat_image)
    cv2.waitKey(0)


# Ganti Lokasi Gambar saja
im1_path = "data/jokowi-1.jpg"
im2_path = "data/jokowi.jpg"
compare2face(im1_path, im2_path)
