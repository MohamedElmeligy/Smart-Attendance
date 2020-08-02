import face_recognition
import cv2
import os
import pyttsx3

attend = []

def intialize():
    attendance = []
    
    # Get a reference to webcam #0 (the default one)
    video_capture = cv2.VideoCapture(0)
    engine = pyttsx3.init()
    engine.setProperty('rate', 130)    
    engine.setProperty('volume', 0.9)    
    return video_capture,engine,attendance 

def loadData(file):
    x=0
    known_face_image = []
    known_face_encoding = []
    known_face_name = []
    
    for image in os.listdir(file):
        print(image)
        # Load a sample picture and learn how to recognize it.
        known_face_image.append (face_recognition.load_image_file(file+"\\"+image))
        known_face_encoding.append (face_recognition.face_encodings(known_face_image[x])[0])
        known_face_name.append(image.split(".")[0])
        x=x+1
    
    return known_face_encoding,known_face_name

def captureFrame(video_capture):
    # Grab a single frame of video
    ret, frame = video_capture.read()         
    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]
    
    return frame,rgb_small_frame

def compareFaces(rgb_small_frame,eco,engine,attendance,known_face_encodings,known_face_names):
    
    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    face_names = []
    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding,tolerance = .5)
        name = "Unknown"
        
        # If a match was found in known_face_encodings, just use the first one.
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
            if eco:
                engine.say("Hello Doctor " + name )
                engine.runAndWait()
                engine.stop()
                eco = False

        face_names.append(name)
        if not (name in attendance):
            attendance.append(name)         
        
    return face_names,face_locations,eco,attendance

def repeatSound():
    if cv2.waitKey(1) & 0xFF == ord('a'):
        return True
    
            
def writeNames(frame,face_names,face_locations):
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 0), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
    return frame


def run():   
    global attend
    known_face_encodings,known_face_names = loadData("F:\PythonProjects\img\Known")
    video_capture,engine,attendance = intialize()
    eco = True

    while True:   

        frame,rgb_small_frame = captureFrame(video_capture)

        face_names,face_locations,eco,attend = compareFaces(rgb_small_frame,eco,engine,attendance,known_face_encodings,known_face_names)
        if not eco:
            eco = repeatSound()

        frame = writeNames(frame,face_names,face_locations)
        cv2.imshow('Face Recognition', frame)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    attend.remove("Unknown")       
    video_capture.release()
    cv2.destroyWindow('Face Recognition')
    

def attendance():
    return attend


