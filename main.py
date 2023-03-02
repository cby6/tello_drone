import robomaster
from robomaster import robot
from robomaster import camera
import cv2
import time

robomaster.config.LOCAL_IP_STR = '192.168.10.2'
tl_drone = robot.Drone()
tl_drone.initialize()
tl_flight = tl_drone.flight
tl_flight.takeoff().wait_for_completed()
tl_camera= tl_drone.camera
tl_camera.start_video_stream(display=False)
tl_camera.set_fps("middle")
tl_camera.set_resolution("high")
tl_camera.set_bitrate(6)
for i in range(0, 5):
    img = tl_camera.read_cv2_image()
    cv2.imwrite(f'img{i}.jpg', img)
cv2.destroyAllWindows()
tl_camera.stop_video_stream()
# tl_flight.forward(distance=20).wait_for_completed()
tl_flight.land().wait_for_completed()
tl_drone.close()


