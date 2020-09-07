import cv2
import time
import datetime
import numpy as np

tempo_de_video=180
fps_de_gravacao=15

cap = cv2.VideoCapture(0)  # Try out with your webcam
save_as = "caminho_completo_para_a_pasta_tmp"

fourcc = cv2.VideoWriter_fourcc(*'MJPG')  # set video extension type

# path_name, video type, frame rate, (image_width, image_height)

print(cap.get(cv2.CAP_PROP_FPS))


def iniciaGravacao(secs):
    string = time.strftime("%d%b%Y-%H_%M_%S", time.gmtime())
    print(string)
    video_writer = cv2.VideoWriter(
        save_as + '/'+ str(string) + '.avi', fourcc, fps_de_gravacao, (640, 480))
    init = time.time()
    print('gravando')
    while (init+secs) > time.time():
        image = cap.read()[1]
        video_writer.write(image)
        cv2.imshow('gravando', image)
        if cv2.waitKey(1) == 32:
            break
    video_writer.release()


def calculaDiferenca(img1, img2, img3):
    d1 = cv2.absdiff(img3, img2)
    d2 = cv2.absdiff(img2, img1)
    imagem = cv2.bitwise_and(d1, d2)
    s, imagem = cv2.threshold(imagem, 35, 255, cv2.THRESH_BINARY)
    if imagem.max() > 0:
        iniciaGravacao(tempo_de_video)
    return imagem


frame = cv2.cvtColor(cap.read()[1], cv2.COLOR_RGB2GRAY)
penultima = frame
antepenultima = frame
while (cap.isOpened()):
    antepenultima = penultima
    penultima = frame
    frame = cv2.cvtColor(cap.read()[1], cv2.COLOR_RGB2GRAY)
    # last_frame = cv2.cvtColor(last_frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Frame', calculaDiferenca(antepenultima, penultima, frame))
    cv2.imshow('color', cap.read()[1])

    if cv2.waitKey(1) == 32:
        cv2.destroyWindow(janela)
        break
    # time.sleep(1)

print("Fim")
