import face_recognition
import cv2
image = cv2.VideoCapture(0)
import os
j = 0
dire = r"C:\Users\mohan\OneDrive\Desktop\Face Recognition\Images"
while True:
    check, frame = image.read()
##    face_locations = face_recognition.face_locations(frame)
##    for top, right, bottom, left in face_locations:
            # Draw a box around the face
            
##        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
    cv2.imshow("Capturing", frame)
    key = cv2.waitKey(1)
    if key == ord('s'):
        j = j+1
        if not os.path.exists(dire):
            os.mkdir(dire)
        y = os.path.join(dire,"image")
        w = y+ str(j)
        z = w + str(".jpg")
        cv2.imwrite(z, img=frame)

        
        
        
    elif key == ord('q'):
##        print("Turning off camera.")
        image.release()

        cv2.destroyAllWindows()
        break
        

    
    
    




##images = face_recognition.load_image_file("image.jpg")
##face_locations = face_recognition.face_locations(images)
##for top, right, bottom, left in face_locations:
##            # Draw a box around the face
##            
##            cv2.rectangle(images, (left, top), (right, bottom), (0, 255, 0), 2)
##            roi_color = images[top:bottom, left:right] 
##            print("[INFO] Object found. Saving locally.") 
##            cv2.imwrite('total_faces.jpg', roi_color) 

 


##status = cv2.imwrite('faces_detected.jpg', images)
##print("[INFO] Image faces_detected.jpg written to filesystem: ", status)

