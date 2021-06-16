import cv2
from pyzbar import pyzbar


def read_bar_code(frame):
    codes = pyzbar.decode(frame)
    for barcode in codes:
        x, y, w, z = barcode.rect
        #decoding the barcode
        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x,y), (x+w, y+z), (255, 0, 0))
        #selecting font for rectangle
        font = cv2.FONT_HERSHEY_PLAIN
        cv2.putText(frame, barcode_info, (x, y), font, 2.0, (255, 255, 0), 1)
    return frame

#main method

#1
def myFunc():
    vid = cv2.VideoCapture(0)
    ret, frame = vid.read()
    while ret:
        ret, frame = vid.read()
        frame = read_bar_code(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == 27:
            break
    vid.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    myFunc()

#2

# if __name__ == "__main__":
#     vid = cv2.VideoCapture(0)
#     ret, frame = vid.read()
#     while ret:
#         ret, frame = vid.read()
#         frame = read_bar_code(frame)
#         cv2.imshow('frame', frame)
#         if cv2.waitKey(1) == 27:
#             break
#     vid.release()
#     cv2.destroyAllWindows()
























