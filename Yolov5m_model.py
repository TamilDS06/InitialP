import glob
import sys
import cv2
folder = glob.glob("C:\\Users\\User\\Downloads\\Vcount_output\\Output_frames\\Output**")
if len(folder) == 0:
    sys.exit()
else:
    for image in folder:
        frame = cv2.imread(image)
        cv2.imshow("Output", frame)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break