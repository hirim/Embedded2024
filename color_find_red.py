import cv2
import numpy as np
from picamera2 import Picamera2
import time

def main():
    # Picamera2 초기화 및 설정
    picam2 = Picamera2()
    config = picam2.create_preview_configuration(main={"size": (320, 240)})
    picam2.configure(config)
    picam2.start()
    
    # 카메라 준비 시간
    time.sleep(0.1)

    # 색상 범위 설정 (HSV)
    lower_blue = np.array([100, 100, 120])
    upper_blue = np.array([150, 255, 255])

    lower_green = np.array([50, 150, 50])
    upper_green = np.array([80, 255, 255])

    lower_red1 = np.array([0, 50, 50])
    upper_red1 = np.array([10, 255, 255])

    lower_red2 = np.array([170, 50, 50]) 
    upper_red2 = np.array([180, 255, 255]) 

    # 카메라에서 프레임 읽기 및 처리 루프
    while True:
        # Picamera2에서 프레임 가져오기
        frame = picam2.capture_array()

        # BGR에서 HSV로 변환
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # 각각의 색상에 대해 마스크 생성
        redMask1 = cv2.inRange(hsv, lower_red1, upper_red1) 
        redMask2 = cv2.inRange(hsv, lower_red2, upper_red2) 
        redMask = cv2.bitwise_or(redMask1, redMask2) 

        #redMask = cv2.inRange(hsv, lower_red, upper_red)
        greenMask = cv2.inRange(hsv, lower_green, upper_green)
        blueMask = cv2.inRange(hsv, lower_blue, upper_blue)

        # 마스크를 사용하여 색상 부분 추출
        red = cv2.bitwise_and(frame, frame, mask=redMask)
        green = cv2.bitwise_and(frame, frame, mask=greenMask)
        blue = cv2.bitwise_and(frame, frame, mask=blueMask)

        # 결과를 화면에 출력
        cv2.imshow('Frame', frame)
        cv2.imshow('Red', red)
        cv2.imshow('Green', green)
        cv2.imshow('Blue', blue)

        # 키 입력을 기다리고 'q'를 누르면 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 모든 창 닫기
    cv2.destroyAllWindows()
    picam2.stop()

if __name__ == "__main__":
    main()
