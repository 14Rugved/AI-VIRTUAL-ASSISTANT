elif 'detect face' in query.lower():
                print("Detecting faces...")
                face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

                # Initialize webcam
                cap = cv2.VideoCapture(0)

                while True:
                    # Read frame from webcam
                    ret, frame = cap.read()

                    # Convert frame to grayscale for face detection
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                    # Detect faces in the grayscale frame
                    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

                    # Draw rectangles around the detected faces and display label
                    for (x, y, w, h) in faces:
                        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                        cv2.putText(frame, 'Face', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

                    # Display the resulting frame
                    cv2.imshow('Face Detection', frame)

                    # Break the loop if 'q' is pressed
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

                # Release the webcam and close all windows
                cap.release()
                cv2.destroyAllWindows()