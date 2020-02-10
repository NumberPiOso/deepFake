import face_recognition

def crop_faces(image):
    '''
    Receives a images and returns the cropped of the face in the image.
    Inputs:
        image (array of ints) usually np.ndarray
            dim n1 x n2 x n3 where n3 usually represents the differents colors.
    Output:
        status (bool):
            Ok if a face was found.
        cropped_face (array of ints)
            subarrays of Image if face was found.
    '''
    face_locations = face_recognition.face_locations(image)
    faces_imgs = []
    for face_location in face_locations:
        top, right, bottom, left = face_location
        face_image = image[top:bottom, left:right]
        faces_imgs.append(face_image)
    return faces_imgs

