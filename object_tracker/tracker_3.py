from ultralytics import YOLO
import cv2

from sort.sort import *
import numpy as np

from utils.util import get_car, read_license_plate, write_csv

class Tracker:

    def __init__(self):
        # load models
        self.vehicle_detection_model = YOLO("yolov8x.pt")
        self.license_plate_detector = YOLO("C:\\ANPR & ATCC\\License_plate_yoloModel\\new_best.pt")
        self.results = {}
        self.mot_tracker = Sort()
        self.vehicles = [2, 3, 5, 7]

    def process_video(self, frames):

        for frame_no, frame in enumerate(frames):
            self.results[frame_no] = {}

            detections = self.vehicle_detection_model(frame)[0]
            detections_ = []

            for detection in detections.boxes.data.tolist():
                x1, y1, x2, y2, score, class_id = detection
                if int(class_id) in self.vehicles:
                    detections_.append([x1, y1, x2, y2, score])

            track_ids = self.mot_tracker.update(np.asarray(detections_))

            # detect license plates
            license_plates = self.license_plate_detector(frame)[0]
            for license_plate in license_plates.boxes.data.tolist():
                x1, y1, x2, y2, score, class_id = license_plate

                # assign license plate to car
                xcar1, ycar1, xcar2, ycar2, car_id = get_car(license_plate, track_ids)

                if car_id != -1:

                    # crop license plate
                    license_plate_crop = frame[int(y1):int(y2), int(x1): int(x2), :]

                    # process license plate

                    sharpen_kernel = np.array([[-1, -1, -1], [-1, 10, -1], [-1, -1, -1]])
                    license_plate_crop_thresh = cv2.filter2D(license_plate_crop, -1, sharpen_kernel)

                    license_plate_crop_thresh = 255 - license_plate_crop_thresh

                    object_filename = f"data1/{x1}_{car_id}.jpg"
                    cv2.imwrite(object_filename, license_plate_crop_thresh)

                    # read license plate number
                    license_plate_text, license_plate_text_score = read_license_plate(license_plate_crop_thresh)

                    if license_plate_text is not None:
                        self.results[frame_no][car_id] = {'car': {'bbox': [xcar1, ycar1, xcar2, ycar2]},
                                                      'license_plate': {'bbox': [x1, y1, x2, y2],
                                                                        'text': license_plate_text,
                                                                        'bbox_score': score,
                                                                        'text_score': license_plate_text_score}}

        # write results
        write_csv(self.results, "C:\\ANPR & ATCC\\output\\test1.csv")