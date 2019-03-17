import cv2
import os


if __name__ == '__main__':
    data_names = os.listdir("../data/video")
    data_names = ["../data/video/" + i for i in data_names]
    datas = []
    for i in data_names:
        a = os.listdir(i)
        data = [i+'/'+j for j in a]
        datas += data
    num = 0
    for i in datas:
        print(i)
        cap = cv2.VideoCapture(i)
        num_frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        num_img = num_frame // 36
        cnt = 0
        while 1:
            ret, frame = cap.read()
            cnt += 1
            if cnt <= num_img*36:
                print('../data/image/' + str(num // 36) + '/' + str((cnt-1) % 36) + '.jpg')
                if not os.path.exists('../data/image/' + str(num // 36)):
                    os.mkdir('../data/image/' + str(num // 36))
                cv2.imwrite('../data/image/' + str(num // 36) + '/' + str((cnt-1) % 36) + '.jpg', frame)
                num += 1
            else:
                break
