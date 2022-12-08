# prompt: Python code for detecting people in a video and then tracking detected people for 5 seconds before detecting again
# prompt: the tracking code does not include any opencv trackers, it should

import cv2

# define video capture
capture = cv2.VideoCapture(0)

# define HOG person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# define tracking duration
tracking_duration = 5  # seconds

# game loop
while True:
    # capture frame
    _, frame = capture.read()

    # detect people
    people, _ = hog.detectMultiScale(frame)

    # create tracking objects
    trackers = []
    for (x, y, w, h) in people:
        # create tracking object
        tracker = cv2.TrackerKCF_create()
        tracker.init(frame, (x, y, w, h))
        trackers.append(tracker)

    # track detected people for a certain duration
    tracking_time = 0  # seconds
    while len(trackers) > 0 and tracking_time < tracking_duration:
        # capture next frame
        _, frame = capture.read()

        # update trackers
        success, boxes = [], []
        for tracker in trackers:
            success_, box = tracker.update(frame)
            success.append(success_)
            boxes.append(box)

        # remove failed trackers
        trackers = [tracker for (success_, tracker) in zip(success, trackers) if success_]
        boxes = [box for (success_, box) in zip(success, boxes) if success_]

        # draw detection bounding boxes
        for (x, y, w, h) in boxes:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # show frame
        cv2.imshow("Frame", frame)

        # increment tracking time
        tracking_time += 1

        # check for user input
        key = cv2.waitKey(1)
        if key == ord("q"):
            # end program
            break

