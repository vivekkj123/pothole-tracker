import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Initialize Firebase with your credentials
cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://pothole-detector.firebaseio.com/'
})

# Function to send detected potholes to Firebase
def send_pothole_to_firebase(pothole_data):
    ref = db.reference('potholes')
    ref.push().set(pothole_data)

# Modify your inference function to include sending pothole data to Firebase
def inference(stop_flag, preprocessed_frame_queue, detections_queue, fps_queue,
              network, class_names, threshold):
    while not stop_flag.is_set():
        darknet_image = preprocessed_frame_queue.get()
        prev_time = time.time()
        detections = darknet.detect_image(network, class_names, darknet_image, thresh=threshold)
        fps = 1 / (time.time() - prev_time)
        detections_queue.put(detections)
        fps_queue.put(int(fps))
        print("FPS: {:.2f}".format(fps))
        darknet.print_detections(detections, args.ext_output)
        # Iterate through detections to find potholes and send them to Firebase
        for label, confidence, bbox in detections:
            if label == "pothole" and confidence >= 0.85:  # Assuming "pothole" is the label for potholes
                # Calculate GPS coordinates and create pothole data
                # Replace these dummy values with actual GPS coordinates
                latitude = 0.0
                longitude = 0.0
                pothole_data = {
                    'latitude': latitude,
                    'longitude': longitude,
                    'confidence': confidence
                }
                send_pothole_to_firebase(pothole_data)
                print("Pothole Detected. Sending to DB")
        darknet.free_image(darknet_image)

# Modify your main block to include Firebase initialization
if __name__ == "__main__":
    args = parser()
    check_arguments_errors(args)
    # Initialize Firebase
    cred = credentials.Certificate("credentials.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://pothole-detector.firebaseio.com/'
    })
    # Rest of your main block remains unchanged
