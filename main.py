import cozmo
import numpy as np
import cv2
def cozmo_program(robot: cozmo.robot.Robot):
    # Configure camera to output color images
    
    robot.camera.image_stream_enabled = True
    robot.camera.color_image_enabled = True
    robot.set_head_angle(cozmo.util.degrees(-10)).wait_for_completed()
    print("Streaming camera feed... Press CTRL+C to stop.")

    while True:
        latest = robot.world.latest_image
        if latest is None:
            continue

        # Convert to OpenCV image
        cv_img = np.array(latest.raw_image)
        # Show the image
        cv2.imshow("Cozmo Camera", cv_img)

        # Exit on 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

cozmo.run_program(cozmo_program)
